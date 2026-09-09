#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generator static — Acoperișul Solid / acoperisulsolid.ro
Rulează:  python3 build.py
"""
import os, json, hashlib

ROOT = os.path.dirname(os.path.abspath(__file__))

def _ver(rel):
    with open(os.path.join(ROOT, rel), "rb") as f:
        return hashlib.md5(f.read()).hexdigest()[:8]

CSS_V = _ver("assets/style.css")
JS_V  = _ver("assets/script.js")

B = {
    "name":     "Acoperișul Solid",
    "tagline":  "Montaj · Reparații · Mansardări",
    "domain":   "https://acoperisulsolid.ro",
    "tel_disp": "0756 419 558",
    "tel_raw":  "+40756419558",
    "wa":       "40756419558",
    "rating":   "4,8",
    "reviews":  54,
    "years":    10,
    "projects": 500,
}
WA_TXT = "Bun%C4%83%20ziua%21%20A%C8%99%20dori%20o%20ofert%C4%83%20pentru%20lucr%C4%83ri%20la%20acoperi%C8%99."
WA_LINK = "https://wa.me/%s?text=%s" % (B["wa"], WA_TXT)
TEL = "tel:" + B["tel_raw"]

WEB3FORMS_KEY = "3bb80e3f-b3a1-49d3-bf60-6480faf41f2c"

# mărci de materiale cu care se lucrează, afișate ca "parteneri" pe homepage
BRANDS = ["Bilka", "Lindab", "Velux"]  # TODO: al 4-lea brand — de confirmat cu clientul

REGIONS = ["Iași", "Suceava", "Vaslui", "Neamț", "Bacău"]

# localitati reale pe judet, pentru a arata acoperire pe toata raza judetului, nu doar resedinta
JUDETE_LOC = {
    "Iași":    ["Iași", "Pașcani", "Hârlău", "Târgu Frumos", "Podu Iloaiei", "Belcești"],
    "Suceava": ["Suceava", "Fălticeni", "Rădăuți", "Câmpulung Moldovenesc", "Gura Humorului", "Vatra Dornei", "Siret"],
    "Vaslui":  ["Vaslui", "Bârlad", "Huși", "Negrești"],
    "Neamț":   ["Piatra Neamț", "Roman", "Târgu Neamț", "Bicaz"],
    "Bacău":   ["Bacău", "Onești", "Moinești", "Comănești", "Buhuși"],
}

NAV = [
    ("servicii",            "/servicii/",            "Servicii"),
    ("lucrari",             "/lucrari/",             "Lucrări"),
    ("calculator-pret",     "/calculator-pret/",     "Calculator preț"),
    ("acoperire",           "/zona-acoperire/",       "Unde lucrăm"),
    ("intrebari-frecvente", "/intrebari-frecvente/", "Întrebări"),
    ("despre",              "/despre/",              "Despre noi"),
    ("contact",             "/contact/",             "Contact"),
]

SERVICES = [
    dict(k="acoperis-nou", tag="Case noi", img="srv-acoperis-nou.jpg",
         t="Acoperiș complet la casă nouă",
         s="Preluăm casa la roșu și o predăm cu acoperișul închis, gata de iarnă.",
         d="Dimensionăm șarpanta pentru deschiderea reală și pentru încărcarea din zăpadă a zonei, apoi montăm straturile în ordinea corectă: astereală sau șipci, folie anticondens, contrașipci, învelitoare, tinichigerie. Închidem toate racordurile — coame, dolii, coșuri, lucarne — înainte să plecăm de pe șantier."),
    dict(k="inlocuire", tag="Cel mai cerut", img="srv-inlocuire-invelitoare.jpg",
         t="Înlocuire învelitoare",
         s="Scoatem învelitoarea veche și punem una nouă, cu toate straturile refăcute.",
         d="Demontăm învelitoarea uzată, verificăm fiecare căprior și fiecare pană, înlocuim ce e atacat de umezeală și refacem acoperișul complet. Vă spunem dinainte ce se poate găsi sub țiglă la o casă de 30–40 de ani și cât costă fiecare situație, ca să nu vă trezim cu un cost nou la jumătatea lucrării."),
    dict(k="reparatii", tag="Intervenții", img="srv-reparatii.jpg",
         t="Reparații și infiltrații",
         s="Găsim de unde intră apa, nu doar unde se vede pata.",
         d="Apa intră într-un loc și iese în altul, la câțiva metri distanță. Urmărim traseul până la sursă și reparăm cauza: țiglă spartă sau deplasată, coamă desfăcută, dolie ruginită, șorț lipsă la coș, folie ruptă. Pentru infiltrații active ne organizăm cu prioritate."),
    dict(k="sarpante", tag="Structură", img="sarpanta-lemn-cladire-noua.jpg",
         t="Șarpante și dulgherie",
         s="Construim și consolidăm structura de lemn a acoperișului.",
         d="Executăm șarpante noi și consolidăm structuri existente. Lemnul se tratează ignifug și antifungic înainte de urcare, iar îmbinările se fac astfel încât structura să lucreze ca un tot. La casele vechi înlocuim punctual elementele atacate, fără să demontăm tot ce încă e sănătos."),
    dict(k="mansardari", tag="Spațiu în plus", img="srv-mansardari.jpg",
         t="Mansardări",
         s="Transformăm podul în cameră locuibilă, izolată ca să nu condenseze.",
         d="Închidem podul cu structură, izolație de grosime corectă și barieră de vapori montată continuu, cu suprapuneri lipite. Majoritatea mansardelor reci sau cu mucegai nu au prea puțină vată, ci o barieră de vapori pusă neetanș — acolo insistăm cel mai mult. Montăm și ferestre de mansardă, cu toate șorțurile aferente."),
    dict(k="pluviale", tag="Pluvial", img="srv-jgheaburi.jpg",
         t="Jgheaburi și burlane",
         s="Sisteme pluviale dimensionate și montate cu panta corectă.",
         d="Calculăm jgheabul după suprafața reală a acoperișului și îl montăm cu panta necesară către burlan. Un sistem subdimensionat sau montat orizontal se revarsă la ploi puternice și udă fațada și fundația, chiar dacă la montaj arată impecabil."),
    dict(k="tinichigerie", tag="Detalii", img="srv-inlocuire-invelitoare.jpg",
         t="Tinichigerie și racorduri",
         s="Șorțuri, dolii, coame și racorduri la coșuri, executate pe loc.",
         d="Cele mai multe infiltrații nu vin din mijlocul acoperișului, ci din racorduri. Executăm tinichigeria la fața locului, croită pe forma reală a casei: șorțuri la coșuri și la calcane, dolii, pazii, glafuri. Aici se vede diferența între o echipă și un montaj făcut pe repede-înainte."),
    dict(k="acoperis-verde", tag="Ecologic", img="srv-acoperis-verde.jpg",
         t="Acoperișuri verzi",
         s="Sistem complet pentru acoperiș vegetal, de la hidroizolație la substrat.",
         d="Montăm sistemul complet pentru acoperiș vegetal extensiv: hidroizolație antiradiculară, strat drenant, filtru, substrat și vegetație. Verificăm întâi dacă structura suportă încărcarea suplimentară în stare saturată, pentru că acolo se greșește cel mai des."),
    dict(k="hidroizolatii", tag="Terase", img="srv-reparatii.jpg",
         t="Hidroizolații și terase",
         s="Refacem hidroizolația teraselor și acoperișurilor plate.",
         d="Curățăm suportul, refacem panta unde apa băltește și montăm membrana cu suprapuneri sudate corect. Tratăm separat punctele unde cedează în practică o terasă: gurile de scurgere, aticele și racordurile la pereți."),
]

WORKS = [
    ("acoperis-tigla-metalica-antracit.jpg", "Înlocuire", "Învelitoare nouă din țiglă metalică antracit", "Casă individuală"),
    ("acoperis-tigla-metalica-rosie.jpg",    "Montaj",    "Structură și folie pregătite, cu fereastră de mansardă integrată", "Casă la curte"),
    ("sarpanta-lemn-casa-noua.jpg",          "Dulgherie", "Șarpantă nouă executată la casă în construcție", "Construcție nouă"),
    ("acoperis-casa-noua-antracit.jpg",      "Acoperiș nou","Acoperiș închis complet la casă cu mansardă", "Construcție nouă"),
    ("acoperis-finalizat-casa-parter.jpg",   "Finalizat", "Acoperiș pe casă parter, cu streașină lambrisată", "Locuință parter"),
    ("acoperis-visiniu-tigla-metalica.jpg",  "Finalizat", "Țiglă metalică antracit, cu racord la coș de cărămidă", "jud. Iași"),
    ("montaj-tigla-antracit-lucru.jpg",      "În lucru",  "Montaj țiglă metalică antracit, casă în construcție alăturată", "jud. Iași"),
    ("acoperis-visiniu-patru-ape.jpg",       "În lucru",  "Acoperiș în patru ape, structură pregătită pentru țiglă", "jud. Bacău"),
    ("acoperis-gri-panorama-sat.jpg",        "Finalizat", "Acoperiș gri, vedere panoramică spre sat", "jud. Suceava"),
    ("detaliu-montaj-insurubare.jpg",        "Detaliu",   "Fixarea țiglei metalice, prindere pe toată suprafața", "Detaliu montaj"),
    ("sarpanta-casa-montaj.jpg",             "Structură", "Șarpantă nouă ridicată pe o casă în construcție", "jud. Neamț"),
    ("structura-lemn-pergola-terasa.jpg",    "Dulgherie", "Structură din lemn masiv pentru o terasă acoperită", "Dulgherie"),
]

REVIEWS = [
    ("Constantin B.", "jud. Iași",     "echipa-1.mp4",                          "Au venit când au spus și au închis acoperișul în cinci zile. Prețul din ofertă a fost prețul final, fără discuții pe parcurs."),
    ("Elena R.",      "jud. Suceava",  "echipa-2.mp4",                          "Aveam tablă veche care ruginise. Au pus țiglă metalică și au refăcut și jgheaburile. Curtea a rămas curată după ei."),
    ("Marius D.",     "jud. Vaslui",   "acoperis-finalizat-casa-parter.jpg",    "De doi ani aveam o pată pe tavan și nimeni nu găsea cauza. Au urcat, au urmărit apa și au reparat șorțul de la coș."),
    ("Ioana P.",      "jud. Neamț",    "montaj-fereastra-mansarda.jpg",         "Mansarda nu mai are condens iarna. Ne-au explicat exact de ce trebuia bariera de vapori pusă altfel decât era."),
    ("Vasile M.",     "jud. Bacău",    "acoperis-tigla-metalica-rosie.jpg",     "Furtuna îmi luase câteva plăci. Au venit în două zile și au rezolvat, fără să-mi ceară să schimb tot acoperișul."),
    ("Andrei T.",     "jud. Iași",     "sarpanta-lemn-casa-noua.jpg",           "Șarpanta era atacată pe o parte. Au schimbat doar ce trebuia schimbat, nu tot, și mi-au arătat fiecare element."),
]

FAQ = [
    ("În ce zone lucrați exact?",
     ["Acoperim integral județele Iași, Suceava, Vaslui, Neamț și Bacău — nu doar reședințele de județ, ci toate orașele, comunele și satele din raza lor.",
      "Ne spuneți unde este casa și vă confirmăm în aceeași zi dacă putem prelua lucrarea și în ce interval."]),
    ("Cât costă un acoperiș?",
     ["Depinde de suprafața reală, de pantă, de învelitoarea aleasă și de starea șarpantei. Pe pagina de calculator preț ne puteți trimite aceste detalii pe email și vă răspundem cu un interval orientativ.",
      "Prețul exact vine după măsurătoare. O ofertă dată doar pe telefon, fără măsurători, iese aproape întotdeauna prea mică și crește pe parcurs."]),
    ("De ce suprafața acoperișului e mai mare decât a casei?",
     ["Pentru că un acoperiș este o suprafață înclinată, plus streașina care depășește pereții cu 40–80 cm de jur împrejur.",
      "La o casă obișnuită diferența este de aproximativ o treime față de amprenta la sol. La un pod înalt poate ajunge la jumătate."]),
    ("Cât durează lucrarea?",
     ["O înlocuire de învelitoare la o casă obișnuită durează între trei și șapte zile lucrătoare. Un acoperiș complet la o casă nouă, cu șarpantă, între una și două săptămâni. O reparație punctuală se rezolvă de obicei într-o zi.",
      "Vă dăm un termen în ofertă și vă anunțăm din timp dacă vremea ne obligă să îl decalăm."]),
    ("Ce garanție oferiți?",
     ["Garanție scrisă la manoperă pentru toate lucrările executate de echipele noastre. Garanția învelitorii vine de la producătorul ales, iar un montaj corect este chiar condiția ca acea garanție să rămână valabilă."]),
    ("Ce se întâmplă dacă apar surprize după demontare?",
     ["La casele vechi, starea reală a lemnului se vede abia după ce se scoate învelitoarea. Vă spunem de la început ce ar putea apărea și cât costă fiecare situație.",
      "Dacă găsim ceva ce nu era în deviz, oprim, vă sunăm, vă arătăm cu poze și continuăm doar după ce sunteți de acord."]),
    ("Se poate lucra iarna?",
     ["Pentru reparații și intervenții de urgență, da. Înlocuirile mari le programăm în sezon, pentru că acoperișul stă desfăcut o parte din timp și nu lăsăm casa descoperită pe ninsoare."]),
    ("Cumpăr eu materialele sau le aduceți voi?",
     ["Cum preferați. Vă putem calcula necesarul exact ca să cumpărați direct de la furnizor, sau vă aducem noi materialele în ofertă.",
      "În ambele cazuri vedeți separat cât înseamnă materialele și cât înseamnă manopera."]),
    ("Cum vă contactez cel mai rapid?",
     ["Pe WhatsApp. Trimiteți două-trei poze cu acoperișul și vă spunem din prima ce credem că are și în ce interval de preț se încadrează.",
      "Sau ne sunați direct la " + B["tel_disp"] + "."]),
    ("Strângeți după voi?",
     ["Da. Molozul, învelitoarea veche și cuiele pleacă odată cu noi. Curtea rămâne cum a fost, nu ca după un șantier."]),
]

LOGO = ('<svg viewBox="0 0 36 36" aria-hidden="true">'
        '<rect width="36" height="36" rx="9" fill="#12261E"/>'
        '<path d="M6 19.5 L18 9 L30 19.5" stroke="#C4562A" stroke-width="3" '
        'stroke-linecap="round" stroke-linejoin="round" fill="none"/>'
        '<path d="M10 21.5c1.6 0 1.6 2 3.2 2s1.6-2 3.2-2 1.6 2 3.2 2 1.6-2 3.2-2 1.6 2 3.2 2" '
        'stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" fill="none"/>'
        '<path d="M10 26.5c1.6 0 1.6 2 3.2 2s1.6-2 3.2-2 1.6 2 3.2 2 1.6-2 3.2-2 1.6 2 3.2 2" '
        'stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" fill="none" opacity=".55"/></svg>')

def biz_ld():
    return {
        "@context": "https://schema.org",
        "@type": "RoofingContractor",
        "@id": B["domain"] + "/#business",
        "name": B["name"],
        "description": "Montaj, înlocuire și reparații acoperișuri, șarpante, mansardări, jgheaburi și hidroizolații, în județele Iași, Suceava, Vaslui, Neamț și Bacău.",
        "url": B["domain"] + "/",
        "telephone": B["tel_raw"],
        "image": B["domain"] + "/images/acoperis-tigla-metalica-antracit.jpg",
        "logo": B["domain"] + "/favicon.svg",
        "priceRange": "$$",
        "address": {"@type": "PostalAddress", "addressCountry": "RO", "addressLocality": "România"},
        "areaServed": [{"@type": "AdministrativeArea", "name": "Iași"}, {"@type": "AdministrativeArea", "name": "Suceava"}, {"@type": "AdministrativeArea", "name": "Vaslui"}, {"@type": "AdministrativeArea", "name": "Neamț"}, {"@type": "AdministrativeArea", "name": "Bacău"}],
        "openingHoursSpecification": {
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
            "opens": "07:00", "closes": "21:00"},
        "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.8",
                            "reviewCount": str(B["reviews"]), "bestRating": "5"},
        "contactPoint": {"@type": "ContactPoint", "telephone": B["tel_raw"],
                         "contactType": "customer service", "areaServed": "RO",
                         "availableLanguage": "Romanian"},
    }


def crumb_ld(path, label):
    items = [{"@type": "ListItem", "position": 1, "name": "Acasă", "item": B["domain"] + "/"}]
    if path != "/":
        items.append({"@type": "ListItem", "position": 2, "name": label, "item": B["domain"] + path})
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items}


def head(title, desc, path, og="acoperis-tigla-metalica-antracit.jpg", label="", extra=None, noindex=False):
    url = B["domain"] + path
    lds = [biz_ld(), crumb_ld(path, label)]
    if extra:
        lds.append(extra)
    blocks = "".join('<script type="application/ld+json">%s</script>'
                     % json.dumps(x, ensure_ascii=False, separators=(",", ":")) for x in lds)
    robots = "noindex, follow" if noindex else "index, follow, max-image-preview:large, max-snippet:-1"
    return """<!DOCTYPE html>
