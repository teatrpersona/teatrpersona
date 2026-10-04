(async()=>{
const R=document.body.dataset.root||'',J=f=>fetch(R+'data/'+f+'.json').then(r=>r.json());
const img=(s,a)=>`<img src="${R}${s}" alt="${a}" loading="lazy" onerror="this.onerror=null;this.src='${R}assets/img/placeholder.svg'">`;
const S=await J('site'),page=document.body.dataset.page;
const mail=e=>`<a href="mailto:${e}">${e}</a>`;
document.body.insertAdjacentHTML('afterbegin',`<header><div class="wrap"><a class="logo" href="${R}">TEATR <b>PERSONA</b></a><button id="burger" aria-label="Menu">☰</button><nav id="nav">${S.nav.map(n=>`<a href="${R}${n.h}" class="${n.cta?'cta ':''}${n.id==page?'on':''}">${n.t}</a>`).join('')}</nav></div></header>`);
document.body.insertAdjacentHTML('beforeend',`<footer><div class="wrap"><h3>TEATR PERSONA</h3><p>${S.slogan}</p><p>${mail(S.email)} · ${mail(S.ticketEmail)}</p><p>${S.social.map(s=>`<a href="${s.url}" target="_blank" rel="noopener">${s.name}</a>`).join('')}</p><p>© ${new Date().getFullYear()} Teatr Persona</p></div></footer>`);
document.getElementById('burger').onclick=()=>document.getElementById('nav').classList.toggle('open');
document.querySelectorAll('[data-mail]').forEach(e=>e.innerHTML=mail(S[e.dataset.mail]));
const empty='<p>Wkrótce.</p>';
const T={
news:(d,e)=>d.slice(0,+e.dataset.limit||99).map(n=>`<article class="news reveal">${img(n.image,n.title)}<div>${n.date?`<small>${n.date}</small>`:''}<h3>${n.title}</h3><p>${n.text}</p></div></article>`).join('')||empty,
team:d=>`<div class="grid">${d.map(p=>`<div class="card reveal">${img(p.photo,p.name)}<div><h3>${p.name}</h3><p>${p.role}</p></div></div>`).join('')}</div>`,
projects:d=>`<div class="grid">${d.map(p=>`<a class="card reveal" href="${R}projekty/${p.slug}/">${img(p.poster,p.title)}<div><h3>${p.title}</h3><p>${p.short}</p></div></a>`).join('')}</div>`,
partners:d=>d.length?`<div class="grid">${d.map(p=>`<a class="card" href="${p.url}" target="_blank" rel="noopener">${img(p.logo,p.name)}<div><h3>${p.name}</h3></div></a>`).join('')}</div>`:empty,
classes:(_,e,s)=>`<h3>${s.classes.title}</h3><p>${s.classes.when}<br>${s.classes.where}</p>`,
tickets:t=>`<div class="banner"><h3>${t.title}</h3><p>${t.text}</p></div><ol>${t.steps.map(s=>`<li>${s}</li>`).join('')}</ol>${t.fundUrl?`<a class="btn" href="${t.fundUrl}" target="_blank" rel="noopener">Wesprzyj zbiórkę</a>`:''}<a class="btn o" href="mailto:${S.ticketEmail}">Zdobądź bilet</a>`};
for(const e of document.querySelectorAll('[data-render]')){const n=e.dataset.render;
try{e.innerHTML=T[n](n=='classes'?null:await J(n),e,S)}catch(x){console.error(n,x)}}
const io=new IntersectionObserver(a=>a.forEach(i=>i.isIntersecting&&i.target.classList.add('in')));
document.querySelectorAll('.reveal').forEach(e=>io.observe(e));
})();
