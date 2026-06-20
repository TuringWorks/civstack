#!/usr/bin/env python3
"""
Build a self-contained, static, browsable site for the CivStack library.

- One rendered HTML page per skill, doc, and checklist; standalone HTML tools are copied into the site.
- A search/filter index page with the catalog inlined (works over file://, no fetch).
- No build dependencies beyond the Python standard library; no network; no JS frameworks.

Run:  python3 tools/build_site.py
Open: site/index.html  (double-click) — or:  python3 -m http.server -d site 8000
Host: commit site/ and point GitHub Pages at it, or copy site/ to any static host.
"""
import html
import os
import re
import shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS = os.path.join(ROOT, "skills")
DOCS = os.path.join(ROOT, "docs")
CHECKLISTS = os.path.join(ROOT, "checklists")
TOOLS = os.path.join(ROOT, "tools")
SITE = os.path.join(ROOT, "site")


# ---------------------------------------------------------------------------
# Minimal Markdown -> HTML (handles what the skills use: headings, lists,
# tables, blockquotes, code, bold/italic, links, hr).
# ---------------------------------------------------------------------------
def _inline(s):
    s = html.escape(s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", s)

    def link(m):
        text, href = m.group(1), m.group(2)
        if href.endswith("SKILL.md"):            # intra-skill link -> directory page
            href = href[:-len("SKILL.md")]
        elif href.endswith(".md"):              # rendered documentation page
            href = href[:-len(".md")] + ".html"
        return '<a href="%s">%s</a>' % (html.escape(href, quote=True), text)
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", link, s)
    return s


def md_to_html(md):
    lines = md.split("\n")
    out, i, n = [], 0, len(lines)
    while i < n:
        line = lines[i]
        # fenced code
        if line.startswith("```"):
            i += 1
            buf = []
            while i < n and not lines[i].startswith("```"):
                buf.append(html.escape(lines[i])); i += 1
            i += 1
            out.append("<pre><code>%s</code></pre>" % "\n".join(buf)); continue
        # table
        if line.strip().startswith("|") and i + 1 < n and re.match(r"^\s*\|[\s:|-]+\|\s*$", lines[i + 1]):
            header = [c.strip() for c in line.strip().strip("|").split("|")]
            i += 2
            rows = []
            while i < n and lines[i].strip().startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")]); i += 1
            th = "".join("<th>%s</th>" % _inline(c) for c in header)
            trs = "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % _inline(c) for c in r) for r in rows)
            out.append("<table><thead><tr>%s</tr></thead><tbody>%s</tbody></table>" % (th, trs)); continue
        # heading
        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            lvl = len(m.group(1))
            out.append("<h%d>%s</h%d>" % (lvl, _inline(m.group(2)), lvl)); i += 1; continue
        # hr
        if re.match(r"^\s*(-{3,}|\*{3,})\s*$", line):
            out.append("<hr>"); i += 1; continue
        # blockquote
        if line.startswith(">"):
            buf = []
            while i < n and lines[i].startswith(">"):
                buf.append(_inline(lines[i].lstrip(">").strip())); i += 1
            out.append("<blockquote>%s</blockquote>" % "<br>".join(buf)); continue
        # unordered list
        if re.match(r"^\s*[-*]\s+", line):
            buf = []
            while i < n and re.match(r"^\s*[-*]\s+", lines[i]):
                buf.append("<li>%s</li>" % _inline(re.sub(r"^\s*[-*]\s+", "", lines[i]))); i += 1
            out.append("<ul>%s</ul>" % "".join(buf)); continue
        # ordered list
        if re.match(r"^\s*\d+\.\s+", line):
            buf = []
            while i < n and re.match(r"^\s*\d+\.\s+", lines[i]):
                buf.append("<li>%s</li>" % _inline(re.sub(r"^\s*\d+\.\s+", "", lines[i]))); i += 1
            out.append("<ol>%s</ol>" % "".join(buf)); continue
        # blank
        if not line.strip():
            i += 1; continue
        # paragraph (gather until blank/structural)
        buf = [line]
        i += 1
        while i < n and lines[i].strip() and not re.match(r"^(#{1,6}\s|\s*[-*]\s|\s*\d+\.\s|>|\||```|\s*-{3,}\s*$)", lines[i]):
            buf.append(lines[i]); i += 1
        out.append("<p>%s</p>" % _inline(" ".join(buf)))
    return "\n".join(out)


def parse_fm(text):
    fm, body = {}, text
    if text.startswith("---\n"):
        _, fmtext, body = text.split("---\n", 2)
        for ln in fmtext.splitlines():
            mm = re.match(r'^(\w+):\s*"?(.*?)"?\s*$', ln)
            if mm:
                fm[mm.group(1)] = mm.group(2)
    return fm, body.strip()


def classify(rel):
    if rel == "00-framework":
        return "Framework"
    if rel.startswith("strategic-missions"):
        return "Strategic mission"
    if rel.startswith("cross-cutting-archetypes"):
        return "Archetype"
    if rel.startswith("_catalogs/"):
        return "Catalog: " + rel.split("/")[1]
    p = rel.split("/")
    if re.match(r"^\d\d-", p[0]):
        if len(p) == 1:
            return "Operating system"
        return {"roles": "Sector role", "robots": "Sector robot",
                "autonomous": "Sector machine"}.get(p[1], "Sector")
    return "Other"


def os_of(rel):
    m = re.match(r"^(\d\d)-", rel)
    return m.group(1) if m else ""


# ---------------------------------------------------------------------------
# Assets
# ---------------------------------------------------------------------------
CSS = """
:root{--bg:#0f1115;--panel:#171a21;--ink:#e8eaed;--muted:#9aa3b2;--line:#2a2f3a;--accent:#6ea8fe;--chip:#222734}
@media (prefers-color-scheme: light){:root{--bg:#fbfbfa;--panel:#fff;--ink:#1a1a1a;--muted:#666;--line:#e3e3e0;--accent:#1f6feb;--chip:#f1f1ee}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
a{color:var(--accent);text-decoration:none}a:hover{text-decoration:underline}
.wrap{max-width:980px;margin:0 auto;padding:24px 20px 80px}
header.site{position:sticky;top:0;background:var(--bg);border-bottom:1px solid var(--line);padding:10px 20px;display:flex;gap:14px;align-items:baseline;flex-wrap:wrap}
header.site .brand{font-weight:600;font-size:16px}
header.site .muted{color:var(--muted);font-size:13px}
input,select{background:var(--panel);color:var(--ink);border:1px solid var(--line);border-radius:8px;padding:8px 10px;font-size:14px}
input#q{flex:1;min-width:200px}
.controls{display:flex;gap:8px;flex-wrap:wrap;margin:18px 0}
.count{color:var(--muted);font-size:13px;margin:8px 0}
ul.results{list-style:none;padding:0;margin:0}
ul.results li{border:1px solid var(--line);border-radius:10px;padding:10px 12px;margin-bottom:8px;background:var(--panel)}
ul.results li .cat{display:inline-block;font-size:11px;color:var(--muted);background:var(--chip);border:1px solid var(--line);border-radius:999px;padding:1px 9px;margin-right:8px;vertical-align:middle}
ul.results li .name{font-weight:600}
ul.results li .desc{color:var(--muted);font-size:13px;margin-top:3px}
article{max-width:820px}
article h1{font-size:24px;margin:.2em 0}
article h2{font-size:19px;margin-top:1.6em;border-bottom:1px solid var(--line);padding-bottom:4px}
article h3{font-size:16px}
article code{background:var(--chip);border:1px solid var(--line);border-radius:5px;padding:1px 5px;font-size:.9em}
article pre{background:var(--panel);border:1px solid var(--line);border-radius:8px;padding:12px;overflow:auto}
article pre code{background:none;border:none;padding:0}
article table{border-collapse:collapse;width:100%;margin:1em 0;font-size:14px;display:block;overflow:auto}
article th,article td{border:1px solid var(--line);padding:6px 9px;text-align:left;vertical-align:top}
article th{background:var(--chip)}
article blockquote{border-left:3px solid var(--accent);margin:1em 0;padding:6px 12px;background:var(--panel);color:var(--muted);border-radius:0 8px 8px 0}
.crumb{color:var(--muted);font-size:13px;margin-bottom:10px}
.foot{color:var(--muted);font-size:12px;margin-top:40px;border-top:1px solid var(--line);padding-top:14px}
"""

APP_JS = """
(function(){
  var data = window.SKILLS || [];
  var q=document.getElementById('q'), cat=document.getElementById('cat'), os=document.getElementById('os');
  var list=document.getElementById('results'), count=document.getElementById('count');
  function opts(sel, vals){vals.forEach(function(v){var o=document.createElement('option');o.value=v;o.textContent=v;sel.appendChild(o);});}
  opts(cat, Array.from(new Set(data.map(function(d){return d.c;}))).sort());
  opts(os, Array.from(new Set(data.map(function(d){return d.o;}).filter(Boolean))).sort());
  function render(){
    var t=(q.value||'').toLowerCase(), c=cat.value, o=os.value;
    var rows=data.filter(function(d){
      if(c && d.c!==c) return false;
      if(o && d.o!==o) return false;
      if(t && (d.n+' '+d.d+' '+d.c).toLowerCase().indexOf(t)<0) return false;
      return true;
    });
    count.textContent=rows.length+' / '+data.length+' skills';
    list.innerHTML=rows.slice(0,600).map(function(d){
      return '<li><a href="'+d.u+'"><span class="cat">'+d.c+'</span><span class="name">'+d.n+'</span></a>'+
             '<div class="desc">'+d.d+'</div></li>';
    }).join('');
  }
  [q,cat,os].forEach(function(el){el.addEventListener('input',render);});
  render();
})();
"""


def page(title, body_html, prefix, crumb=""):
    return """<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>%s · CivStack</title><link rel="stylesheet" href="%sassets/style.css"></head>
<body><header class="site"><a class="brand" href="%sindex.html">CivStack</a>
<span class="muted">browsable skill library</span></header>
<div class="wrap">%s%s</div></body></html>""" % (
        html.escape(title), prefix, prefix,
        ('<div class="crumb">%s</div>' % crumb) if crumb else "", body_html)


def main():
    if os.path.isdir(SITE):
        try:
            shutil.rmtree(SITE)          # clean rebuild where the filesystem allows deletes
        except OSError:
            pass                          # otherwise overwrite in place (e.g. restricted mounts)
    os.makedirs(os.path.join(SITE, "assets"), exist_ok=True)
    open(os.path.join(SITE, "assets", "style.css"), "w").write(CSS)
    open(os.path.join(SITE, "assets", "app.js"), "w").write(APP_JS)

    index = []
    nskills = 0
    for dp, _, fs in os.walk(SKILLS):
        if "SKILL.md" not in fs:
            continue
        rel = os.path.relpath(dp, SKILLS)
        if rel.startswith("examples"):
            continue
        fm, body = parse_fm(open(os.path.join(dp, "SKILL.md")).read())
        name = fm.get("name", rel)
        desc = fm.get("description", "")
        cat = classify(rel)
        depth = len(rel.split("/"))
        prefix = "../" * (depth + 1)          # site/skills/<rel>/index.html -> site/
        crumb = '<a href="%sindex.html">Home</a> / %s / <code>skills/%s</code>' % (prefix, cat, rel)
        art = "<article><h1>%s</h1>%s<div class='foot'>Source: <code>skills/%s/SKILL.md</code></div></article>" % (
            html.escape(name), md_to_html(body), rel)
        outdir = os.path.join(SITE, "skills", rel)
        os.makedirs(outdir, exist_ok=True)
        open(os.path.join(outdir, "index.html"), "w").write(page(name, art, prefix, crumb))
        index.append({"n": name, "d": desc, "c": cat, "o": os_of(rel), "u": "skills/%s/" % rel})
        nskills += 1

    # docs pages
    docs_links = []
    if os.path.isdir(DOCS):
        os.makedirs(os.path.join(SITE, "docs"), exist_ok=True)
        for f in sorted(os.listdir(DOCS)):
            if not f.endswith(".md"):
                continue
            fm, body = parse_fm(open(os.path.join(DOCS, f)).read())
            title = f[:-3]
            art = "<article>%s</article>" % md_to_html(body)
            open(os.path.join(SITE, "docs", f[:-3] + ".html"), "w").write(page(title, art, "../"))
            docs_links.append('<a href="docs/%s.html">%s</a>' % (f[:-3], f[:-3]))

    # checklist pages
    checklist_links = []
    if os.path.isdir(CHECKLISTS):
        os.makedirs(os.path.join(SITE, "checklists"), exist_ok=True)
        for f in sorted(os.listdir(CHECKLISTS)):
            if not f.endswith(".md"):
                continue
            fm, body = parse_fm(open(os.path.join(CHECKLISTS, f)).read())
            title = f[:-3]
            art = "<article>%s</article>" % md_to_html(body)
            open(os.path.join(SITE, "checklists", f[:-3] + ".html"), "w").write(page(title, art, "../"))
            checklist_links.append('<a href="checklists/%s.html">%s</a>' % (f[:-3], f[:-3]))

    # standalone interactive HTML tools
    tool_links = []
    if os.path.isdir(TOOLS):
        os.makedirs(os.path.join(SITE, "tools"), exist_ok=True)
        for f in sorted(os.listdir(TOOLS)):
            if not f.endswith(".html"):
                continue
            shutil.copy2(os.path.join(TOOLS, f), os.path.join(SITE, "tools", f))
            tool_links.append('<a href="tools/%s">%s</a>' % (f, f[:-5]))

    # data.js (inlined catalog so file:// works without fetch)
    import json
    open(os.path.join(SITE, "data.js"), "w").write(
        "window.SKILLS=" + json.dumps(index, ensure_ascii=False) + ";")

    # home / search page
    home_body = """
<h1 style="font-size:26px">CivStack — browsable skill library</h1>
<p style="color:var(--muted)">%d skills across 23 operating systems and 12 strategic missions.
Search and filter below, or read the <strong>docs</strong>: %s.</p>
<p style="color:var(--muted)"><strong>Interactive tools:</strong> %s.<br><strong>Deployment checklists:</strong> %s.</p>
<div class="controls">
  <input id="q" type="search" placeholder="Search skills…" autofocus>
  <select id="cat"><option value="">All categories</option></select>
  <select id="os"><option value="">All operating systems</option></select>
</div>
<div class="count" id="count"></div>
<ul class="results" id="results"></ul>
<script src="data.js"></script><script src="assets/app.js"></script>
""" % (nskills, " · ".join(docs_links) or "(none)",
       " · ".join(tool_links) or "(none)", " · ".join(checklist_links) or "(none)")
    open(os.path.join(SITE, "index.html"), "w").write(page("Home", home_body, ""))

    print("Built site/ : %d skill pages + %d docs + %d checklists + %d tools." %
          (nskills, len(docs_links), len(checklist_links), len(tool_links)))
    print("Open site/index.html, or: python3 -m http.server -d site 8000")


if __name__ == "__main__":
    main()
