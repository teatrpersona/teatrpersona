import json,os
def page(path,pid,title,desc,body):
    d=path.count('/');R='../'*d
    html=f'''<!doctype html><html lang="pl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title} – Teatr Persona</title><meta name="description" content="{desc}"><meta property="og:title" content="{title} – Teatr Persona"><meta property="og:description" content="{desc}"><meta property="og:image" content="{R}assets/img/og.jpg"><link rel="icon" href="{R}assets/img/favicon.svg"><link rel="stylesheet" href="{R}assets/css/style.css"></head><body data-root="{R}" data-page="{pid}"><main>{body}</main><noscript>Włącz JavaScript, aby zobaczyć menu i treści.</noscript><script src="{R}assets/js/main.js" defer></script></body></html>'''.replace('@R',R)
    os.makedirs(os.path.dirname(path) or '.',exist_ok=True);open(path,'w',encoding='utf-8').write(html)
S=lambda h,x:f'<section><div class="wrap reveal"><h2>{h}</h2>{x}</div></section>'
T=lambda h:f'<div class="wrap page-title"><h1>{h}</h1></div>'
R_=lambda n,x='':f'<div data-render="{n}" {x}></div>'
page('index.html','home','Strona główna','Teatr Persona – niezależny teatr z Katowic.',
 '<div class="hero"><div class="wrap"><h1>Teatr<br>Persona</h1><p>Rozszczepienie Hamleta na dziewięć osobowości, pan rozumie</p><a class="btn" href="@Rbilety/">Bilety</a><a class="btn o" href="@Rprojekty/">Nasze projekty</a></div></div>'
 +S('Aktualności',R_('news','data-limit="3"'))+S('Nasze zajęcia',R_('classes'))+S('Nasze projekty',R_('projects'))+S('Nasi partnerzy',R_('partners')))
page('o-nas/index.html','about','O nas','Kim jesteśmy i czym zajmuje się Teatr Persona.',
 T('O nas')+S('Kim jesteśmy?','<p>[Do uzupełnienia: kilka zdań o teatrze.]</p>')+S('Nasz cel','<p>[Do uzupełnienia.]</p>')+S('Nasze zajęcia',R_('classes')))
page('zespol/index.html','team','Zespół','Poznaj zespół Teatru Persona.',T('Zespół')+S('Poznaj nasz zespół',R_('team')))
page('aktualnosci/index.html','news','Aktualności','Najnowsze wieści z Teatru Persona.',T('Aktualności')+S('Co nowego',R_('news')))
page('bilety/index.html','tickets','Bilety','Jak zdobyć bilet na spektakl Teatru Persona.',T('Bilety')+S('Jak zdobyć bilety?',R_('tickets')))
page('projekty/index.html','projects','Nasze projekty','Spektakle i projekty Teatru Persona.',T('Nasze projekty')+S('Spektakle',R_('projects')))
page('partnerzy/index.html','partners','Partnerzy','Partnerzy Teatru Persona.',T('Partnerzy')+S('Nasi partnerzy',R_('partners')))
page('kontakt/index.html','contact','Kontakt','Skontaktuj się z Teatrem Persona.',T('Kontakt')+S('Napisz do nas',
 '<div class="two"><div><h3>Kontakt główny</h3><p data-mail="email"></p><h3>Dystrybucja biletów</h3><p data-mail="ticketEmail"></p><h3>Gdzie ćwiczymy</h3><p>Katowice, ul. Kopernika 14</p><a class="btn o" target="_blank" rel="noopener" href="https://www.openstreetmap.org/search?query=Kopernika%2014%20Katowice">OpenStreetMap</a><a class="btn o" target="_blank" rel="noopener" href="https://www.google.com/maps/search/?api=1&query=Kopernika+14+Katowice">Google Maps</a></div>'
 '<form action="https://formspree.io/f/YOUR_FORM_ID" method="POST"><label>Imię i nazwisko<input name="name" required></label><label>E-mail<input type="email" name="email" required></label><label>Wiadomość<textarea name="message" rows="6" required></textarea></label><button class="btn" type="submit">Wyślij</button></form></div>'))
page('404.html','','Nie znaleziono','Strona nie istnieje.','<div class="wrap page-title"><h1>404</h1><p>Tej sceny nie ma. <a href="/">Wróć na start</a>.</p></div>')
for p in json.load(open('data/projects.json',encoding='utf-8')):
    page(f"projekty/{p['slug']}/index.html",'projects',p['title'],p['short'],
     f'''<section><div class="wrap two"><img src="@R{p['poster']}" alt="Plakat: {p['title']}" onerror="this.onerror=null;this.src='@Rassets/img/placeholder.svg'"><div><h1>{p['title']}</h1><p>{p['long']}</p><a class="btn" href="@Rbilety/">Bilety</a><a class="btn o" href="@Rprojekty/">Wszystkie projekty</a></div></div></section>''')
