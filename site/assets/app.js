
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