<html lang="ro">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%s</title>
<meta name="description" content="%s">
<link rel="canonical" href="%s">
<meta name="robots" content="%s">
<meta name="theme-color" content="#12261E">
<meta name="author" content="%s">
<meta name="geo.region" content="RO">
<meta property="og:type" content="website">
<meta property="og:locale" content="ro_RO">
<meta property="og:site_name" content="%s">
<meta property="og:title" content="%s">
<meta property="og:description" content="%s">
<meta property="og:url" content="%s">
<meta property="og:image" content="%s/images/%s">
<meta property="og:image:width" content="1600">
<meta property="og:image:height" content="1200">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="%s">
<meta name="twitter:description" content="%s">
<meta name="twitter:image" content="%s/images/%s">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/favicon.svg">
<link rel="manifest" href="/site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Figtree:wght@400;500;600;700&family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/style.css?v=%s">
%s
</head>
<body>""" % (title, desc, url, robots, B["name"], B["name"], title, desc, url, B["domain"], og,
             title, desc, B["domain"], og, CSS_V, blocks)


def header(active=""):
    nav = "".join('<a href="%s"%s>%s</a>' % (u, ' class="on"' if k == active else "", t)
                  for k, u, t in NAV)
    mnav = "".join('<a href="%s">%s</a>' % (u, t) for k, u, t in NAV)
    return """
