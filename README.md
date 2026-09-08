# Acoperișul Solid — acoperisulsolid.ro

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
