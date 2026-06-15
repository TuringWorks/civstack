# Finishing the git repo locally

All project files are already here on disk. The git history was prepared for you as a
single-file **bundle** (`civstack.bundle`) because this volume blocked my sandbox from
finalizing a `.git` directory in place. Pick one of the options below — each takes one step.

## Option A — clone the bundle (recommended, gives you full history)

```bash
cd /Volumes/fast01/source/other/git
git clone civstack/civstack.bundle civstack-repo
cd civstack-repo
git log --oneline        # → one commit on branch "main"
```

Then point it at a remote and push:

```bash
git remote add origin git@github.com:<you>/civstack.git
git push -u origin main
```

You can delete `civstack/civstack.bundle` afterward, and replace the original
`civstack/` working folder with `civstack-repo/` if you prefer a clean repo.

## Option B — initialize in place

There may be a partial `.git/` folder in `civstack/` that my sandbox could not remove.
On your Mac you have full permissions, so:

```bash
cd /Volumes/fast01/source/other/git/civstack
rm -rf .git
git init -b main
git add -A
git commit -m "CivStack: 248 agent skills mapping a nation's operating systems to human, AI, and robot roles"
```

## Notes

- The committed history in the bundle is identical to the files on disk (254 tracked files).
- `civstack.bundle` and this `SETUP-GIT.md` can both be deleted once you have a working repo.