<div class="topbar"><div class="wrap">
  <span>Lucrăm în Iași, Suceava, Vaslui, Neamț și Bacău · <b>Deplasare și deviz gratuit</b></span>
  <span class="tb-r"><span>Program 07:00 – 21:00</span>
  <span><span class="tb-star">★★★★★</span> %s din %d de recenzii</span></span>
</div></div>

<header class="hdr">
  <div class="wrap">
    <a class="brand" href="/" aria-label="%s — pagina principală">%s
      <span class="brand-t"><b>%s</b><span>%s</span></span></a>
    <nav class="nav" aria-label="Navigare principală">%s</nav>
    <div class="hdr-cta">
      <a class="hdr-tel" href="%s"><span>Sunați-ne</span><b>%s</b></a>
      <a class="btn btn-p btn-sm" href="/calculator-pret/">Cere ofertă</a>
      <button class="burger" aria-label="Deschideți meniul" aria-expanded="false" aria-controls="mnav"><i></i><i></i><i></i></button>
    </div>
  </div>
  <nav class="mnav" id="mnav" aria-label="Meniu mobil"><div class="wrap">%s
    <div class="mnav-cta">
      <a class="btn btn-d" href="%s">Sunați: %s</a>
      <a class="btn btn-wa" href="%s" target="_blank" rel="noopener">Scrieți pe WhatsApp</a>
    </div></div></nav>
</header>""" % (B["rating"], B["reviews"], B["name"], LOGO, B["name"], B["tagline"], nav,
                TEL, B["tel_disp"], mnav, TEL, B["tel_disp"], WA_LINK)


def form(sid, title, sub, compact=False):
    extra = ""
    if not compact:
        opts = "".join("<option>%s</option>" % s["t"] for s in SERVICES)
        extra = """
      <div class="field"><label for="lu%s">Ce lucrare vă interesează</label>
        <select id="lu%s" name="lucrare"><option value="">Alegeți din listă</option>%s<option>Altă lucrare</option></select></div>
      <div class="field"><label for="de%s">Detalii (opțional)</label>
        <textarea id="de%s" name="detalii" placeholder="Suprafață aproximativă, tip de învelitoare, ce problemă aveți."></textarea></div>""" % (sid, sid, opts, sid, sid)
    return """<div class="cta-f">
  <h3>%s</h3><p>%s</p>
  <form class="ef" data-ef action="https://api.web3forms.com/submit" method="POST" novalidate>
    <input type="hidden" name="access_key" value="%s">
    <input type="hidden" name="subject" value="Cerere ofertă de pe acoperisulsolid.ro">
    <input type="hidden" name="from_name" value="Formular acoperisulsolid.ro">
    <input type="checkbox" name="botcheck" class="hp" tabindex="-1" autocomplete="off">
    <div class="field-2">
      <div class="field"><label for="nu%s">Nume *</label>
        <input id="nu%s" name="nume" type="text" autocomplete="name" required></div>
      <div class="field"><label for="te%s">Telefon *</label>
        <input id="te%s" name="telefon" type="tel" autocomplete="tel" required></div>
    </div>
    <div class="field-2">
      <div class="field"><label for="em%s">Email *</label>
        <input id="em%s" name="email" type="email" autocomplete="email" required></div>
      <div class="field"><label for="or%s">Localitate</label>
        <input id="or%s" name="oras" type="text" autocomplete="address-level2"></div>
    </div>
    %s
    <p class="f-msg" role="alert"></p>
    <button class="btn btn-p btn-w" type="submit">Trimiteți solicitarea</button>
    <p class="f-hint">Vă răspundem pe email, de obicei în aceeași zi. Preferați telefonul? <a href="%s">Sunați acum</a>.</p>
  </form>
</div>""" % (title, sub, WEB3FORMS_KEY, sid, sid, sid, sid, sid, sid, sid, sid, extra, TEL)


def footer():
    svc = "".join('<li><a href="/servicii/#%s">%s</a></li>' % (s["k"], s["t"]) for s in SERVICES[:6])
    return """
