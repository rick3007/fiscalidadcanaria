#!/usr/bin/env python3
"""Generate static language pages from index.html translations."""
import re, os, json
from bs4 import BeautifulSoup

import subprocess, tempfile

with open('index.html', 'r', encoding='utf-8') as f:
    src = f.read()

# Use Node.js to extract T object (handles JS string escaping natively)
subprocess.run(['node', '-e', """
const fs = require('fs');
const src = fs.readFileSync('index.html', 'utf8');
const m = src.match(/const T = (\\{[\\s\\S]*?\\n\\});/);
eval('var T = ' + m[1]);
fs.writeFileSync('/tmp/translations.json', JSON.stringify(T));
"""], check=True, cwd='.')

with open('/tmp/translations.json', 'r', encoding='utf-8') as f:
    T = json.load(f)

META = {
    'en': {
        'title': 'Canary Islands Tax Advisory | Fiscal & Legal Services in Las Palmas',
        'desc':  'Expert tax and legal advisory specialised in the Canary Islands Economic Tax Regime. ZEC, RIC, IGIC, Corporation Tax. Free first consultation. Las Palmas de Gran Canaria.',
        'og_locale': 'en_GB',
    },
    'de': {
        'title': 'Steuerberatung Kanarische Inseln | Kanzlei Las Palmas de Gran Canaria',
        'desc':  'Steuerliche und rechtliche Beratung spezialisiert auf das kanarische Wirtschafts- und Steuerregime. ZEC, RIC, IGIC, Körperschaftsteuer. Erstes Gespräch kostenlos.',
        'og_locale': 'de_DE',
    },
    'it': {
        'title': 'Consulenza Fiscale Isole Canarie | Studio Legale e Fiscale Las Palmas',
        'desc':  'Consulenza fiscale e legale specializzata nel Regime Economico e Fiscale delle Canarie. ZEC, RIC, IGIC, Imposta sulle Società. Prima consulenza gratuita.',
        'og_locale': 'it_IT',
    },
    'fr': {
        'title': 'Conseil Fiscal Îles Canaries | Cabinet Fiscal et Juridique Las Palmas',
        'desc':  'Conseil fiscal et juridique spécialisé dans le Régime Économique et Fiscal des Canaries. ZEC, RIC, IGIC, Impôt sur les Sociétés. Première consultation gratuite.',
        'og_locale': 'fr_FR',
    },
}

for lang, meta in META.items():
    soup = BeautifulSoup(src, 'html.parser')
    translations = T.get(lang, {})

    # Update html lang attribute
    soup.html['lang'] = lang

    # Update title
    soup.find('title').string = meta['title']

    # Update meta description
    desc_tag = soup.find('meta', attrs={'name': 'description'})
    if desc_tag:
        desc_tag['content'] = meta['desc']

    # Update canonical
    canonical = soup.find('link', attrs={'rel': 'canonical'})
    if canonical:
        canonical['href'] = f'https://fiscalidadcanaria.com/{lang}/'

    # Update hreflang alternates (each must point to its own language path)
    hreflang_paths = {'es': '', 'en': 'en/', 'de': 'de/', 'it': 'it/', 'fr': 'fr/', 'x-default': ''}
    for tag in soup.find_all('link', attrs={'rel': 'alternate', 'hreflang': True}):
        path = hreflang_paths.get(tag['hreflang'])
        if path is not None:
            tag['href'] = f'https://fiscalidadcanaria.com/{path}'

    # Update og tags
    og_title = soup.find('meta', attrs={'property': 'og:title'})
    if og_title:
        og_title['content'] = meta['title']
    og_desc = soup.find('meta', attrs={'property': 'og:description'})
    if og_desc:
        og_desc['content'] = meta['desc']
    og_url = soup.find('meta', attrs={'property': 'og:url'})
    if og_url:
        og_url['content'] = f'https://fiscalidadcanaria.com/{lang}/'
    og_locale = soup.find('meta', attrs={'property': 'og:locale'})
    if og_locale:
        og_locale['content'] = meta['og_locale']

    # Update twitter tags
    tw_title = soup.find('meta', attrs={'name': 'twitter:title'})
    if tw_title:
        tw_title['content'] = meta['title']
    tw_desc = soup.find('meta', attrs={'name': 'twitter:description'})
    if tw_desc:
        tw_desc['content'] = meta['desc']

    # Replace data-i18n element content
    for el in soup.find_all(attrs={'data-i18n': True}):
        key = el['data-i18n']
        val = translations.get(key)
        if val is not None and not isinstance(val, list):
            el.clear()
            el.append(BeautifulSoup(str(val), 'html.parser'))

    # Set correct active lang button
    for btn in soup.find_all('button', class_='lang-btn'):
        if btn.get_text(strip=True) == lang.upper():
            btn['class'] = ['lang-btn', 'active']
        else:
            btn['class'] = ['lang-btn']

    # Update Blog link to point to language-specific blog
    for a in soup.find_all('a', href='/blog/'):
        a['href'] = f'/{lang}/blog/'

    # Set currentLang in JS
    html_str = str(soup)
    html_str = html_str.replace("let currentLang='es';", f"let currentLang='{lang}';")

    # Update base path for assets (fonts, etc.) — use absolute URL
    # No local assets, all external, so nothing to fix

    out_dir = lang
    os.makedirs(out_dir, exist_ok=True)
    with open(f'{out_dir}/index.html', 'w', encoding='utf-8') as f:
        f.write(html_str)
    print(f'✓ {lang}/index.html generated')

print('Done.')
