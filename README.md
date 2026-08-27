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

Nu există backend și **nu există adresă de e-mail pe site**. Toate formularele și
calculatorul compun un mesaj și îl deschid în WhatsApp către 0756 419 558
(`assets/script.js`, constanta `WA`).

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