<footer class="ftr">
  <div class="wrap">
    <div class="ftr-g">
      <div class="ftr-brand">
        <a class="brand" href="/">%s<span class="brand-t"><b>%s</b><span>%s</span></span></a>
        <p>Echipe de acoperișuri active în tot județul Iași, Suceava, Vaslui, Neamț și Bacău — orașe, comune și sate deopotrivă. Peste %d ani de experiență și %d+ de lucrări.</p>
        <a class="ftr-tel" href="%s">%s</a>
      </div>
      <div><h4>Servicii</h4><ul>%s</ul></div>
      <div><h4>Firma</h4><ul>
        <li><a href="/despre/">Despre noi</a></li>
        <li><a href="/lucrari/">Lucrări executate</a></li>
        <li><a href="/calculator-pret/">Calculator preț</a></li>
        <li><a href="/zona-acoperire/">Unde lucrăm</a></li>
        <li><a href="/intrebari-frecvente/">Întrebări frecvente</a></li>
        <li><a href="/contact/">Contact</a></li>
      </ul></div>
      <div><h4>Contact</h4><ul>
        <li><a href="%s">%s</a></li>
        <li><a href="%s" target="_blank" rel="noopener">Scrieți pe WhatsApp</a></li>
        <li>Luni – duminică, 07:00 – 21:00</li>
        <li>Iași · Suceava · Vaslui · Neamț · Bacău</li>
        <li><a href="https://anpc.ro/" target="_blank" rel="noopener nofollow">ANPC</a> · <a href="https://ec.europa.eu/consumers/odr/" target="_blank" rel="noopener nofollow">SOL</a></li>
      </ul></div>
    </div>
    <div class="ftr-bot">
      <span>© <span data-year></span> %s. Toate drepturile rezervate.</span>
      <span><span style="color:var(--gold)">★★★★★</span> %s din %d de recenzii</span>
    </div>
  </div>
</footer>

<div class="mbar">
  <a class="m-call" href="%s">Sunați acum</a>
  <a class="m-wa" href="%s" target="_blank" rel="noopener">WhatsApp</a>
</div>

<script src="/assets/script.js?v=%s" defer></script>
</body>
</html>""" % (LOGO, B["name"], B["tagline"], B["years"], B["projects"], TEL, B["tel_disp"], svc,
              TEL, B["tel_disp"], WA_LINK, B["name"], B["rating"], B["reviews"],
              TEL, WA_LINK, JS_V)


def phero(crumb, h1, lead):
    return """<section class="phero"><div class="wrap">
  <div class="crumb"><a href="/">Acasă</a> / %s</div>
  <h1>%s</h1><p>%s</p>
</div></section>""" % (crumb, h1, lead)


def stars():
    return '<span class="stars" aria-label="5 din 5 stele">★★★★★</span>'


def rev_card(name, judet, photo, text):
    if photo.endswith(".mp4"):
        media = ('<div class="rev-ph rev-ph-v"><video src="/videos/%s" poster="/images/acoperis-tigla-metalica-antracit.jpg" '
                 'controls playsinline preload="metadata" '
                 'aria-label="Echipa la lucru"></video></div>') % photo
    else:
        media = '<div class="rev-ph"><img src="/images/%s" alt="Lucrare la un client din %s" loading="lazy" width="400" height="260"></div>' % (photo, judet)
    return """<article class="rev-c">
  %s
  %s<p>%s</p>
  <div class="rev-who"><span class="rev-av" aria-hidden="true">%s</span>
    <span><b>%s</b><span>%s</span></span></div></article>""" % (media, stars(), text, name[0], name, judet)


def faq_block(items):
    out = []
    for i, (q, aa) in enumerate(items):
        ans = "".join("<p>%s</p>" % p for p in aa)
        cls = " on" if i == 0 else ""
        exp = "true" if i == 0 else "false"
        out.append('<div class="faq-i%s"><button class="faq-q" type="button" aria-expanded="%s">%s</button>'
                   '<div class="faq-a">%s</div></div>' % (cls, exp, q, ans))
    return '<div class="faq">%s</div>' % "".join(out)


FAQ_LD = {"@context": "https://schema.org", "@type": "FAQPage",
          "mainEntity": [{"@type": "Question", "name": q,
                          "acceptedAnswer": {"@type": "Answer", "text": " ".join(a)}} for q, a in FAQ]}


def partners_section():
    chips = "".join('<span class="brand-i">%s</span>' % b for b in BRANDS)
    return """<section class="sec" style="padding:40px 0 44px"><div class="wrap">
  <p class="kicker" style="justify-content:center;margin-bottom:24px">Lucrăm cu materiale de la</p>
  <div class="brands">%s</div>
</div></section>""" % chips


def cta_section():
    return """<section class="sec sec-stone"><div class="wrap"><div class="cta">
  <div>
    <span class="kicker">Următorul pas</span>
    <h2>Trimiteți două poze și primiți un răspuns azi</h2>
    <p style="font-size:1.02rem;margin-top:14px">Cel mai rapid mod de a afla unde stați: ne trimiteți pe WhatsApp două-trei poze cu acoperișul și vă spunem ce credem că are și în ce interval de preț se încadrează. Fără obligații.</p>
    <div class="hero-act" style="margin-top:24px">
      <a class="btn btn-wa" href="%s" target="_blank" rel="noopener">Scrieți pe WhatsApp</a>
      <a class="btn btn-o" href="%s">Sunați: %s</a>
    </div>
  </div>
  %s
</div></div></section>""" % (WA_LINK, TEL, B["tel_disp"], form("c", "Solicitare rapidă", "Lăsați numele și telefonul, restul discutăm la telefon.", compact=True))


# ------------------------------------------------------------------ pagini
def page_home():
    svc = "".join("""<article class="svc-c rv">
      <div class="svc-ph"><img src="/images/%s" alt="%s" loading="lazy" width="900" height="506">
        <span class="svc-tag">%s</span></div>
      <div class="svc-b"><h3>%s</h3><p>%s</p><a class="svc-more" href="/servicii/#%s">Detalii</a></div>
    </article>""" % (s["img"], s["t"], s["tag"], s["t"], s["s"], s["k"]) for s in SERVICES[:6])

    work = "".join("""<a class="work-c rv" href="/lucrari/">
      <img src="/images/%s" alt="%s" loading="lazy" width="900" height="600">
      <div class="work-o"><span>%s</span><h3>%s</h3></div></a>""" % (im, t, tag, t) for im, tag, t, _ in WORKS)

    steps = [
        ("Ne scrieți", "O poză și un rând pe WhatsApp sunt de ajuns ca să înțelegem despre ce vorbim."),
        ("Venim și măsurăm", "Ne deplasăm la fața locului, luăm măsurătorile reale și verificăm starea structurii."),
        ("Primiți devizul", "Pe etape, cu materialele și manopera separat, la preț final."),
        ("Executăm și predăm", "Lucrăm curat, strângem după noi și predăm cu garanție scrisă la manoperă."),
    ]
    proc = "".join("""<div class="proc-i"><span class="proc-n">%02d</span><h3>%s</h3><p>%s</p></div>"""
                   % (i + 1, t, d) for i, (t, d) in enumerate(steps))

    why = [
        ("Acoperire", "Toată România", "Echipele se deplasează oriunde în țară. Pentru lucrări mari ne cazăm în zonă pe durata execuției."),
        ("Transparent", "Deviz pe etape", "Vedeți separat structura, folia, învelitoarea și tinichigeria — nu o singură cifră pentru tot."),
        ("Scris", "Garanție la manoperă", "Dacă apare o problemă la lucrarea noastră, ne întoarcem și o remediem."),
        ("Gratuit", "Deplasare și măsurătoare", "Venim, măsurăm și vă dăm un preț real înainte să începem orice."),
        ("%d ani" % B["years"], "Experiență", "Peste %d de acoperișuri executate și %s din %d de recenzii." % (B["projects"], B["rating"], B["reviews"])),
        ("Fără surprize", "Prețul rămâne prețul", "Dacă găsim ceva neprevăzut, oprim și vă arătăm cu poze înainte să lucrăm ceva în plus."),
    ]
    why_h = "".join('<div class="why-i"><span class="why-k">%s</span><h3>%s</h3><p>%s</p></div>' % w for w in why)
    revs = "".join(rev_card(*r) for r in REVIEWS[:3])
    chips = "".join("<span>%s</span>" % c for c in REGIONS)

    return head(
        "Acoperișul Solid | Montaj și reparații acoperiș în Iași, Suceava, Vaslui, Neamț, Bacău",
        "Montaj acoperiș, înlocuire învelitoare, reparații, șarpante și mansardări în județele Iași, Suceava, Vaslui, Neamț și Bacău. Peste %d ani experiență, %d+ lucrări, garanție scrisă. Deviz gratuit pe WhatsApp." % (B["years"], B["projects"]),
        "/", extra=FAQ_LD) + header("") + """

