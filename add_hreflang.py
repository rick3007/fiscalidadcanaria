#!/usr/bin/env python3
"""Insert hreflang alternates into blog pages (idempotent).

Run after generate_blog_langs.py or after adding a translated article.
"""
import os, re

BASE = 'https://fiscalidadcanaria.com'

# Each group: lang -> path (without domain). 'es' is also x-default.
GROUPS = [
    {'es': '/blog/', 'en': '/en/blog/', 'de': '/de/blog/', 'it': '/it/blog/', 'fr': '/fr/blog/'},
    {'es': '/blog/zec-zona-especial-canaria/',
     'en': '/en/blog/zec-canary-islands-special-zone/',
     'de': '/de/blog/zec-sonderwirtschaftszone-kanarische-inseln/',
     'it': '/it/blog/zec-zona-speciale-canaria/',
     'fr': '/fr/blog/zec-zone-speciale-canarienne/'},
    {'es': '/blog/ric-reserva-inversiones-canarias/',
     'en': '/en/blog/ric-canary-islands-investment-reserve/',
     'de': '/de/blog/ric-investitionsruecklage-kanarische-inseln/',
     'it': '/it/blog/ric-riserva-investimenti-canarie/',
     'fr': '/fr/blog/ric-reserve-investissements-canaries/'},
    {'es': '/blog/igic-vs-iva/',
     'en': '/en/blog/igic-vs-vat/',
     'de': '/de/blog/igic-vs-mehrwertsteuer/',
     'it': '/it/blog/igic-vs-iva-canarie/',
     'fr': '/fr/blog/igic-vs-tva/'},
    {'es': '/blog/ley-segunda-oportunidad-canarias/',
     'en': '/en/blog/second-chance-law-canary-islands/',
     'de': '/de/blog/gesetz-zweite-chance-kanarische-inseln/',
     'it': '/it/blog/legge-seconda-opportunita-canarie/',
     'fr': '/fr/blog/loi-seconde-chance-canaries/'},
    {'es': '/blog/regimen-fiscal-canario-internacionales/',
     'en': '/en/blog/canary-islands-tax-regime-international-entrepreneurs/',
     'de': '/de/blog/steuerregime-kanarische-inseln-internationale-unternehmer/',
     'it': '/it/blog/regime-fiscale-canario-imprenditori-internazionali/',
     'fr': '/fr/blog/regime-fiscal-canarien-entrepreneurs-internationaux/'},
]


def hreflang_tags(path):
    """Return the hreflang <link> block for the group containing path, or ''."""
    for group in GROUPS:
        if path in group.values():
            lines = [f'<link rel="alternate" hreflang="{l}" href="{BASE}{p}">' for l, p in group.items()]
            lines.append(f'<link rel="alternate" hreflang="x-default" href="{BASE}{group["es"]}">')
            return '\n'.join(lines)
    return ''


def main():
    for group in GROUPS:
        for path in group.values():
            fn = path.strip('/') + '/index.html'
            with open(fn, encoding='utf-8') as f:
                html = f.read()
            html = re.sub(r'<link rel="alternate" hreflang="[^"]+" href="[^"]+">\n', '', html)
            canonical = re.search(r'<link rel="canonical" href="[^"]+">\n', html)
            if not canonical:
                print(f'✗ {fn}: no canonical')
                continue
            html = html[:canonical.end()] + hreflang_tags(path) + '\n' + html[canonical.end():]
            with open(fn, 'w', encoding='utf-8') as f:
                f.write(html)
            print(f'✓ {fn}')


if __name__ == '__main__':
    main()