<section class="hero"><div class="wrap"><div class="hero-g">
  <div>
    <span class="kicker">Iași · Suceava · Vaslui · Neamț · Bacău</span>
    <h1>Un acoperiș pus o dată, corect, pentru următorii treizeci de ani</h1>
    <p class="hero-lead">Montăm, înlocuim și reparăm acoperișuri în tot județul — orașe, comune și sate deopotrivă, nu doar reședințele de județ. Măsurăm gratuit, vă dăm un deviz pe etape cu preț final și predăm cu garanție scrisă la manoperă.</p>
    <div class="hero-act">
      <a class="btn btn-p" href="/calculator-pret/">Calculați prețul</a>
      <a class="btn btn-wa" href="%s" target="_blank" rel="noopener">Trimiteți o poză pe WhatsApp</a>
    </div>
    <p class="hero-tel">Sau sunați direct: <a href="%s">%s</a></p>
  </div>
  <div class="hero-ph">
    <img src="/images/acoperis-tigla-metalica-antracit.jpg" alt="Acoperiș din țiglă metalică antracit finalizat de echipa Acoperișul Solid" width="1600" height="1200" fetchpriority="high">
    <div class="hero-badge">%s<span class="hb-t"><b>%s din %d de recenzii</b></span></div>
  </div>
</div></div>

<div class="spec"><div class="wrap"><div class="spec-g">
  <div class="spec-i"><div class="spec-n">%d<em>+ ani</em></div><div class="spec-l">De experiență</div></div>
  <div class="spec-i"><div class="spec-n">%d<em>+</em></div><div class="spec-l">Lucrări finalizate</div></div>
  <div class="spec-i"><div class="spec-n">5</div><div class="spec-l">Județe deservite integral</div></div>
  <div class="spec-i"><div class="spec-n">0<em> lei</em></div><div class="spec-l">Deplasare și deviz</div></div>
</div></div></div>
</section>

%s

<section class="sec"><div class="wrap">
  <div class="sec-h rv"><span class="kicker">Servicii</span>
    <h2>Tot ce ține de acoperișul dumneavoastră</h2>
    <p>De la o reparație de o zi până la un acoperiș executat de la șarpantă. Aceleași echipe pentru toate etapele, deci un singur responsabil pentru rezultat.</p></div>
  <div class="svc">%s</div>
  <div style="margin-top:28px"><a class="btn btn-o" href="/servicii/">Vedeți toate cele %d servicii</a></div>
</div></section>

<section class="sec sec-dark"><div class="wrap">
  <div class="sec-h rv"><span class="kicker kicker-l">Cum lucrăm</span>
    <h2>De la primul mesaj la acoperișul predat</h2>
    <p>Patru pași, fără niciun cost până în momentul în care acceptați oferta.</p></div>
  <div class="proc rv">%s</div>
</div></section>

<section class="sec"><div class="wrap">
  <div class="sec-h rv"><span class="kicker">De ce noi</span>
    <h2>Șase lucruri pe care le puteți verifica</h2>
    <p>Un acoperiș se vede greu după montaj, iar problemele apar abia la a doua sau a treia iarnă. Astea sunt lucrurile pe care merită să le întrebați orice firmă, inclusiv pe noi.</p></div>
  <div class="why rv">%s</div>
</div></section>

<section class="sec sec-stone"><div class="wrap">
  <div class="sec-h rv"><span class="kicker">Lucrări</span>
    <h2>Fotografii de pe șantierele noastre</h2>
    <p>Nu randări, nu poze de stoc. Case reale, la care au lucrat echipele noastre.</p></div>
  <div class="work">%s</div>
  <div style="margin-top:28px"><a class="btn btn-o" href="/lucrari/">Vedeți toate lucrările</a></div>
</div></section>

<section class="sec"><div class="wrap">
  <div class="sec-h sec-h-c rv"><span class="kicker">Recenzii</span><h2>Ce spun clienții</h2></div>
  <div class="rev-line rv">%s<b>%s din %d de recenzii</b></div>
  <div class="rev-g">%s</div>
</div></section>

<section class="sec sec-dark"><div class="wrap"><div class="zone">
  <div>
    <span class="kicker kicker-l">Zona de lucru</span>
    <h2>Ne deplasăm oriunde în România</h2>
    <p>Nu suntem legați de un singur județ. Echipele noastre lucrează în toată țara, iar pentru lucrările mai mari ne cazăm în zonă pe durata execuției. Spuneți-ne unde este casa și vă confirmăm în aceeași zi dacă putem prelua lucrarea.</p>
    <div class="zone-chips">%s</div>
    <a class="btn btn-p" href="/zona-acoperire/">Vedeți detalii</a>
  </div>
  <div class="zone-facts">
    <div class="zone-f"><span>Telefon</span><b>%s</b></div>
    <div class="zone-f"><span>Program</span><b>Luni – duminică<br>07:00 – 21:00</b></div>
    <div class="zone-f"><span>Deplasare</span><b>Gratuită, în toată țara</b></div>
    <div class="zone-f"><span>Răspuns</span><b>În aceeași zi pe WhatsApp</b></div>
  </div>
</div></div></section>

<section class="sec"><div class="wrap">
  <div class="sec-h sec-h-c rv"><span class="kicker">Întrebări frecvente</span>
    <h2>Ce ne întreabă oamenii cel mai des</h2></div>
  %s
  <div style="margin-top:28px;text-align:center"><a class="btn btn-o" href="/intrebari-frecvente/">Toate întrebările</a></div>
</div></section>

%s""" % (WA_LINK, TEL, B["tel_disp"], stars(), B["rating"], B["reviews"],
         B["years"], B["projects"], partners_section(), svc, len(SERVICES), proc, why_h, work,
         stars(), B["rating"], B["reviews"], revs, chips, B["tel_disp"],
         faq_block(FAQ[:5]), cta_section()) + footer()


def page_servicii():
    cards = "".join("""<article class="svc-c rv" id="%s">
      <div class="svc-ph"><img src="/images/%s" alt="%s" loading="lazy" width="900" height="506">
        <span class="svc-tag">%s</span></div>
      <div class="svc-b"><h3>%s</h3><p>%s</p></div></article>"""
                    % (s["k"], s["img"], s["t"], s["tag"], s["t"], s["d"]) for s in SERVICES)
    extra = ["Ferestre de mansardă și luminatoare", "Parazăpezi și accesorii de siguranță",
             "Tratamente ignifuge și antifungice pentru lemn", "Streșini lambrisate și pazii",
             "Curățare și revizie anuală de acoperiș", "Montaj coșuri de fum și racorduri"]
    svcld = {"@context": "https://schema.org", "@type": "ItemList",
             "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": s["t"],
                                  "url": B["domain"] + "/servicii/#" + s["k"]}
                                 for i, s in enumerate(SERVICES)]}
    return head("Servicii acoperișuri | Montaj, înlocuire, reparații — Acoperișul Solid",
                "Montaj acoperiș nou, înlocuire învelitoare, reparații și infiltrații, șarpante, mansardări, jgheaburi, tinichigerie și hidroizolații. Echipe în județele Iași, Suceava, Vaslui, Neamț și Bacău.",
                "/servicii/", "srv-acoperis-nou.jpg", "Servicii", extra=svcld) + header("servicii") + """
%s
<section class="sec"><div class="wrap"><div class="svc">%s</div></div></section>

<section class="sec sec-stone"><div class="wrap">
  <div class="sec-h rv"><span class="kicker">Și în plus</span><h2>Lucrări conexe pe care le executăm</h2>
    <p>În cadrul unei lucrări mai mari sau separat, dacă asta aveți nevoie.</p></div>
  <ul class="slist">%s</ul>
</div></section>

%s""" % (phero("Servicii", "Servicii de acoperișuri",
               "Executăm manoperă și montaj complet, de la o reparație punctuală până la un acoperiș ridicat de la zero. Toate lucrările vin cu garanție scrisă la manoperă."),
         cards, "".join("<li>%s</li>" % x for x in extra), cta_section()) + footer()


def page_lucrari():
    cards = "".join("""<a class="work-c rv" href="%s" target="_blank" rel="noopener">
      <img src="/images/%s" alt="%s — %s" loading="lazy" width="900" height="600">
      <div class="work-o"><span>%s · %s</span><h3>%s</h3></div></a>"""
                    % (WA_LINK, im, t, loc, tag, loc, t) for im, tag, t, loc in WORKS)
    return head("Lucrări executate | Galerie foto acoperișuri — Acoperișul Solid",
                "Fotografii reale de pe șantierele noastre: acoperișuri din țiglă metalică, șarpante, mansardări și sisteme pluviale, executate în Iași, Suceava, Vaslui, Neamț și Bacău.",
                "/lucrari/", "acoperis-tigla-metalica-rosie.jpg", "Lucrări") + header("lucrari") + """
%s
<section class="sec"><div class="wrap">
  <div class="work">%s</div>
  <div style="margin-top:40px;text-align:center">
    <p style="margin-bottom:18px">Vreți să vedeți o lucrare asemănătoare cu ce aveți de făcut? Spuneți-ne ce casă aveți și vă trimitem poze de la un proiect similar.</p>
    <a class="btn btn-wa" href="%s" target="_blank" rel="noopener">Cereți poze pe WhatsApp</a>
  </div>
</div></section>

%s""" % (phero("Lucrări", "Lucrări executate",
               "Peste %d de acoperișuri în %d ani. Mai jos sunt fotografii făcute pe șantierele noastre — case reale, nu randări." % (B["projects"], B["years"])),
         cards, WA_LINK, cta_section()) + footer()


def page_calculator():
    return head("Calculator preț acoperiș | Cerere de ofertă gratuită",
                "Aflați intervalul orientativ de preț pentru manoperă, materiale și șarpantă. Trimiteți detaliile pe email și primiți un răspuns în aceeași zi.",
                "/calculator-pret/", "acoperis-casa-noua-antracit.jpg", "Calculator preț") + header("calculator-pret") + """
%s
<section class="sec sec-stone"><div class="wrap">
  <div class="sec-h rv"><span class="kicker">De citit</span><h2>De ce nu se poate da un preț la telefon</h2></div>
  <div class="arg rv">
    <div class="arg-i"><h3>Panta adaugă între 16 și 50 la sută</h3>
      <p>Acoperișul este o suprafață înclinată, deci mai mare decât amprenta pe care o acoperă. La o casă obișnuită diferența e de aproximativ o treime; la un pod înalt ajunge la jumătate. O estimare dată pe suprafața casei iese aproape mereu prea mică.</p></div>
    <div class="arg-i"><h3>Streașina nu intră în amprentă</h3>
      <p>Acoperișul depășește pereții cu 40–80 cm de jur împrejur. La o casă de 10 pe 12 metri, doar streașina adaugă câțiva metri pătrați de învelitoare, folie, șipcă și manoperă.</p></div>
    <div class="arg-i"><h3>Forma contează mai mult decât mărimea</h3>
      <p>Două acoperișuri de aceeași suprafață pot diferi mult ca preț. Doliile, lucarnele, coșurile și racordurile cer timp și tinichigerie croită pe loc — acolo se duce manopera, nu pe suprafețele drepte.</p></div>
    <div class="arg-i"><h3>De aceea venim și măsurăm</h3>
      <p>Măsurătoarea durează sub o oră și este gratuită, indiferent dacă lucrați cu noi sau nu. După ea primiți un deviz pe etape, cu preț final, pe care îl puteți compara cu orice altă ofertă.</p></div>
  </div>
</div></section>

<section class="sec"><div class="wrap"><div class="cta">
  <div>
    <span class="kicker">Preț orientativ</span>
    <h2>Trimiteți detaliile și primiți un interval de preț</h2>
    <p style="font-size:1.02rem;margin-top:14px">Spuneți-ne aproximativ câți metri pătrați are casa la sol, ce învelitoare v-ați dori și dacă aveți nevoie de șarpantă nouă. Vă răspundem pe email cu un interval orientativ; prețul final vine după măsurătoare, care este gratuită.</p>
  </div>
  %s
</div></div></section>
""" % (phero("Calculator preț", "Cât costă acoperișul dumneavoastră",
             "Prețul depinde de suprafața reală, panta acoperișului, învelitoarea aleasă și starea structurii — nu poate fi dat corect fără o vizită. Trimiteți-ne detaliile și vă răspundem cu un interval orientativ pe email."),
       form("k", "Cereți o estimare", "Completați formularul și vă răspundem pe email cu un interval de preț.")) + footer()


def page_acoperire():
    chips = "".join("<span>%s</span>" % c for c in REGIONS)
    judet_blocks = "".join("""<div class="arg-i" style="border-color:var(--copper)">
      <h3>Județul %s</h3>
      <p>Acoperim toată raza județului — nu doar %s, ci și %s și toate comunele și satele din jurul lor.</p></div>"""
        % (j, locs[0], ", ".join(locs[1:])) for j, locs in JUDETE_LOC.items())

    return head("Unde lucrăm | Acoperișuri în Iași, Suceava, Vaslui, Neamț, Bacău — Acoperișul Solid",
                "Lucrăm pe toată raza județelor Iași, Suceava, Vaslui, Neamț și Bacău — orașe, comune și sate, nu doar reședințele de județ. Deplasare și măsurătoare gratuite.",
                "/zona-acoperire/", "acoperis-finalizat-casa-parter.jpg", "Unde lucrăm") + header("acoperire") + """
%s
<section class="sec"><div class="wrap">
  <div class="sec-h rv"><span class="kicker">Acoperire</span><h2>Cinci județe, acoperite integral</h2>
    <p>Nu ne oprim la orașele reședință de județ. Lucrăm pe toată raza fiecărui județ — la orice comună sau sat, la fel ca la reședința de județ.</p></div>
  <div class="zone-chips" style="margin-bottom:34px">%s</div>
  <div class="arg rv">%s</div>
</div></section>

<section class="sec sec-dark"><div class="wrap">
  <div class="sec-h rv"><span class="kicker kicker-l">Cum funcționează</span><h2>Deplasarea nu vă costă nimic</h2></div>
  <div class="arg rv">
    <div class="arg-i" style="border-color:var(--copper)"><h3>Evaluare gratuită, oriunde în cele 5 județe</h3>
      <p>Ne deplasăm pentru evaluare și măsurători fără niciun cost, la oraș sau la sat, și fără să vă oblige la ceva. Dacă în urma măsurătorii decideți să nu lucrați cu noi, nu plătiți nimic.</p></div>
    <div class="arg-i" style="border-color:var(--copper)"><h3>Nicio comună nu e "prea departe"</h3>
      <p>Nu tratăm diferit un client din reședința de județ față de unul dintr-o comună. Prețul manoperei rămâne același, indiferent de localitate.</p></div>
    <div class="arg-i" style="border-color:var(--copper)"><h3>Un singur responsabil</h3>
      <p>Nu dăm lucrarea mai departe către echipe locale găsite pentru un singur proiect. Oamenii care vin la măsurătoare sunt cei care execută și cei la care puteți reveni după finalizare.</p></div>
    <div class="arg-i" style="border-color:var(--copper)"><h3>Confirmare în aceeași zi</h3>
      <p>Ne scrieți localitatea și vă spunem în aceeași zi dacă putem prelua lucrarea și în ce interval ne putem încadra.</p></div>
  </div>
</div></section>

%s""" % (phero("Unde lucrăm", "Acoperim tot județul, nu doar orașul",
               "Lucrăm pe toată raza județelor Iași, Suceava, Vaslui, Neamț și Bacău. Deplasarea pentru evaluare și măsurători este gratuită, la oraș sau la sat."),
         chips, judet_blocks, cta_section()) + footer()


def page_faq():
    return head("Întrebări frecvente despre acoperișuri | Acoperișul Solid",
                "Prețuri, garanție, materiale, durata lucrărilor, zone de lucru. Răspunsuri clare la întrebările pe care ni le pun cel mai des clienții.",
                "/intrebari-frecvente/", "montaj-fereastra-mansarda.jpg", "Întrebări frecvente",
                extra=FAQ_LD) + header("intrebari-frecvente") + """
%s
<section class="sec"><div class="wrap">%s</div></section>
%s""" % (phero("Întrebări frecvente", "Întrebări frecvente",
               "Dacă nu găsiți răspunsul aici, scrieți-ne pe WhatsApp. Vă spunem cum stau lucrurile chiar dacă răspunsul nu e cel pe care sperați să îl auziți."),
         faq_block(FAQ), cta_section()) + footer()


def page_contact():
    return head("Contact | Acoperișul Solid — %s" % B["tel_disp"],
                "Sunați la %s sau scrieți pe WhatsApp. Răspundem în aceeași zi. Deplasare și deviz gratuit în tot județul Iași, Suceava, Vaslui, Neamț sau Bacău." % B["tel_disp"],
                "/contact/", "acoperis-tigla-metalica-rosie.jpg", "Contact") + header("contact") + """
%s
<section class="sec"><div class="wrap">
  <div class="cont">
    <div class="cont-c"><span class="why-k">Telefon</span><b><a href="%s">%s</a></b>
      <p>Luni – duminică, 07:00 – 21:00. Pentru infiltrații active răspundem și în afara programului.</p></div>
    <div class="cont-c"><span class="why-k">WhatsApp</span><b><a href="%s" target="_blank" rel="noopener">Trimiteți un mesaj</a></b>
      <p>Cel mai rapid canal. Trimiteți două-trei poze cu acoperișul și vă răspundem în aceeași zi.</p></div>
    <div class="cont-c"><span class="why-k">Zonă</span><b>Toată România</b>
      <p>Ne deplasăm oriunde în țară. Lucrările le executăm la dumneavoastră, nu avem showroom.</p></div>
  </div>

  <div class="cta">
    <div>
      <span class="kicker">Ce ne ajută să răspundem rapid</span>
      <h2>Trei informații și vă putem da un interval</h2>
      <p style="margin-top:14px">Aproximativ câți metri pătrați are casa la sol, ce învelitoare aveți acum sau ce v-ați dori, și în ce localitate este. Cu astea trei vă putem spune destul de exact unde stați, încă înainte să venim.</p>
      <p style="margin-top:12px">Dacă aveți și două poze, cu atât mai bine — o poză de ansamblu și una cu zona problemă.</p>
      <div class="hero-act" style="margin-top:22px">
        <a class="btn btn-wa" href="%s" target="_blank" rel="noopener">Scrieți pe WhatsApp</a>
        <a class="btn btn-o" href="%s">Sunați acum</a>
      </div>
    </div>
    %s
  </div>
</div></section>
""" % (phero("Contact", "Hai să vorbim despre acoperișul dumneavoastră",
             "Cel mai rapid este pe WhatsApp sau la telefon. Ne spuneți ce aveți de făcut, stabilim o vizită și primiți un deviz cu preț final."),
       TEL, B["tel_disp"], WA_LINK, WA_LINK, TEL,
       form("m", "Scrieți-ne", "Completați formularul și vă răspundem pe email.")) + footer()


def page_despre():
    return head("Despre noi | Echipe de acoperișuri în Iași, Suceava, Vaslui, Neamț, Bacău",
                "Peste %d ani de experiență și %d+ de acoperișuri executate. Echipe proprii, fără subcontractare, active pe toată raza județelor Iași, Suceava, Vaslui, Neamț și Bacău." % (B["years"], B["projects"]),
                "/despre/", "sarpanta-lemn-casa-noua.jpg", "Despre noi") + header("despre") + """
%s
<section class="sec"><div class="wrap"><div class="about rv">
  <div>
    <span class="kicker">Cine suntem</span>
    <h2>Meseriași, nu intermediari</h2>
    <p>Am început ca o echipă mică de dulgheri și tinichigii. În peste %d ani am ajuns să executăm acoperișuri complete în toată țara, de la structura de lemn până la ultimul burlan, fără să dăm lucrările mai departe către altcineva.</p>
    <p>Am rămas la un model simplu: echipe care se deplasează, care stau în zonă până termină și care răspund la telefon și după doi ani de la lucrare. Nu suntem cea mai ieftină variantă de pe piață și nu ne propunem să fim.</p>
    <p>Ce ne diferențiază cel mai mult e ce facem înainte să începem: măsurăm, explicăm ce se poate găsi sub învelitoarea veche și punem totul în deviz, pe etape. Un client care știe dinainte ce urmează nu are surprize la final.</p>
  </div>
  <img src="/images/sarpanta-lemn-casa-noua.jpg" alt="Șarpantă din lemn executată de echipa Acoperișul Solid la o casă în construcție" loading="lazy" width="1200" height="1600">
</div></div></section>

<section class="sec sec-stone"><div class="wrap">
  <div class="spec-g" style="background:#fff;border:1px solid var(--line);border-radius:var(--r-lg);overflow:hidden">
    <div class="spec-i"><div class="spec-n">%d<em>+ ani</em></div><div class="spec-l">De experiență</div></div>
    <div class="spec-i"><div class="spec-n">%d<em>+</em></div><div class="spec-l">Lucrări finalizate</div></div>
    <div class="spec-i"><div class="spec-n">%s</div><div class="spec-l">Din %d de recenzii</div></div>
    <div class="spec-i"><div class="spec-n">5</div><div class="spec-l">Județe deservite integral</div></div>
  </div>
</div></section>

<section class="sec"><div class="wrap">
  <div class="sec-h rv"><span class="kicker">Cum lucrăm</span><h2>Șase reguli la care nu facem rabat</h2></div>
  <div class="arg rv">
    <div class="arg-i"><h3>Prețul din deviz e prețul final</h3>
      <p>Dacă apare ceva neprevăzut sub învelitoare, oprim, vă sunăm, vă arătăm cu poze și continuăm doar după acordul dumneavoastră. Nu anunțăm costuri noi la jumătatea lucrării.</p></div>
    <div class="arg-i"><h3>Contrașipca nu e opțională</h3>
      <p>Folia anticondens funcționează doar cu contrașipci care lasă aerul să circule pe sub învelitoare. Fără ele condensează și udă izolația. E fix etapa pe care o ofertă ieftină o sare, pentru că nu se vede după montaj.</p></div>
    <div class="arg-i"><h3>Se lucrează cu ancoraj</h3>
      <p>Oamenii noștri lucrează legați, cu ham și linie de viață. Costă timp, dar nu vrem să explicăm nimănui de ce a căzut cineva de pe casa lui.</p></div>
    <div class="arg-i"><h3>Strângem după noi</h3>
      <p>Molozul, învelitoarea veche și cuiele pleacă odată cu noi. Curtea rămâne cum a fost, nu ca după un șantier.</p></div>
    <div class="arg-i"><h3>Garanția e scrisă</h3>
      <p>Nu spusă la telefon. Dacă apare o problemă la ce am executat noi, ne întoarcem și o rezolvăm.</p></div>
    <div class="arg-i"><h3>Spunem și când nu merită</h3>
      <p>Uneori un acoperiș nu are nevoie de înlocuire, ci de o reparație de câteva sute de lei. Vă spunem asta, chiar dacă înseamnă o lucrare mai mică pentru noi.</p></div>
  </div>
</div></section>

%s""" % (phero("Despre noi", "O echipă care se deplasează, nu un intermediar",
               "Peste %d ani în acoperișuri și %d+ de lucrări finalizate, în județele Iași, Suceava, Vaslui, Neamț și Bacău." % (B["years"], B["projects"])),
         B["years"], B["years"], B["projects"], B["rating"], B["reviews"], cta_section()) + footer()


def page_404():
    return head("Pagina nu a fost găsită | " + B["name"],
                "Pagina căutată nu există. Reveniți la pagina principală sau contactați-ne.",
                "/404.html", noindex=True) + header("") + """
<section class="e404"><div class="wrap">
  <div class="e404-big">404</div>
  <h1>Pagina asta nu există</h1>
  <p>Poate a fost mutată sau linkul e greșit. Vă puteți întoarce la pagina principală sau ne puteți scrie direct.</p>
  <div class="hero-act" style="justify-content:center">
    <a class="btn btn-p" href="/">Înapoi la pagina principală</a>
    <a class="btn btn-wa" href="%s" target="_blank" rel="noopener">Scrieți pe WhatsApp</a>
  </div>
</div></section>
""" % WA_LINK + footer()


def redirect(target):
    return """<!DOCTYPE html><html lang="ro"><head><meta charset="UTF-8">
<title>Redirecționare…</title><link rel="canonical" href="%s%s">
<meta name="robots" content="noindex, follow">
<meta http-equiv="refresh" content="0; url=%s">
<script>location.replace("%s");</script></head>
<body><p>Redirecționare către <a href="%s">%s%s</a>…</p></body></html>""" % (
        B["domain"], target, target, target, target, B["domain"], target)


# ------------------------------------------------------------------ output
PAGES = {
    "index.html":                      page_home(),
    "servicii/index.html":             page_servicii(),
    "lucrari/index.html":              page_lucrari(),
    "calculator-pret/index.html":      page_calculator(),
    "zona-acoperire/index.html":       page_acoperire(),
    "intrebari-frecvente/index.html":  page_faq(),
    "contact/index.html":              page_contact(),
    "despre/index.html":               page_despre(),
    "404.html":                        page_404(),
}

REDIRECTS = {
    "oferta": "/calculator-pret/", "calculator": "/calculator-pret/", "pret": "/calculator-pret/",
    "preturi": "/calculator-pret/", "proiecte": "/lucrari/", "portofoliu": "/lucrari/",
    "galerie": "/lucrari/", "despre-noi": "/despre/", "faq": "/intrebari-frecvente/",
    "intrebari": "/intrebari-frecvente/", "acoperisuri": "/servicii/", "zone": "/zona-acoperire/",
    "acoperire": "/zona-acoperire/", "acoperire-nationala": "/zona-acoperire/",
}

FAVICON = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 36 36">
<rect width="36" height="36" rx="8" fill="#12261E"/>
<path d="M6 19.5 L18 9 L30 19.5" stroke="#C4562A" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
<path d="M10 21.5c1.6 0 1.6 2 3.2 2s1.6-2 3.2-2 1.6 2 3.2 2 1.6-2 3.2-2 1.6 2 3.2 2" stroke="#fff" stroke-width="2.1" stroke-linecap="round" fill="none"/>
<path d="M10 26.5c1.6 0 1.6 2 3.2 2s1.6-2 3.2-2 1.6 2 3.2 2 1.6-2 3.2-2 1.6 2 3.2 2" stroke="#fff" stroke-width="2.1" stroke-linecap="round" fill="none" opacity=".55"/>
</svg>"""

MANIFEST = {"name": B["name"] + " — " + B["tagline"], "short_name": B["name"],
            "start_url": "/", "display": "standalone", "background_color": "#FFFFFF",
            "theme_color": "#12261E", "lang": "ro",
            "icons": [{"src": "/favicon.svg", "sizes": "any", "type": "image/svg+xml"}]}

SITEMAP = [("/", "1.0", "weekly"), ("/servicii/", "0.9", "monthly"),
           ("/calculator-pret/", "0.9", "monthly"), ("/lucrari/", "0.8", "monthly"),
           ("/zona-acoperire/", "0.8", "monthly"), ("/despre/", "0.7", "yearly"),
           ("/intrebari-frecvente/", "0.7", "monthly"), ("/contact/", "0.8", "yearly")]

ROBOTS = """User-agent: *
Allow: /

Disallow: /oferta/
Disallow: /calculator/
Disallow: /pret/
Disallow: /preturi/
Disallow: /proiecte/
Disallow: /portofoliu/
Disallow: /galerie/
Disallow: /despre-noi/
Disallow: /faq/
Disallow: /intrebari/
Disallow: /acoperisuri/
Disallow: /zone/
Disallow: /acoperire/
Disallow: /acoperire-nationala/

Sitemap: %s/sitemap.xml
""" % B["domain"]

README = """# %s — acoperisulsolid.ro

Site static generat cu `build.py`. GitHub Pages, fără build tools.

## Regenerare

```bash
python3 build.py
```

**Nu editați fișierele HTML direct** — se suprascriu la fiecare rulare. Editați `build.py`.

## Pagini

| Pagină | URL |
|---|---|
| Acasă | `/` |
| Servicii | `/servicii/` |
| Lucrări | `/lucrari/` |
| Calculator preț | `/calculator-pret/` |
| Unde lucrăm | `/zona-acoperire/` |
| Întrebări frecvente | `/intrebari-frecvente/` |
| Despre noi | `/despre/` |
| Contact | `/contact/` |

Plus 13 redirecturi (meta refresh + JS), excluse din sitemap și blocate în robots.txt.

## Contact

Nu există backend propriu. Formularele de pe site trimit datele prin
[Web3Forms](https://web3forms.com/) (`action="https://api.web3forms.com/submit"`,
cheia din `WEB3FORMS_KEY`) către adresa de e-mail configurată pentru acea cheie.
Linkurile directe de telefon și WhatsApp (header, bara mobilă) rămân construite
static, în `build.py`, prin `TEL` și `WA_LINK`.

## SEO

- `sitemap.xml` — doar cele 8 pagini reale
- `robots.txt` — blochează explicit redirecturile
- Canonical, OG și Twitter Card pe fiecare pagină
- JSON-LD: `RoofingContractor` + `BreadcrumbList` pe toate paginile,
  `FAQPage` pe acasă și pe întrebări, `ItemList` pe servicii
- Titluri și meta description unice pe fiecare pagină

## Design

- Paletă: verde pin `#12261E`, aramă `#C4562A`, piatră `#F1F3F0`
- Typography: Fraunces (titluri), Figtree (text), Space Grotesk (cifre)
- Motiv recurent: profilul ondulat al țiglei metalice (kickere, separatoare, logo)
""" % B["name"]


def write(rel, content):
    path = os.path.join(ROOT, rel)
    d = os.path.dirname(path)
    if d:
        os.makedirs(d, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def main():
    n = 0
    for rel, html in PAGES.items():
        write(rel, html); n += 1
    for slug, target in REDIRECTS.items():
        write("%s/index.html" % slug, redirect(target)); n += 1
    write("favicon.svg", FAVICON)
    write("site.webmanifest", json.dumps(MANIFEST, ensure_ascii=False, indent=2))
    write("robots.txt", ROBOTS)
    write("CNAME", "acoperisulsolid.ro\n")
    write(".nojekyll", "")
    write("README.md", README)
    urls = "\n".join(
        '  <url><loc>%s%s</loc><changefreq>%s</changefreq><priority>%s</priority></url>'
        % (B["domain"], u, cf, p) for u, p, cf in SITEMAP)
    write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n'
                         '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                         + urls + "\n</urlset>\n")
    print("OK — %d pagini HTML + assets" % n)


if __name__ == "__main__":
    main()
