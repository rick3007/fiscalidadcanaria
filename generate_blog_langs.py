#!/usr/bin/env python3
"""Generate translated blog pages for EN, DE, IT, FR."""
import os

LANGS = {
    'en': {
        'blog_title': 'Blog — Fiscalidad Canaria | Articles on REF, ZEC, RIC & IGIC',
        'blog_desc': 'Articles and guides on the Canary Islands Tax Regime: ZEC, RIC, IGIC, Second Chance Law and taxation for international entrepreneurs.',
        'blog_h1': 'Blog — Fiscalidad Canaria',
        'blog_sub': 'Guides and articles on the Canary Islands Economic and Tax Regime, written by our specialists.',
        'blog_tag': 'Tax knowledge',
        'nav_back': '← Home',
        'nav_cta': 'Free consultation',
        'read_more': 'Read article →',
        'footer': '© 2026 Fiscalidad Canaria',
        'free_cta_title': 'Free first consultation',
        'free_cta_desc': 'Analyse your tax situation with no commitment. We speak English.',
        'free_cta_btn': 'Free consultation →',
        'by': 'By',
        'date': 'July 2026',
        'min_read': 'min read',
        'articles': [
            {
                'slug': 'zec-canary-islands-special-zone',
                'tag': 'Canary Islands Tax Regime',
                'title': 'ZEC Canary Islands Special Zone: what it is and how it works in 2026',
                'desc': 'Complete guide to the Canary Islands Special Zone (ZEC): requirements, 4% corporation tax rate and how to register. Updated 2026.',
                'keywords': 'ZEC canary islands special zone, ZEC canaries 2026, canary islands special zone requirements, canary islands 4% corporation tax',
                'read_time': '8',
                'breadcrumb_label': 'ZEC Canary Islands Special Zone',
                'intro': 'The <strong>Canary Islands Special Zone (ZEC)</strong> is one of the most powerful fiscal instruments available in the European Union. Created within the framework of the Canary Islands Economic and Tax Regime, it allows registered companies to pay <strong>4% corporation tax</strong>, compared to the general rate of 25% in mainland Spain.',
                'highlight': 'The ZEC offers a <strong>4% corporation tax rate</strong> — 21 percentage points below the general Spanish rate. For a company with €500,000 profit, that means savings of over €100,000 per year.',
                'sections': [
                    ('What is the ZEC?', 'The Canary Islands Special Zone was created by Law 19/1994 and is authorised by the European Union as State aid compatible with the internal market. Its aim is to promote economic development of the Canary Islands and compensate for the costs of outermost region status (remoteness, insularity and energy dependence).\n\nEntities registered in the ZEC can apply a <strong>reduced rate of 4%</strong> on the portion of the taxable base corresponding to operations carried out materially and effectively within the ZEC geographic area.'),
                    ('Main fiscal advantages', '<h3>4% corporation tax rate</h3><p>The main advantage. While the general rate in Spain is 25%, ZEC entities pay 4% on the ZEC-generated taxable base.</p><h3>IGIC exemption for certain operations</h3><p>Supplies of goods and services between ZEC entities are exempt from the Canary Islands General Indirect Tax (IGIC), facilitating trade between companies in the area.</p>'),
                    ('Requirements to register in the ZEC', '<h3>1. Permitted activities</h3><p>The ZEC admits a wide range of economic activities including technology, industrial, commercial, financial (with restrictions), R&D, consulting and logistics services.</p><h3>2. Minimum investment</h3><p>ZEC entities must make a minimum investment in fixed assets within the first two years: <strong>€100,000</strong> on Gran Canaria and Tenerife; <strong>€50,000</strong> on the smaller islands.</p><h3>3. Job creation</h3><p>At least <strong>5 jobs</strong> must be created within the first six months (3 on smaller islands) and maintained throughout the ZEC regime.</p><h3>4. Effective activity</h3><p>Operations benefiting from the reduced rate must be carried out materially and effectively within the ZEC. Purely instrumental structures are not admitted.</p>'),
                    ('Who can benefit from the ZEC?', 'The ZEC is particularly attractive for:\n<ul><li><strong>Technology and digital companies</strong> seeking a European base with low taxation</li><li><strong>International investors</strong> wanting to establish themselves in the EU with tax advantages</li><li><strong>Business groups</strong> looking to optimise their international tax structure</li><li><strong>Service companies</strong> with export or international activity</li><li><strong>Growing startups</strong> wanting to minimise their tax burden during expansion</li></ul>'),
                ],
            },
            {
                'slug': 'ric-canary-islands-investment-reserve',
                'tag': 'Canary Islands Tax Regime',
                'title': 'RIC Canary Islands Investment Reserve: complete guide 2026',
                'desc': 'How to reduce corporation tax by up to 90% with the Canary Islands Investment Reserve (RIC). Requirements, valid investments and practical savings example.',
                'keywords': 'RIC canary islands investment reserve, reduce corporation tax canaries, RIC canarias 2026',
                'read_time': '7',
                'breadcrumb_label': 'RIC Investment Reserve',
                'intro': 'The <strong>Canary Islands Investment Reserve (RIC)</strong> is one of the most powerful fiscal incentives in the Spanish tax system. It allows Canarian companies to reduce their <strong>corporation tax base by up to 90%</strong> of undistributed profits, provided those amounts are invested in the Canary Islands.',
                'highlight': 'A company with €200,000 net profit can allocate €180,000 (90%) to the RIC and pay tax on only €20,000. The tax saving compared to the general regime can exceed €40,000 per year.',
                'sections': [
                    ('What is the RIC and its legal basis?', 'The RIC is regulated in Article 27 of Law 19/1994. It is an accounting allocation that companies can make against undistributed profits, directly reducing the corporation tax base in the year of allocation. The RIC is approved by the EU as State aid compatible with the Treaty.'),
                    ('How the RIC works step by step', '<h3>1. Reserve allocation</h3><p>In the year profits are earned, the company can allocate up to <strong>90% of undistributed profits</strong> to the RIC, reducing the IS taxable base immediately.</p><h3>2. Investment deadline</h3><p>Allocated amounts must be invested within <strong>3 years</strong> from the end of the financial year in which the reserve was allocated.</p><h3>3. Asset retention</h3><p>Assets must remain in the company\'s assets for at least <strong>5 years</strong> (3 years for fungible goods).</p>'),
                    ('What investments qualify for the RIC?', '<h3>Fixed assets (Group A)</h3><ul><li>New fixed assets located in the Canary Islands (machinery, IT equipment, vehicles, etc.)</li><li>Construction or refurbishment of property used in economic activity</li><li>Shares in entities carrying out economic activities in the Canary Islands</li></ul><h3>Canarian public debt (Group B)</h3><ul><li>Subscription of debt securities issued by the Canary Islands Government or its autonomous bodies (max. 50% of total RIC allocation)</li></ul>'),
                    ('RIC compatibility with other incentives', 'The RIC is compatible with other Canary Islands REF incentives. Combined with the ZEC (4% IS rate) and the Investment Deduction (DIC), the effective tax rate can be reduced to near zero for companies that invest significantly in the Canary Islands.'),
                ],
            },
            {
                'slug': 'igic-vs-vat',
                'tag': 'Indirect Taxation',
                'title': 'IGIC vs VAT: key differences and tax advantages in the Canary Islands',
                'desc': 'Everything about the Canary Islands IGIC tax: rates, differences from VAT and how it affects your business. Complete guide 2026.',
                'keywords': 'IGIC VAT differences canary islands, IGIC canaries 2026, canary islands indirect tax, IGIC vs VAT spain',
                'read_time': '6',
                'breadcrumb_label': 'IGIC vs VAT',
                'intro': 'One of the first questions any business operating in — or thinking of establishing in — the Canary Islands asks is: <strong>what is the difference between IGIC and VAT?</strong> The answer has very significant fiscal implications for both businesses and end consumers.',
                'highlight': 'The Canary Islands are excluded from the EU VAT territory. Instead, <strong>IGIC at 7%</strong> applies instead of the general VAT rate of 21% — a 14 percentage point difference that represents a real competitive advantage.',
                'sections': [
                    ('What is the IGIC?', 'The <strong>Canary Islands General Indirect Tax (IGIC)</strong> is the indirect tax levied on consumption in the Canary Islands, created by Law 20/1991. Like VAT, it is a value-added tax levied on supplies of goods and services by businesses in the Canary Islands and on imports of goods into the Canary Islands territory.'),
                    ('IGIC rates in 2026', 'Zero rate (0%): basic food products, books, medicines, inter-island passenger transport.<br>Reduced rate (3%): new housing, water, electricity.<br><strong>General rate (7%)</strong>: most goods and services.<br>Increased rate (9.5%): tobacco.<br>Special rate (20%): certain luxury vehicles.'),
                    ('Key differences between IGIC and VAT', '<h3>1. Significantly lower rates</h3><p>The IGIC general rate is <strong>7%</strong> versus <strong>21%</strong> VAT. Goods and services in the Canary Islands are fiscally cheaper for end consumers.</p><h3>2. Canary Islands outside EU VAT territory</h3><p>The Canary Islands are excluded from the EU VAT area. This has important consequences for international operations.</p><h3>3. Imports are subject to IGIC, not VAT</h3><p>When a Canarian company imports goods from outside the islands (including mainland Spain), the transaction is subject to IGIC on entry into Canary Islands territory.</p>'),
                    ('Implications for businesses operating in the Canary Islands', 'For international investors, establishing in the Canary Islands means working with IGIC instead of VAT. The 7% general rate represents a competitive advantage in non-recoverable costs and commercial margins versus mainland or European competitors.'),
                ],
            },
            {
                'slug': 'second-chance-law-canary-islands',
                'tag': 'Insolvency Law',
                'title': 'Second Chance Law in the Canary Islands: guide for self-employed and individuals 2026',
                'desc': 'How the Second Chance Law works in the Canary Islands: who can apply, which debts are cancelled and the step-by-step process. Complete guide 2026.',
                'keywords': 'second chance law canary islands, debt cancellation canaries, insolvency self-employed canary islands, fresh start canary islands',
                'read_time': '8',
                'breadcrumb_label': 'Second Chance Law',
                'intro': 'The <strong>Second Chance Law</strong> allows natural persons — both individuals and self-employed — who are insolvent to obtain the <strong>total or partial cancellation of their debts</strong> and start afresh without the burden of the past.',
                'highlight': 'In the Canary Islands we have successfully processed Second Chance procedures with debt cancellations ranging from €30,000 to over €500,000. The first consultation is free and confidential.',
                'sections': [
                    ('Who can apply for the Second Chance Law?', 'Those who can apply for discharge of unsatisfied liabilities (BEPI) include: natural persons (individuals), self-employed with debts arising from their business activity, and sole traders in insolvency. Requirements: be a natural person (not available for companies), be in actual or imminent insolvency, have acted in good faith, no criminal convictions for economic offences in the previous 10 years.'),
                    ('Which debts can be cancelled?', '<h3>Debts that CAN be cancelled</h3><ul><li>Debts with banks (loans, mortgages, credit cards)</li><li>Debts with commercial suppliers and creditors</li><li>Social Security debts (up to certain limits)</li><li>Tax debts with HMRC equivalent (up to certain limits)</li><li>Rent arrears</li></ul><h3>Debts that CANNOT be cancelled</h3><ul><li>Child or spousal maintenance</li><li>Civil liability arising from criminal offence</li><li>Criminal fines</li></ul>'),
                    ('The process step by step', '<h3>Phase 1 — Insolvency proceedings</h3><p>An insolvency petition is filed with the Commercial Court, which appoints an insolvency administrator. The administrator inventories the debtor\'s assets and liabilities (6–18 months).</p><h3>Phase 2 — Asset liquidation</h3><p>If the debtor has assets, they are liquidated to partially repay creditors. The family home can be protected in certain circumstances.</p><h3>Phase 3 — Discharge application (BEPI)</h3><p>After liquidation, the debtor requests discharge of unsatisfied liabilities. If the judge finds good faith, the remaining debts are cancelled (1–3 months).</p>'),
                    ('What happens to the family home?', 'In most cases, if the home is mortgaged, the bank retains its security interest even if the debtor obtains discharge of other debts. However, if the debtor can continue paying the mortgage, they can keep the home. Legal strategies to protect the family home must be analysed case by case.'),
                ],
            },
            {
                'slug': 'canary-islands-tax-regime-international-entrepreneurs',
                'tag': 'International',
                'title': 'Canary Islands Tax Regime for international entrepreneurs: advantages and how to establish',
                'desc': 'Guide for foreign entrepreneurs and companies wanting to set up in the Canary Islands: REF advantages, ZEC, IGIC, requirements and process. Advice in English.',
                'keywords': 'set up company canary islands, canary islands tax advantages foreign company, digital nomads canary islands tax, ZEC canary islands foreign company',
                'read_time': '9',
                'breadcrumb_label': 'REF for internationals',
                'intro': 'The Canary Islands have become one of Europe\'s most attractive destinations for international entrepreneurs, digital nomads and foreign investors. The main reason: the <strong>Canary Islands Economic and Tax Regime (REF)</strong> offers unique tax advantages within the European Union that allow significant, fully legal tax reduction.',
                'highlight': 'We advise in <strong>Spanish, English, German, Italian and French</strong>. If you are thinking of setting up in the Canary Islands, we can guide you through the entire process from day one.',
                'sections': [
                    ('Why the Canary Islands for international entrepreneurs?', '<ul><li><strong>EU territory</strong>: full access to the single European market, double taxation treaties, free movement of capital</li><li><strong>Special tax regime</strong>: 4% corporation tax (ZEC), 7% IGIC, own deductions and incentives</li><li><strong>Climate and quality of life</strong>: one of the best climates in the world, modern infrastructure, international connectivity</li><li><strong>Legal stability</strong>: Spanish legal system (European legal certainty)</li><li><strong>GMT+0 timezone</strong>: ideal for working with Europe, America and Africa simultaneously</li></ul>'),
                    ('Main tax advantages of the REF', '<h3>1. ZEC — 4% Corporation Tax</h3><p>The ZEC allows 4% IS versus 25% general. Minimum investment from €50,000 on smaller islands, at least 3–5 jobs, effective activity in the Canary Islands required.</p><h3>2. IGIC at 7% instead of 21% VAT</h3><p>The Canary IGIC applies at 7% versus the 21% mainland VAT — a direct competitive price advantage.</p><h3>3. RIC — Up to 90% taxable base reduction</h3><p>The Investment Reserve allows reducing the IS taxable base by up to 90% of undistributed profits destined for Canary Islands investments.</p>'),
                    ('How to set up in the Canary Islands from abroad', '<h3>Step 1 — Define the legal structure</h3><p>The most common option for international investors is the <strong>Sociedad de Responsabilidad Limitada (S.L.)</strong>: minimum share capital of €1 (2023 reform), limited liability.</p><h3>Step 2 — Obtain NIE and NIF</h3><p>Foreign shareholders and directors must obtain a Foreigner Identification Number (NIE), essential for any procedure in Spain.</p><h3>Step 3 — Incorporate the company</h3><p>The full process takes <strong>2–4 weeks</strong> if documentation is in order: company name registration, bank account, notary deed, Commercial Register inscription, tax registration.</p><h3>Step 4 — Apply for ZEC status (if applicable)</h3><p>If requirements are met, the company can apply for inscription in the ZEC Entity Register. The process takes approximately 3 months.</p>'),
                    ('Digital nomads and the Beckham Law', 'Spain has the <strong>Digital Nomad Visa</strong> (since 2023), allowing non-EU remote workers to reside in Spain for up to 5 years. Additionally, the <strong>Beckham Law</strong> (Special Regime for Inpatriate Workers) allows new tax residents to pay a flat 24% IRPF rate on income (up to €600,000/year) for 6 years instead of the progressive general rate.'),
                ],
            },
        ],
    },
    'de': {
        'blog_title': 'Blog — Fiscalidad Canaria | Artikel über REF, ZEC, RIC & IGIC',
        'blog_desc': 'Artikel und Leitfäden zum Wirtschafts- und Steuerregime der Kanarischen Inseln: ZEC, RIC, IGIC, Gesetz der zweiten Chance und Besteuerung internationaler Unternehmer.',
        'blog_h1': 'Blog — Fiscalidad Canaria',
        'blog_sub': 'Leitfäden und Artikel zum kanarischen Wirtschafts- und Steuerregime, verfasst von unseren Spezialisten.',
        'blog_tag': 'Steuerwissen',
        'nav_back': '← Startseite',
        'nav_cta': 'Kostenloses Gespräch',
        'read_more': 'Artikel lesen →',
        'footer': '© 2026 Fiscalidad Canaria',
        'free_cta_title': 'Kostenloses Erstgespräch',
        'free_cta_desc': 'Analysieren Sie Ihre Steuersituation unverbindlich. Wir sprechen Deutsch.',
        'free_cta_btn': 'Kostenloses Gespräch →',
        'by': 'Von',
        'date': 'Juli 2026',
        'min_read': 'Min. Lesezeit',
        'articles': [
            {
                'slug': 'zec-sonderwirtschaftszone-kanarische-inseln',
                'tag': 'Kanarisches Steuerregime',
                'title': 'ZEC Sonderwirtschaftszone Kanarische Inseln: Was sie ist und wie sie 2026 funktioniert',
                'desc': 'Vollständiger Leitfaden zur Sonderwirtschaftszone der Kanarischen Inseln (ZEC): Anforderungen, 4% Körperschaftsteuersatz und Registrierungsverfahren. Aktualisiert 2026.',
                'keywords': 'ZEC Sonderwirtschaftszone Kanarische Inseln, ZEC Kanarische Inseln 2026, Körperschaftsteuer 4% Kanarische Inseln',
                'read_time': '8',
                'breadcrumb_label': 'ZEC Sonderwirtschaftszone',
                'intro': 'Die <strong>Sonderwirtschaftszone der Kanarischen Inseln (ZEC)</strong> ist eines der leistungsstärksten Steuerprivilegien innerhalb der Europäischen Union. Sie ermöglicht registrierten Unternehmen, nur <strong>4% Körperschaftsteuer</strong> zu zahlen — gegenüber dem allgemeinen Satz von 25% im spanischen Festland.',
                'highlight': 'Die ZEC bietet einen <strong>Körperschaftsteuersatz von 4%</strong> — 21 Prozentpunkte unter dem allgemeinen spanischen Satz. Bei einem Gewinn von 500.000€ bedeutet das eine jährliche Ersparnis von über 100.000€.',
                'sections': [
                    ('Was ist die ZEC?', 'Die ZEC wurde durch das Gesetz 19/1994 geschaffen und von der EU als mit dem Binnenmarkt vereinbare staatliche Beihilfe genehmigt. Ihr Ziel ist die Förderung der wirtschaftlichen Entwicklung der Kanarischen Inseln und der Ausgleich der Kosten der Ultramarginalität (Abgelegenheit, Insellage, Energieabhängigkeit).'),
                    ('Hauptsteuervorteile der ZEC', '<h3>4% Körperschaftsteuersatz</h3><p>Der wichtigste Vorteil. Während der allgemeine Satz in Spanien 25% beträgt, zahlen ZEC-Einheiten 4% auf die ZEC-Bemessungsgrundlage.</p><h3>IGIC-Befreiung für bestimmte Umsätze</h3><p>Lieferungen und Dienstleistungen zwischen ZEC-Einheiten sind von der kanarischen indirekten Steuer (IGIC) befreit.</p>'),
                    ('Anforderungen für die ZEC-Registrierung', '<h3>Zulässige Tätigkeiten</h3><p>Technologie, Industrie, Handel, Finanzdienstleistungen, F&E, Beratung, Logistik.</p><h3>Mindestinvestition</h3><p>100.000€ auf Gran Canaria und Teneriffa; 50.000€ auf den kleineren Inseln.</p><h3>Schaffung von Arbeitsplätzen</h3><p>Mindestens 5 Arbeitsplätze in den ersten sechs Monaten (3 auf kleineren Inseln).</p><h3>Effektive Tätigkeit</h3><p>Die Tätigkeiten müssen tatsächlich und materiell im ZEC-Gebiet ausgeübt werden.</p>'),
                    ('Wer profitiert von der ZEC?', 'Besonders attraktiv für: <ul><li><strong>Technologie- und Digitalunternehmen</strong>, die eine europäische Basis mit niedriger Besteuerung suchen</li><li><strong>Internationale Investoren</strong>, die sich in der EU niederlassen möchten</li><li><strong>Unternehmensgruppen</strong>, die ihre internationale Steuerstruktur optimieren wollen</li><li><strong>Wachsende Startups</strong></li></ul>'),
                ],
            },
            {
                'slug': 'ric-investitionsruecklage-kanarische-inseln',
                'tag': 'Kanarisches Steuerregime',
                'title': 'RIC Investitionsrücklage Kanarische Inseln: vollständiger Leitfaden 2026',
                'desc': 'Wie man die Körperschaftsteuer mit der kanarischen Investitionsrücklage (RIC) um bis zu 90% reduziert. Anforderungen, gültige Investitionen und Praxisbeispiel.',
                'keywords': 'RIC Kanarische Inseln Investitionsrücklage, Körperschaftsteuer reduzieren Kanarische Inseln, RIC Kanarische Inseln 2026',
                'read_time': '7',
                'breadcrumb_label': 'RIC Investitionsrücklage',
                'intro': 'Die <strong>Investitionsrücklage für die Kanarischen Inseln (RIC)</strong> ist einer der leistungsstärksten Steueranreize im spanischen Steuersystem. Sie ermöglicht kanarischen Unternehmen, ihre <strong>Körperschaftsteuerbemessungsgrundlage um bis zu 90%</strong> der nicht ausgeschütteten Gewinne zu reduzieren.',
                'highlight': 'Ein Unternehmen mit 200.000€ Nettogewinn kann 180.000€ (90%) als RIC dotieren und nur auf 20.000€ Steuern zahlen. Die Steuerersparnis gegenüber dem allgemeinen Regime kann 40.000€ pro Jahr übersteigen.',
                'sections': [
                    ('Was ist die RIC?', 'Die RIC ist in Artikel 27 des Gesetzes 19/1994 geregelt. Es handelt sich um eine Buchhaltungsrücklage, die Unternehmen aus nicht ausgeschütteten Gewinnen bilden können, was die Körperschaftsteuerbemessungsgrundlage im Dotierungsjahr direkt reduziert.'),
                    ('Wie die RIC funktioniert', '<h3>1. Dotierung der Rücklage</h3><p>Im Gewinnjahr kann die Rücklage auf bis zu <strong>90% der nicht ausgeschütteten Gewinne</strong> dotiert werden.</p><h3>2. Investitionsfrist</h3><p>Die dotierten Beträge müssen innerhalb von <strong>3 Jahren</strong> nach Abschluss des Geschäftsjahres investiert werden.</p><h3>3. Haltedauer</h3><p>Die Vermögenswerte müssen mindestens <strong>5 Jahre</strong> gehalten werden.</p>'),
                    ('Zulässige Investitionen für die RIC', '<h3>Sachanlagen (Gruppe A)</h3><ul><li>Neue Sachanlagen auf den Kanarischen Inseln (Maschinen, IT-Geräte, Fahrzeuge)</li><li>Bau oder Renovierung von Gewerbeimmobilien</li><li>Beteiligungen an Unternehmen mit Tätigkeit auf den Kanarischen Inseln</li></ul><h3>Kanarische Staatsanleihen (Gruppe B)</h3><ul><li>Höchstens 50% der gesamten RIC-Dotierung</li></ul>'),
                    ('Vereinbarkeit mit anderen Anreizen', 'Die RIC ist mit anderen Anreizen des REF vereinbar: ZEC (4% KSt) und dem Investitionsabzug (DIC). Die Kombination kann den effektiven Steuersatz für Unternehmen, die erheblich in die Kanarischen Inseln investieren, gegen null reduzieren.'),
                ],
            },
            {
                'slug': 'igic-vs-mehrwertsteuer',
                'tag': 'Indirekte Besteuerung',
                'title': 'IGIC vs MwSt: Hauptunterschiede und Steuervorteile auf den Kanarischen Inseln',
                'desc': 'Alles über die kanarische IGIC-Steuer: Steuersätze, Unterschiede zur MwSt und Auswirkungen auf Ihr Unternehmen. Vollständiger Leitfaden 2026.',
                'keywords': 'IGIC MwSt Unterschiede Kanarische Inseln, IGIC Kanarische Inseln 2026, kanarische Steuer IGIC',
                'read_time': '6',
                'breadcrumb_label': 'IGIC vs MwSt',
                'intro': 'Eine der ersten Fragen, die sich jedes Unternehmen stellt, das auf den Kanarischen Inseln tätig ist oder sich dort niederlassen möchte, ist: <strong>Was ist der Unterschied zwischen IGIC und MwSt?</strong> Die Antwort hat sehr bedeutende steuerliche Auswirkungen.',
                'highlight': 'Die Kanarischen Inseln sind vom EU-MwSt-Gebiet ausgeschlossen. Stattdessen gilt <strong>IGIC mit 7%</strong> anstelle des allgemeinen MwSt-Satzes von 21% — ein Unterschied von 14 Prozentpunkten.',
                'sections': [
                    ('Was ist der IGIC?', 'Der <strong>Kanarische Allgemeine Indirekte Steuer (IGIC)</strong> ist die indirekte Steuer auf den Verbrauch auf den Kanarischen Inseln, geschaffen durch das Gesetz 20/1991. Wie die MwSt ist sie eine Mehrwertsteuer auf Lieferungen von Waren und Dienstleistungen durch Unternehmer auf den Kanarischen Inseln.'),
                    ('IGIC-Steuersätze 2026', 'Nullsatz (0%): Grundnahrungsmittel, Bücher, Arzneimittel.<br>Ermäßigter Satz (3%): Neubau, Wasser, Strom.<br><strong>Allgemeiner Satz (7%)</strong>: die meisten Waren und Dienstleistungen.<br>Erhöhter Satz (9,5%): Tabakerzeugnisse.'),
                    ('Hauptunterschiede zwischen IGIC und MwSt', '<h3>1. Erheblich niedrigere Sätze</h3><p>Der allgemeine IGIC-Satz beträgt <strong>7%</strong> gegenüber <strong>21%</strong> MwSt. Waren und Dienstleistungen auf den Kanarischen Inseln sind für Endverbraucher steuerlich günstiger.</p><h3>2. Kanarische Inseln außerhalb des EU-MwSt-Gebiets</h3><p>Wichtige Konsequenzen für internationale Transaktionen: Lieferungen von/nach Festlandspanien oder der EU werden als Import/Export behandelt.</p><h3>3. Einfuhr unterliegt IGIC, nicht MwSt</h3><p>Wenn ein kanarisches Unternehmen Waren importiert, unterliegt der Vorgang dem IGIC beim Eintritt in das kanarische Gebiet.</p>'),
                    ('Auswirkungen auf Unternehmen', 'Für internationale Investoren bedeutet die Niederlassung auf den Kanarischen Inseln die Arbeit mit IGIC statt MwSt. Der allgemeine Satz von 7% stellt einen Wettbewerbsvorteil bei nicht abzugsfähigen Kosten und Handelsspannen dar.'),
                ],
            },
            {
                'slug': 'gesetz-zweite-chance-kanarische-inseln',
                'tag': 'Insolvenzrecht',
                'title': 'Gesetz der zweiten Chance auf den Kanarischen Inseln: Leitfaden für Selbstständige und Privatpersonen 2026',
                'desc': 'Wie das Gesetz der zweiten Chance auf den Kanarischen Inseln funktioniert: wer es beantragen kann, welche Schulden erlassen werden und der schrittweise Ablauf.',
                'keywords': 'Gesetz zweite Chance Kanarische Inseln, Schuldenbefreiung Kanarische Inseln, Insolvenz Selbstständiger Kanarische Inseln',
                'read_time': '8',
                'breadcrumb_label': 'Gesetz der zweiten Chance',
                'intro': 'Das <strong>Gesetz der zweiten Chance</strong> ermöglicht natürlichen Personen — sowohl Privatpersonen als auch Selbstständigen — in einer Überschuldungssituation die <strong>vollständige oder teilweise Befreiung von ihren Schulden</strong> und einen wirtschaftlichen Neuanfang ohne die Last der Vergangenheit.',
                'highlight': 'Auf den Kanarischen Inseln haben wir erfolgreich Verfahren mit Schuldenbefreiungen von 30.000€ bis über 500.000€ abgewickelt. Das erste Gespräch ist kostenlos und vertraulich.',
                'sections': [
                    ('Wer kann das Gesetz der zweiten Chance beantragen?', 'Natürliche Personen (Privatpersonen), Selbstständige mit geschäftlichen Schulden, Einzelunternehmer in Insolvenz. Voraussetzungen: Natürliche Person sein, aktuelle oder drohende Zahlungsunfähigkeit, guter Glaube, keine strafrechtliche Verurteilung wegen Wirtschaftsdelikten in den letzten 10 Jahren.'),
                    ('Welche Schulden können erlassen werden?', '<h3>Erlassbare Schulden</h3><ul><li>Bankschulden (Kredite, Hypotheken, Kreditkarten)</li><li>Verbindlichkeiten gegenüber Lieferanten und Gläubigern</li><li>Sozialversicherungsschulden (bis zu bestimmten Grenzen)</li><li>Steuerschulden (bis zu bestimmten Grenzen)</li></ul><h3>Nicht erlassbare Schulden</h3><ul><li>Unterhaltspflichten (Kinder, Ehepartner)</li><li>Zivilrechtliche Haftung aus Straftaten</li><li>Strafrechtliche Geldstrafen</li></ul>'),
                    ('Der Ablauf Schritt für Schritt', '<h3>Phase 1 — Insolvenzverfahren</h3><p>Antrag auf Eröffnung des Insolvenzverfahrens beim Handelsgericht. Das Gericht bestellt einen Insolvenzverwalter, der das Vermögen und die Schulden des Schuldners inventarisiert (6–18 Monate).</p><h3>Phase 2 — Liquidation des Vermögens</h3><p>Sofern der Schuldner Vermögenswerte besitzt, werden diese zur teilweisen Befriedigung der Gläubiger verwertet. Die Familienimmobilie kann in bestimmten Fällen geschützt werden.</p><h3>Phase 3 — Befreiungsantrag (BEPI)</h3><p>Nach der Liquidation beantragt der Schuldner die Befreiung. Bei Feststellung des guten Glaubens werden die Restschulden erlassen (1–3 Monate).</p>'),
                    ('Was passiert mit dem Eigenheim?', 'In den meisten Fällen behält die Bank ihr Pfandrecht an der Hypothek, auch wenn andere Schulden erlassen werden. Wenn der Schuldner die Hypothek weiter bedienen kann, kann er das Eigenheim behalten. Rechtliche Strategien müssen fallweise analysiert werden.'),
                ],
            },
            {
                'slug': 'steuerregime-kanarische-inseln-internationale-unternehmer',
                'tag': 'International',
                'title': 'Kanarisches Steuerregime für internationale Unternehmer: Vorteile und Niederlassung',
                'desc': 'Leitfaden für ausländische Unternehmer und Firmen, die sich auf den Kanarischen Inseln niederlassen möchten: REF-Vorteile, ZEC, IGIC, Anforderungen. Beratung auf Deutsch.',
                'keywords': 'Unternehmen gründen Kanarische Inseln Ausland, Steuervorteile Kanarische Inseln internationale Unternehmen, ZEC Kanarische Inseln ausländische Firma',
                'read_time': '9',
                'breadcrumb_label': 'REF für Internationale',
                'intro': 'Die Kanarischen Inseln haben sich zu einem der attraktivsten Ziele in Europa für internationale Unternehmer, digitale Nomaden und ausländische Investoren entwickelt. Der Hauptgrund: das <strong>Wirtschafts- und Steuerregime der Kanarischen Inseln (REF)</strong> bietet einzigartige Steuervorteile innerhalb der EU.',
                'highlight': 'Wir beraten auf <strong>Spanisch, Englisch, Deutsch, Italienisch und Französisch</strong>. Wenn Sie eine Niederlassung auf den Kanarischen Inseln planen, begleiten wir Sie von Anfang an.',
                'sections': [
                    ('Warum die Kanarischen Inseln für internationale Unternehmer?', '<ul><li><strong>EU-Territorium</strong>: voller Zugang zum europäischen Binnenmarkt, Doppelbesteuerungsabkommen, Kapitalverkehrsfreiheit</li><li><strong>Sondersteuersystem</strong>: 4% KSt (ZEC), 7% IGIC, eigene Abzüge und Anreize</li><li><strong>Klima und Lebensqualität</strong>: eines der besten Klimate der Welt, moderne Infrastruktur</li><li><strong>Rechtssicherheit</strong>: spanisches Rechtssystem (europäische Rechtssicherheit)</li><li><strong>Zeitzone GMT+0</strong>: ideal für die gleichzeitige Arbeit mit Europa, Amerika und Afrika</li></ul>'),
                    ('Hauptsteuervorteile des REF', '<h3>1. ZEC — 4% Körperschaftsteuer</h3><p>Mindestinvestition ab 50.000€ auf kleineren Inseln, mindestens 3–5 Arbeitsplätze, effektive Tätigkeit erforderlich.</p><h3>2. IGIC mit 7% statt 21% MwSt</h3><p>Direkter Wettbewerbsvorteil bei Preisen für Endkunden.</p><h3>3. RIC — bis zu 90% Steuerreduzierung</h3><p>Die Investitionsrücklage reduziert die Bemessungsgrundlage um bis zu 90% der reinvestierten Gewinne.</p>'),
                    ('Wie man sich auf den Kanarischen Inseln niederlässt', '<h3>Schritt 1 — Rechtsform wählen</h3><p>Die häufigste Option für internationale Investoren ist die <strong>Sociedad de Responsabilidad Limitada (S.L.)</strong>: Mindestkapital 1€, beschränkte Haftung.</p><h3>Schritt 2 — NIE und NIF erhalten</h3><p>Ausländische Gesellschafter und Geschäftsführer benötigen eine Ausländeridentifikationsnummer (NIE).</p><h3>Schritt 3 — Gesellschaft gründen</h3><p>Der gesamte Prozess dauert <strong>2–4 Wochen</strong>: Firmenname, Bankkonto, Notarakt, Handelsregistereintragung, Steuerregistrierung.</p><h3>Schritt 4 — ZEC-Status beantragen</h3><p>Falls die Voraussetzungen erfüllt sind, kann die ZEC-Registrierung beantragt werden (ca. 3 Monate).</p>'),
                    ('Digitale Nomaden und das Beckham-Gesetz', 'Spanien verfügt seit 2023 über das <strong>Visum für digitale Nomaden</strong>, das Nicht-EU-Fernarbeitern einen Aufenthalt von bis zu 5 Jahren ermöglicht. Das <strong>Beckham-Gesetz</strong> (Sonderregelung für zuziehende Arbeitnehmer) erlaubt neuen Steuerresidenten, 6 Jahre lang einen pauschalen IRPF-Satz von 24% auf Einkünfte bis 600.000€/Jahr zu zahlen.'),
                ],
            },
        ],
    },
    'it': {
        'blog_title': 'Blog — Fiscalidad Canaria | Articoli su REF, ZEC, RIC e IGIC',
        'blog_desc': 'Articoli e guide sul Regime Economico e Fiscale delle Canarie: ZEC, RIC, IGIC, Legge della Seconda Opportunità e fiscalità per imprenditori internazionali.',
        'blog_h1': 'Blog — Fiscalidad Canaria',
        'blog_sub': 'Guide e articoli sul Regime Economico e Fiscale delle Canarie, redatti dai nostri specialisti.',
        'blog_tag': 'Conoscenza fiscale',
        'nav_back': '← Home',
        'nav_cta': 'Consulenza gratuita',
        'read_more': 'Leggi l\'articolo →',
        'footer': '© 2026 Fiscalidad Canaria',
        'free_cta_title': 'Prima consulenza gratuita',
        'free_cta_desc': 'Analizziamo la vostra situazione fiscale senza impegno. Parliamo italiano.',
        'free_cta_btn': 'Consulenza gratuita →',
        'by': 'Di',
        'date': 'Luglio 2026',
        'min_read': 'min di lettura',
        'articles': [
            {
                'slug': 'zec-zona-speciale-canaria',
                'tag': 'Regime Fiscale Canario',
                'title': 'ZEC Zona Speciale Canaria: cos\'è e come funziona nel 2026',
                'desc': 'Guida completa sulla Zona Speciale Canaria (ZEC): requisiti, aliquota del 4% sull\'imposta sulle società e come registrarsi. Aggiornata 2026.',
                'keywords': 'ZEC zona speciale canaria, zona speciale canaria 2026, imposta società 4% Canarie, ZEC requisiti',
                'read_time': '8',
                'breadcrumb_label': 'ZEC Zona Speciale Canaria',
                'intro': 'La <strong>Zona Speciale Canaria (ZEC)</strong> è uno degli strumenti fiscali più potenti disponibili nell\'Unione Europea. Creata nel quadro del Regime Economico e Fiscale delle Canarie, consente alle aziende registrate di pagare solo il <strong>4% di imposta sulle società</strong>, rispetto all\'aliquota generale del 25% nella Spagna continentale.',
                'highlight': 'La ZEC offre un\'<strong>aliquota del 4% sull\'imposta sulle società</strong> — 21 punti percentuali al di sotto dell\'aliquota generale spagnola. Per un\'azienda con 500.000€ di utile, ciò significa un risparmio di oltre 100.000€ all\'anno.',
                'sections': [
                    ('Cos\'è la ZEC?', 'La ZEC è stata creata dalla Legge 19/1994 ed è autorizzata dall\'Unione Europea come aiuto di Stato compatibile con il mercato interno. Il suo obiettivo è promuovere lo sviluppo economico delle Isole Canarie e compensare i costi dell\'ultraperifericitá.'),
                    ('Principali vantaggi fiscali della ZEC', '<h3>Aliquota del 4% sull\'imposta sulle società</h3><p>Il vantaggio principale. Mentre l\'aliquota generale in Spagna è del 25%, le entità ZEC pagano il 4% sulla base imponibile ZEC.</p><h3>Esenzione IGIC per determinate operazioni</h3><p>Le forniture di beni e servizi tra entità ZEC sono esenti dall\'imposta indiretta canaria (IGIC).</p>'),
                    ('Requisiti per la registrazione ZEC', '<h3>Attività consentite</h3><p>Tecnologia, industria, commercio, servizi finanziari (con limitazioni), R&S, consulenza, logistica.</p><h3>Investimento minimo</h3><p>100.000€ a Gran Canaria e Tenerife; 50.000€ nelle isole minori.</p><h3>Creazione di posti di lavoro</h3><p>Almeno 5 posti di lavoro entro i primi sei mesi (3 nelle isole minori).</p><h3>Attività effettiva</h3><p>Le operazioni devono essere svolte materialmente ed effettivamente nel territorio ZEC.</p>'),
                    ('Chi può beneficiare della ZEC?', 'Particolarmente attraente per: <ul><li><strong>Aziende tecnologiche e digitali</strong> che cercano una base europea con bassa tassazione</li><li><strong>Investitori internazionali</strong> che vogliono stabilirsi nell\'UE</li><li><strong>Gruppi aziendali</strong> che vogliono ottimizzare la struttura fiscale internazionale</li><li><strong>Startup in crescita</strong></li></ul>'),
                ],
            },
            {
                'slug': 'ric-riserva-investimenti-canarie',
                'tag': 'Regime Fiscale Canario',
                'title': 'RIC Riserva per Investimenti nelle Canarie: guida completa 2026',
                'desc': 'Come ridurre l\'imposta sulle società fino al 90% con la Riserva per Investimenti nelle Canarie (RIC). Requisiti, investimenti validi ed esempio pratico di risparmio.',
                'keywords': 'RIC riserva investimenti Canarie, ridurre imposta società Canarie, RIC Canarie 2026',
                'read_time': '7',
                'breadcrumb_label': 'RIC Riserva Investimenti',
                'intro': 'La <strong>Riserva per Investimenti nelle Canarie (RIC)</strong> è uno degli incentivi fiscali più potenti del sistema tributario spagnolo. Consente alle aziende canarie di ridurre la <strong>base imponibile dell\'imposta sulle società fino al 90%</strong> degli utili non distribuiti, purché tali importi vengano investiti nelle Isole Canarie.',
                'highlight': 'Un\'azienda con 200.000€ di utile netto può dotare la RIC di 180.000€ (90%) e pagare l\'imposta solo su 20.000€. Il risparmio fiscale rispetto al regime generale può superare i 40.000€ annui.',
                'sections': [
                    ('Cos\'è la RIC?', 'La RIC è disciplinata dall\'articolo 27 della Legge 19/1994. È una dotazione contabile che le aziende possono effettuare a valere sugli utili non distribuiti, riducendo direttamente la base imponibile dell\'imposta sulle società nell\'anno di dotazione.'),
                    ('Come funziona la RIC', '<h3>1. Dotazione della riserva</h3><p>Nell\'anno in cui si conseguono gli utili, la riserva può essere dotata fino al <strong>90% degli utili non distribuiti</strong>.</p><h3>2. Termine di materializzazione</h3><p>Gli importi dotati devono essere investiti entro <strong>3 anni</strong> dalla chiusura dell\'esercizio.</p><h3>3. Mantenimento dell\'investimento</h3><p>I beni devono rimanere nel patrimonio aziendale per almeno <strong>5 anni</strong>.</p>'),
                    ('In cosa si può materializzare la RIC?', '<h3>Investimenti in attività fisse (Gruppo A)</h3><ul><li>Nuove attività fisse nelle Canarie (macchinari, informatica, veicoli)</li><li>Costruzione o ristrutturazione di immobili aziendali</li><li>Partecipazioni in aziende con attività nelle Canarie</li></ul><h3>Debito pubblico canario (Gruppo B)</h3><ul><li>Massimo 50% della dotazione totale della RIC</li></ul>'),
                    ('Compatibilità con altri incentivi', 'La RIC è compatibile con ZEC (4% imposta società) e con la Deduzione per Investimenti (DIC). La combinazione può ridurre l\'aliquota fiscale effettiva quasi a zero per le aziende che investono significativamente nelle Canarie.'),
                ],
            },
            {
                'slug': 'igic-vs-iva-canarie',
                'tag': 'Fiscalità Indiretta',
                'title': 'IGIC vs IVA: differenze chiave e vantaggi fiscali nelle Isole Canarie',
                'desc': 'Tutto sull\'IGIC canario: aliquote, differenze dall\'IVA e come influisce sulla vostra azienda. Guida completa 2026.',
                'keywords': 'IGIC IVA differenze Canarie, IGIC Canarie 2026, imposta indiretta canaria',
                'read_time': '6',
                'breadcrumb_label': 'IGIC vs IVA',
                'intro': 'Una delle prime domande che si pone qualsiasi azienda che opera — o pensa di stabilirsi — nelle Isole Canarie è: <strong>qual è la differenza tra IGIC e IVA?</strong> La risposta ha implicazioni fiscali molto significative.',
                'highlight': 'Le Isole Canarie sono escluse dal territorio IVA dell\'UE. Si applica invece l\'<strong>IGIC al 7%</strong> anziché l\'aliquota IVA generale del 21% — una differenza di 14 punti percentuali.',
                'sections': [
                    ('Cos\'è l\'IGIC?', 'L\'<strong>Imposta Generale Indiretta Canaria (IGIC)</strong> è l\'imposta indiretta che grava sul consumo nelle Isole Canarie, creata dalla Legge 20/1991. Come l\'IVA, è un\'imposta sul valore aggiunto sulle forniture di beni e servizi da parte di imprenditori nelle Canarie.'),
                    ('Aliquote IGIC nel 2026', 'Aliquota zero (0%): prodotti alimentari di base, libri, medicinali.<br>Aliquota ridotta (3%): abitazione nuova, acqua, energia elettrica.<br><strong>Aliquota generale (7%)</strong>: la maggior parte di beni e servizi.<br>Aliquota incrementata (9,5%): tabacco.'),
                    ('Principali differenze tra IGIC e IVA', '<h3>1. Aliquote significativamente più basse</h3><p>L\'aliquota generale IGIC è del <strong>7%</strong> rispetto al <strong>21%</strong> dell\'IVA. Beni e servizi nelle Canarie sono fiscalmente più economici.</p><h3>2. Le Canarie fuori dal territorio IVA UE</h3><p>Importanti conseguenze per le operazioni internazionali: le forniture da/verso la Spagna continentale o l\'UE sono trattate come import/export.</p><h3>3. L\'importazione è soggetta a IGIC, non a IVA</h3><p>Quando un\'azienda canaria importa beni, l\'operazione è soggetta a IGIC all\'entrata nel territorio canario.</p>'),
                    ('Implicazioni per le aziende', 'Per gli investitori internazionali, stabilirsi nelle Canarie significa lavorare con l\'IGIC invece dell\'IVA. L\'aliquota generale del 7% rappresenta un vantaggio competitivo nei costi non recuperabili e nei margini commerciali.'),
                ],
            },
            {
                'slug': 'legge-seconda-opportunita-canarie',
                'tag': 'Diritto Concorsuale',
                'title': 'Legge della Seconda Opportunità nelle Canarie: guida per lavoratori autonomi e privati 2026',
                'desc': 'Come funziona la Legge della Seconda Opportunità nelle Canarie: chi può richiederla, quali debiti vengono cancellati e il processo passo dopo passo.',
                'keywords': 'legge seconda opportunità Canarie, cancellazione debiti Canarie, insolvenza lavoratori autonomi Canarie',
                'read_time': '8',
                'breadcrumb_label': 'Legge della Seconda Opportunità',
                'intro': 'La <strong>Legge della Seconda Opportunità</strong> consente alle persone fisiche — sia privati che lavoratori autonomi — in situazione di sovraindebitamento di ottenere la <strong>cancellazione totale o parziale dei propri debiti</strong> e ricominciare senza i pesi del passato.',
                'highlight': 'Nelle Canarie abbiamo gestito con successo procedure con cancellazioni di debiti da 30.000€ a oltre 500.000€. La prima consulenza è gratuita e riservata.',
                'sections': [
                    ('Chi può accedere alla Legge della Seconda Opportunità?', 'Persone fisiche (privati), lavoratori autonomi con debiti derivanti dall\'attività, imprenditori individuali in stato di insolvenza. Requisiti: essere persona fisica, trovarsi in stato di insolvenza attuale o imminente, aver agito in buona fede, nessuna condanna per reati economici negli ultimi 10 anni.'),
                    ('Quali debiti possono essere cancellati?', '<h3>Debiti che SÌ vengono cancellati</h3><ul><li>Debiti con banche (prestiti, mutui, carte di credito)</li><li>Debiti con fornitori e creditori commerciali</li><li>Debiti con la Previdenza Sociale (entro certi limiti)</li><li>Debiti fiscali (entro certi limiti)</li></ul><h3>Debiti che NON vengono cancellati</h3><ul><li>Obblighi alimentari (figli, coniuge)</li><li>Responsabilità civile derivante da reato</li><li>Sanzioni penali</li></ul>'),
                    ('Il processo passo dopo passo', '<h3>Fase 1 — Procedura concorsuale</h3><p>Presentazione dell\'istanza di fallimento presso il Tribunale Commerciale. Il giudice nomina un commissario giudiziale che inventarierà i beni e i debiti del debitore (6–18 mesi).</p><h3>Fase 2 — Liquidazione del patrimonio</h3><p>Se il debitore ha beni, questi vengono liquidati per pagare parzialmente i creditori. L\'abitazione principale può essere protetta in certi casi.</p><h3>Fase 3 — Domanda di esdebitazione (BEPI)</h3><p>Dopo la liquidazione, il debitore chiede l\'esdebitazione. Se il giudice accerta la buona fede, i debiti residui vengono cancellati (1–3 mesi).</p>'),
                    ('Cosa succede con l\'abitazione principale?', 'Nella maggior parte dei casi, la banca mantiene il diritto reale di garanzia (ipoteca) anche se il debitore ottiene l\'esdebitazione degli altri debiti. Se il debitore può continuare a pagare il mutuo, può conservare l\'abitazione. Le strategie giuridiche vanno analizzate caso per caso.'),
                ],
            },
            {
                'slug': 'regime-fiscale-canario-imprenditori-internazionali',
                'tag': 'Internazionale',
                'title': 'Regime Fiscale Canario per imprenditori internazionali: vantaggi e come stabilirsi',
                'desc': 'Guida per imprenditori e aziende straniere che vogliono stabilirsi nelle Canarie: vantaggi REF, ZEC, IGIC, requisiti e processo. Consulenza in italiano.',
                'keywords': 'stabilirsi Canarie stranieri, vantaggi fiscali Canarie aziende internazionali, ZEC Canarie azienda straniera',
                'read_time': '9',
                'breadcrumb_label': 'REF per internazionali',
                'intro': 'Le Isole Canarie sono diventate una delle destinazioni più attraenti d\'Europa per imprenditori internazionali, nomadi digitali e investitori stranieri. Il motivo principale: il <strong>Regime Economico e Fiscale delle Canarie (REF)</strong> offre vantaggi fiscali unici all\'interno dell\'Unione Europea.',
                'highlight': 'Offriamo consulenza in <strong>spagnolo, inglese, tedesco, italiano e francese</strong>. Se stai pensando di stabilirti nelle Canarie, ti guidiamo in tutto il processo dall\'inizio.',
                'sections': [
                    ('Perché le Canarie per gli imprenditori internazionali?', '<ul><li><strong>Territorio UE</strong>: pieno accesso al mercato unico europeo, convenzioni contro la doppia imposizione</li><li><strong>Regime fiscale speciale</strong>: 4% imposta sulle società (ZEC), IGIC 7%, deduzioni proprie</li><li><strong>Clima e qualità della vita</strong>: uno dei migliori climi al mondo, infrastrutture moderne</li><li><strong>Stabilità giuridica</strong>: sistema legale spagnolo (certezza giuridica europea)</li><li><strong>Fuso orario GMT+0</strong>: ideale per lavorare con Europa, America e Africa</li></ul>'),
                    ('Principali vantaggi fiscali del REF', '<h3>1. ZEC — 4% imposta sulle società</h3><p>Investimento minimo da 50.000€ nelle isole minori, almeno 3–5 posti di lavoro, attività effettiva richiesta.</p><h3>2. IGIC al 7% invece del 21% IVA</h3><p>Vantaggio competitivo diretto nei prezzi per i clienti finali.</p><h3>3. RIC — riduzione fino al 90% della base imponibile</h3><p>La riserva per investimenti riduce la base imponibile fino al 90% degli utili reinvestiti.</p>'),
                    ('Come stabilirsi nelle Canarie dall\'estero', '<h3>Passo 1 — Scegliere la struttura giuridica</h3><p>L\'opzione più comune per gli investitori internazionali è la <strong>Sociedad de Responsabilidad Limitada (S.L.)</strong>: capitale minimo 1€, responsabilità limitata.</p><h3>Passo 2 — Ottenere NIE e NIF</h3><p>I soci e amministratori stranieri devono ottenere il Numero di Identificazione degli Stranieri (NIE).</p><h3>Passo 3 — Costituire la società</h3><p>Il processo completo richiede <strong>2–4 settimane</strong>: denominazione, conto bancario, atto notarile, iscrizione al Registro delle Imprese, registrazione fiscale.</p><h3>Passo 4 — Richiedere lo status ZEC</h3><p>Se i requisiti sono soddisfatti, si può richiedere l\'iscrizione al Registro ZEC (circa 3 mesi).</p>'),
                    ('Nomadi digitali e Legge Beckham', 'La Spagna dispone dal 2023 del <strong>Visto per nomadi digitali</strong>, che permette ai lavoratori remoti extra-UE di risiedere in Spagna fino a 5 anni. La <strong>Legge Beckham</strong> consente ai nuovi residenti fiscali di pagare un\'aliquota fissa del 24% sull\'IRPF per 6 anni su redditi fino a 600.000€/anno.'),
                ],
            },
        ],
    },
    'fr': {
        'blog_title': 'Blog — Fiscalidad Canaria | Articles sur le REF, ZEC, RIC et IGIC',
        'blog_desc': 'Articles et guides sur le Régime Économique et Fiscal des Canaries : ZEC, RIC, IGIC, Loi sur la Seconde Chance et fiscalité pour entrepreneurs internationaux.',
        'blog_h1': 'Blog — Fiscalidad Canaria',
        'blog_sub': 'Guides et articles sur le Régime Économique et Fiscal des Canaries, rédigés par nos spécialistes.',
        'blog_tag': 'Connaissance fiscale',
        'nav_back': '← Accueil',
        'nav_cta': 'Consultation gratuite',
        'read_more': 'Lire l\'article →',
        'footer': '© 2026 Fiscalidad Canaria',
        'free_cta_title': 'Première consultation gratuite',
        'free_cta_desc': 'Analysons votre situation fiscale sans engagement. Nous parlons français.',
        'free_cta_btn': 'Consultation gratuite →',
        'by': 'Par',
        'date': 'Juillet 2026',
        'min_read': 'min de lecture',
        'articles': [
            {
                'slug': 'zec-zone-speciale-canarienne',
                'tag': 'Régime Fiscal Canarien',
                'title': 'ZEC Zone Spéciale Canarienne : qu\'est-ce que c\'est et comment ça fonctionne en 2026',
                'desc': 'Guide complet sur la Zone Spéciale Canarienne (ZEC) : conditions, taux de 4% d\'impôt sur les sociétés et procédure d\'inscription. Mis à jour 2026.',
                'keywords': 'ZEC zone spéciale canarienne, zone spéciale canarienne 2026, impôt sociétés 4% Canaries, ZEC conditions',
                'read_time': '8',
                'breadcrumb_label': 'ZEC Zone Spéciale Canarienne',
                'intro': 'La <strong>Zone Spéciale Canarienne (ZEC)</strong> est l\'un des instruments fiscaux les plus puissants disponibles dans l\'Union Européenne. Créée dans le cadre du Régime Économique et Fiscal des Canaries, elle permet aux sociétés enregistrées de payer seulement <strong>4% d\'impôt sur les sociétés</strong>, contre le taux général de 25% en Espagne continentale.',
                'highlight': 'La ZEC offre un <strong>taux d\'IS de 4%</strong> — 21 points de pourcentage en dessous du taux général espagnol. Pour une entreprise réalisant 500 000€ de bénéfice, cela représente plus de 100 000€ d\'économies annuelles.',
                'sections': [
                    ('Qu\'est-ce que la ZEC ?', 'La ZEC a été créée par la Loi 19/1994 et est autorisée par l\'Union Européenne en tant qu\'aide d\'État compatible avec le marché intérieur. Son objectif est de promouvoir le développement économique des Îles Canaries et de compenser les surcoûts liés à l\'ultrapériphéricité.'),
                    ('Principaux avantages fiscaux de la ZEC', '<h3>Taux d\'IS de 4%</h3><p>L\'avantage principal. Alors que le taux général en Espagne est de 25%, les entités ZEC paient 4% sur la base imposable ZEC.</p><h3>Exonération d\'IGIC pour certaines opérations</h3><p>Les livraisons de biens et prestations de services entre entités ZEC sont exonérées de la taxe indirecte canarienne (IGIC).</p>'),
                    ('Conditions pour s\'inscrire dans la ZEC', '<h3>Activités autorisées</h3><p>Technologie, industrie, commerce, services financiers (avec restrictions), R&D, conseil, logistique.</p><h3>Investissement minimum</h3><p>100 000€ à Grande Canarie et Tenerife ; 50 000€ dans les îles mineures.</p><h3>Création d\'emplois</h3><p>Au moins 5 emplois dans les six premiers mois (3 dans les îles mineures).</p><h3>Activité effective</h3><p>Les opérations doivent être réalisées matériellement et effectivement dans le territoire ZEC.</p>'),
                    ('Qui peut bénéficier de la ZEC ?', 'Particulièrement attractif pour : <ul><li><strong>Entreprises technologiques et numériques</strong> cherchant une base européenne à faible imposition</li><li><strong>Investisseurs internationaux</strong> souhaitant s\'établir dans l\'UE</li><li><strong>Groupes d\'entreprises</strong> voulant optimiser leur structure fiscale internationale</li><li><strong>Startups en croissance</strong></li></ul>'),
                ],
            },
            {
                'slug': 'ric-reserve-investissements-canaries',
                'tag': 'Régime Fiscal Canarien',
                'title': 'RIC Réserve pour Investissements aux Canaries : guide complet 2026',
                'desc': 'Comment réduire l\'impôt sur les sociétés jusqu\'à 90% avec la Réserve pour Investissements aux Canaries (RIC). Conditions, investissements valides et exemple pratique d\'économie.',
                'keywords': 'RIC réserve investissements Canaries, réduire impôt sociétés Canaries, RIC Canaries 2026',
                'read_time': '7',
                'breadcrumb_label': 'RIC Réserve Investissements',
                'intro': 'La <strong>Réserve pour Investissements aux Canaries (RIC)</strong> est l\'un des incentifs fiscaux les plus puissants du système fiscal espagnol. Elle permet aux sociétés canariennes de réduire leur <strong>base imposable de l\'IS jusqu\'à 90%</strong> des bénéfices non distribués, à condition d\'investir ces montants aux Îles Canaries.',
                'highlight': 'Une entreprise réalisant 200 000€ de bénéfice net peut doter la RIC de 180 000€ (90%) et payer l\'impôt uniquement sur 20 000€. L\'économie fiscale par rapport au régime général peut dépasser 40 000€ par an.',
                'sections': [
                    ('Qu\'est-ce que la RIC ?', 'La RIC est régie par l\'article 27 de la Loi 19/1994. Il s\'agit d\'une dotation comptable que les sociétés peuvent effectuer sur leurs bénéfices non distribués, réduisant directement la base imposable de l\'IS dans l\'exercice de dotation.'),
                    ('Comment fonctionne la RIC', '<h3>1. Dotation de la réserve</h3><p>Dans l\'exercice où les bénéfices sont réalisés, la réserve peut être dotée jusqu\'à <strong>90% des bénéfices non distribués</strong>.</p><h3>2. Délai de matérialisation</h3><p>Les montants dotés doivent être investis dans les <strong>3 ans</strong> suivant la clôture de l\'exercice.</p><h3>3. Maintien de l\'investissement</h3><p>Les actifs doivent rester dans le patrimoine de l\'entreprise pendant au moins <strong>5 ans</strong>.</p>'),
                    ('Dans quoi peut-on matérialiser la RIC ?', '<h3>Investissements en actifs fixes (Groupe A)</h3><ul><li>Nouveaux actifs fixes aux Canaries (machines, informatique, véhicules)</li><li>Construction ou réhabilitation d\'immeubles à usage professionnel</li><li>Participations dans des entités exerçant une activité aux Canaries</li></ul><h3>Dette publique canarienne (Groupe B)</h3><ul><li>Maximum 50% de la dotation totale RIC</li></ul>'),
                    ('Compatibilité avec d\'autres incentifs', 'La RIC est compatible avec la ZEC (IS à 4%) et la Déduction pour Investissements (DIC). La combinaison peut ramener le taux effectif d\'imposition near zero pour les entreprises investissant significativement aux Canaries.'),
                ],
            },
            {
                'slug': 'igic-vs-tva',
                'tag': 'Fiscalité Indirecte',
                'title': 'IGIC vs TVA : différences clés et avantages fiscaux aux Îles Canaries',
                'desc': 'Tout sur l\'IGIC canarien : taux, différences avec la TVA et impact sur votre entreprise. Guide complet 2026.',
                'keywords': 'IGIC TVA différences Canaries, IGIC Canaries 2026, taxe indirecte canarienne',
                'read_time': '6',
                'breadcrumb_label': 'IGIC vs TVA',
                'intro': 'L\'une des premières questions que se pose toute entreprise opérant — ou envisageant de s\'établir — aux Îles Canaries est : <strong>quelle est la différence entre l\'IGIC et la TVA ?</strong> La réponse a des implications fiscales très importantes.',
                'highlight': 'Les Îles Canaries sont exclues du territoire TVA de l\'UE. L\'<strong>IGIC à 7%</strong> s\'applique à la place du taux général de TVA de 21% — une différence de 14 points de pourcentage.',
                'sections': [
                    ('Qu\'est-ce que l\'IGIC ?', 'L\'<strong>Impôt Général Indirect Canarien (IGIC)</strong> est l\'impôt indirect sur la consommation aux Îles Canaries, créé par la Loi 20/1991. Comme la TVA, c\'est un impôt sur la valeur ajoutée prélevé sur les livraisons de biens et prestations de services par des professionnels aux Canaries.'),
                    ('Taux IGIC en 2026', 'Taux zéro (0%) : produits alimentaires de base, livres, médicaments.<br>Taux réduit (3%) : logement neuf, eau, électricité.<br><strong>Taux général (7%)</strong> : la plupart des biens et services.<br>Taux majoré (9,5%) : tabac.'),
                    ('Principales différences entre IGIC et TVA', '<h3>1. Taux significativement plus bas</h3><p>Le taux général de l\'IGIC est de <strong>7%</strong> contre <strong>21%</strong> de TVA. Les biens et services aux Canaries sont fiscalement moins chers.</p><h3>2. Canaries hors du territoire TVA de l\'UE</h3><p>Conséquences importantes pour les opérations internationales : les livraisons depuis/vers l\'Espagne continentale ou l\'UE sont traitées comme des importations/exportations.</p><h3>3. L\'importation est soumise à l\'IGIC, pas à la TVA</h3><p>Quand une société canarienne importe des biens, l\'opération est soumise à l\'IGIC à l\'entrée dans le territoire canarien.</p>'),
                    ('Implications pour les entreprises', 'Pour les investisseurs internationaux, s\'établir aux Canaries implique de travailler avec l\'IGIC plutôt que la TVA. Le taux général de 7% représente un avantage concurrentiel dans les coûts non récupérables et les marges commerciales.'),
                ],
            },
            {
                'slug': 'loi-seconde-chance-canaries',
                'tag': 'Droit des procédures collectives',
                'title': 'Loi sur la Seconde Chance aux Canaries : guide pour indépendants et particuliers 2026',
                'desc': 'Comment fonctionne la Loi sur la Seconde Chance aux Canaries : qui peut la demander, quelles dettes sont annulées et le processus étape par étape.',
                'keywords': 'loi seconde chance Canaries, annulation dettes Canaries, insolvabilité indépendants Canaries',
                'read_time': '8',
                'breadcrumb_label': 'Loi sur la Seconde Chance',
                'intro': 'La <strong>Loi sur la Seconde Chance</strong> permet aux personnes physiques — aussi bien aux particuliers qu\'aux travailleurs indépendants — en situation de surendettement d\'obtenir l\'<strong>annulation totale ou partielle de leurs dettes</strong> et de repartir sur de nouvelles bases sans les charges du passé.',
                'highlight': 'Aux Canaries, nous avons traité avec succès des procédures avec des annulations de dettes allant de 30 000€ à plus de 500 000€. La première consultation est gratuite et confidentielle.',
                'sections': [
                    ('Qui peut bénéficier de la Loi sur la Seconde Chance ?', 'Personnes physiques (particuliers), travailleurs indépendants avec des dettes liées à leur activité, entrepreneurs individuels en état d\'insolvabilité. Conditions : être une personne physique, être en état d\'insolvabilité actuelle ou imminente, avoir agi de bonne foi, pas de condamnation pénale pour délits économiques dans les 10 dernières années.'),
                    ('Quelles dettes peuvent être annulées ?', '<h3>Dettes qui PEUVENT être annulées</h3><ul><li>Dettes bancaires (prêts, hypothèques, cartes de crédit)</li><li>Dettes envers fournisseurs et créanciers commerciaux</li><li>Dettes envers la Sécurité Sociale (dans certaines limites)</li><li>Dettes fiscales (dans certaines limites)</li></ul><h3>Dettes qui NE PEUVENT PAS être annulées</h3><ul><li>Pensions alimentaires (enfants, conjoint)</li><li>Responsabilité civile découlant d\'une infraction pénale</li><li>Amendes pénales</li></ul>'),
                    ('Le processus étape par étape', '<h3>Phase 1 — Procédure collective</h3><p>Dépôt d\'une demande de faillite auprès du Tribunal de Commerce. Le juge nomme un mandataire judiciaire chargé d\'inventorier les actifs et passifs du débiteur (6–18 mois).</p><h3>Phase 2 — Liquidation du patrimoine</h3><p>Si le débiteur possède des actifs, ceux-ci sont liquidés pour rembourser partiellement les créanciers. La résidence principale peut être protégée dans certains cas.</p><h3>Phase 3 — Demande d\'exonération (BEPI)</h3><p>Après la liquidation, le débiteur demande l\'exonération. Si le juge constate la bonne foi, les dettes résiduelles sont annulées (1–3 mois).</p>'),
                    ('Que se passe-t-il avec la résidence principale ?', 'Dans la plupart des cas, la banque conserve son droit réel de garantie (hypothèque) même si le débiteur obtient l\'exonération d\'autres dettes. Si le débiteur peut continuer à rembourser l\'hypothèque, il peut conserver son logement. Les stratégies juridiques doivent être analysées au cas par cas.'),
                ],
            },
            {
                'slug': 'regime-fiscal-canarien-entrepreneurs-internationaux',
                'tag': 'International',
                'title': 'Régime Fiscal Canarien pour entrepreneurs internationaux : avantages et comment s\'établir',
                'desc': 'Guide pour entrepreneurs et sociétés étrangers voulant s\'installer aux Canaries : avantages REF, ZEC, IGIC, conditions et processus. Conseil en français.',
                'keywords': 'créer entreprise Canaries étranger, avantages fiscaux Canaries sociétés internationales, ZEC Canaries société étrangère',
                'read_time': '9',
                'breadcrumb_label': 'REF pour les internationaux',
                'intro': 'Les Îles Canaries sont devenues l\'une des destinations les plus attractives d\'Europe pour les entrepreneurs internationaux, les nomades numériques et les investisseurs étrangers. La raison principale : le <strong>Régime Économique et Fiscal des Canaries (REF)</strong> offre des avantages fiscaux uniques au sein de l\'Union Européenne.',
                'highlight': 'Nous conseillons en <strong>espagnol, anglais, allemand, italien et français</strong>. Si vous envisagez de vous établir aux Canaries, nous vous accompagnons dans l\'ensemble du processus.',
                'sections': [
                    ('Pourquoi les Canaries pour les entrepreneurs internationaux ?', '<ul><li><strong>Territoire UE</strong> : accès complet au marché unique européen, conventions de double imposition</li><li><strong>Régime fiscal spécial</strong> : IS à 4% (ZEC), IGIC à 7%, déductions propres</li><li><strong>Climat et qualité de vie</strong> : l\'un des meilleurs climats au monde, infrastructures modernes</li><li><strong>Stabilité juridique</strong> : système juridique espagnol (sécurité juridique européenne)</li><li><strong>Fuseau horaire GMT+0</strong> : idéal pour travailler avec l\'Europe, l\'Amérique et l\'Afrique</li></ul>'),
                    ('Principaux avantages fiscaux du REF', '<h3>1. ZEC — IS à 4%</h3><p>Investissement minimum à partir de 50 000€ dans les îles mineures, au moins 3–5 emplois, activité effective requise.</p><h3>2. IGIC à 7% au lieu de TVA à 21%</h3><p>Avantage concurrentiel direct sur les prix pour les clients finaux.</p><h3>3. RIC — réduction jusqu\'à 90% de la base imposable</h3><p>La réserve pour investissements réduit la base imposable jusqu\'à 90% des bénéfices réinvestis.</p>'),
                    ('Comment s\'établir aux Canaries depuis l\'étranger', '<h3>Étape 1 — Choisir la structure juridique</h3><p>L\'option la plus courante pour les investisseurs internationaux est la <strong>Sociedad de Responsabilidad Limitada (S.L.)</strong> : capital minimum de 1€, responsabilité limitée.</p><h3>Étape 2 — Obtenir NIE et NIF</h3><p>Les associés et dirigeants étrangers doivent obtenir un Numéro d\'Identification des Étrangers (NIE).</p><h3>Étape 3 — Constituer la société</h3><p>Le processus complet prend <strong>2–4 semaines</strong> : dénomination sociale, compte bancaire, acte notarié, inscription au Registre du Commerce, enregistrement fiscal.</p><h3>Étape 4 — Demander le statut ZEC</h3><p>Si les conditions sont remplies, l\'inscription au Registre ZEC peut être demandée (environ 3 mois).</p>'),
                    ('Nomades numériques et Loi Beckham', 'L\'Espagne dispose depuis 2023 du <strong>Visa Nomade Numérique</strong>, permettant aux télétravailleurs non communautaires de résider en Espagne jusqu\'à 5 ans. La <strong>Loi Beckham</strong> (Régime spécial des travailleurs impatriés) permet aux nouveaux résidents fiscaux de payer un taux fixe de 24% d\'IRPF pendant 6 ans sur des revenus jusqu\'à 600 000€/an.'),
                ],
            },
        ],
    },
}

CSS = """
*,*::before,*::after{margin:0;padding:0;box-sizing:border-box}
:root{--bg:#04060d;--gold:#c9a84c;--text:#f0ede8;--muted:#6a7d9a;--border:rgba(201,168,76,0.12)}
html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--text);font-family:'Inter',sans-serif;overflow-x:hidden;line-height:1.8}
a{color:var(--gold);text-decoration:none}a:hover{text-decoration:underline}
nav{position:fixed;top:0;left:0;right:0;z-index:100;padding:20px 48px;display:flex;align-items:center;justify-content:space-between;background:rgba(4,6,13,.85);backdrop-filter:blur(12px);border-bottom:1px solid var(--border)}
.nav-logo{font-family:'Cormorant Garamond',serif;font-size:20px;font-weight:600;color:var(--text);letter-spacing:1px}.nav-logo span{color:var(--gold)}
.nav-back{font-size:12px;letter-spacing:1px;color:var(--muted);transition:color .3s}.nav-back:hover{color:var(--gold);text-decoration:none}
.nav-cta{font-size:10px;letter-spacing:1.5px;text-transform:uppercase;color:var(--gold);border:1px solid var(--gold);padding:9px 20px;transition:all .3s}.nav-cta:hover{background:var(--gold);color:var(--bg);text-decoration:none}
.wrap{max-width:760px;margin:0 auto;padding:140px 32px 100px}
.article-tag{font-size:11px;letter-spacing:2px;text-transform:uppercase;color:var(--gold);margin-bottom:20px;display:block}
.article-h1{font-family:'Cormorant Garamond',serif;font-size:clamp(32px,5vw,52px);font-weight:600;line-height:1.15;margin-bottom:24px}
.article-meta{font-size:13px;color:var(--muted);margin-bottom:48px;padding-bottom:32px;border-bottom:1px solid var(--border)}
.body h2{font-family:'Cormorant Garamond',serif;font-size:28px;font-weight:600;color:var(--text);margin:52px 0 16px;padding-bottom:8px;border-bottom:1px solid var(--border)}
.body h3{font-size:16px;font-weight:600;color:var(--gold);margin:32px 0 12px;letter-spacing:.5px}
.body p{font-size:15px;color:#c8c4be;line-height:1.9;margin-bottom:20px;font-weight:300}
.body ul,.body ol{margin:0 0 20px 24px}
.body li{font-size:15px;color:#c8c4be;line-height:1.9;margin-bottom:8px;font-weight:300}
.body strong{color:var(--text);font-weight:500}
.highlight{background:rgba(201,168,76,.06);border:1px solid var(--border);border-left:3px solid var(--gold);padding:24px 28px;margin:36px 0}
.highlight p{margin-bottom:0}
.cta-box{background:linear-gradient(135deg,rgba(201,168,76,.08),rgba(201,168,76,.03));border:1px solid var(--border);padding:48px;margin:64px 0 0;text-align:center}
.cta-box h3{font-family:'Cormorant Garamond',serif;font-size:28px;margin-bottom:12px}
.cta-box p{color:var(--muted);margin-bottom:28px}
.cta-box .btn{display:inline-block;background:var(--gold);color:var(--bg);padding:14px 36px;font-size:12px;letter-spacing:2px;text-transform:uppercase;font-weight:600}
.cta-box .btn:hover{opacity:.85;text-decoration:none}
.breadcrumb{font-size:12px;color:var(--muted);margin-bottom:24px}.breadcrumb a{color:var(--muted)}.breadcrumb a:hover{color:var(--gold)}
footer{border-top:1px solid var(--border);padding:32px 48px;text-align:center;font-size:12px;color:var(--muted)}
@media(max-width:640px){nav{padding:16px 20px}.wrap{padding:110px 20px 64px}footer{padding:24px 20px}}
"""

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;0,700;1,300;1,600&family=Inter:wght@200;300;400;500;600&display=swap" rel="stylesheet">'

def make_blog_index(lang, data):
    articles = data['articles']
    cards = ''
    for a in articles:
        cards += f'''
    <a href="/{lang}/blog/{a['slug']}/" class="article-card">
      <span class="ac-tag">{a['tag']}</span>
      <div class="ac-title">{a['title']}</div>
      <p class="ac-desc">{a['desc']}</p>
      <span class="ac-link">{data['read_more']}</span>
    </a>'''

    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<title>{data['blog_title']}</title>
<meta name="description" content="{data['blog_desc']}">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://fiscalidadcanaria.com/{lang}/blog/">
<meta property="og:type" content="website">
<meta property="og:url" content="https://fiscalidadcanaria.com/{lang}/blog/">
<meta property="og:title" content="{data['blog_title']}">
<meta property="og:description" content="{data['blog_desc']}">
{FONTS}
<style>
{CSS}
.blog-wrap{{max-width:900px;margin:0 auto;padding:140px 32px 100px}}
.blog-header{{margin-bottom:72px}}
.blog-tag{{font-size:11px;letter-spacing:2px;text-transform:uppercase;color:var(--gold);margin-bottom:16px;display:block}}
.blog-h1{{font-family:'Cormorant Garamond',serif;font-size:clamp(40px,5vw,64px);font-weight:600;line-height:1.1;margin-bottom:20px}}
.blog-sub{{font-size:15px;color:var(--muted);font-weight:300;line-height:1.7}}
.articles-grid{{display:grid;grid-template-columns:repeat(2,1fr);gap:2px;background:var(--border);border:1px solid var(--border)}}
.article-card{{background:var(--bg);padding:40px 36px;transition:background .3s;position:relative}}
.article-card:hover{{background:#07091a}}
.article-card::after{{content:'';position:absolute;top:0;left:0;right:0;height:2px;background:linear-gradient(90deg,transparent,var(--gold),transparent);transform:scaleX(0);transition:transform .5s}}
.article-card:hover::after{{transform:scaleX(1)}}
.ac-tag{{font-size:10px;letter-spacing:2px;text-transform:uppercase;color:var(--gold);opacity:.7;margin-bottom:16px;display:block}}
.ac-title{{font-family:'Cormorant Garamond',serif;font-size:22px;font-weight:600;line-height:1.3;margin-bottom:12px;color:var(--text);transition:color .3s}}
.article-card:hover .ac-title{{color:var(--gold)}}
.ac-desc{{font-size:13px;color:var(--muted);line-height:1.8;font-weight:300;margin-bottom:24px}}
.ac-link{{font-size:11px;letter-spacing:1.5px;text-transform:uppercase;color:var(--gold);opacity:.7;transition:opacity .3s}}
.article-card:hover .ac-link{{opacity:1}}
@media(max-width:640px){{.articles-grid{{grid-template-columns:1fr}}.blog-wrap{{padding:110px 20px 64px}}}}
</style>
</head>
<body>
<nav>
  <a href="https://fiscalidadcanaria.com/{lang}/" class="nav-logo">Fiscalidad<span>Canaria</span></a>
  <a href="https://fiscalidadcanaria.com/{lang}/" class="nav-back">{data['nav_back']}</a>
  <a href="https://fiscalidadcanaria.com/#contacto" class="nav-cta">{data['nav_cta']}</a>
</nav>
<div class="blog-wrap">
  <div class="blog-header">
    <span class="blog-tag">{data['blog_tag']}</span>
    <h1 class="blog-h1">{data['blog_h1']}</h1>
    <p class="blog-sub">{data['blog_sub']}</p>
  </div>
  <div class="articles-grid">{cards}
  </div>
</div>
<footer>{data['footer']} · <a href="https://fiscalidadcanaria.com/{lang}/" style="color:var(--muted)">fiscalidadcanaria.com</a> · <a href="mailto:fiscal@alfiscocanaria.com" style="color:var(--muted)">fiscal@alfiscocanaria.com</a></footer>
</body>
</html>'''


def make_article(lang, data, article):
    sections_html = ''
    for title, content in article['sections']:
        # Check if content already has h3 tags
        if '<h3>' in content or '<ul>' in content or '<ol>' in content:
            sections_html += f'<h2>{title}</h2>\n<div>{content}</div>\n'
        else:
            # Plain text, wrap in p
            paras = content.split('\n\n')
            p_html = ''.join(f'<p>{p}</p>' for p in paras if p.strip())
            sections_html += f'<h2>{title}</h2>\n{p_html}\n'

    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<title>{article['title']} | Fiscalidad Canaria</title>
<meta name="description" content="{article['desc']}">
<meta name="keywords" content="{article['keywords']}">
<meta name="author" content="Raúl Labao — Fiscalidad Canaria">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://fiscalidadcanaria.com/{lang}/blog/{article['slug']}/">
<meta property="og:type" content="article">
<meta property="og:url" content="https://fiscalidadcanaria.com/{lang}/blog/{article['slug']}/">
<meta property="og:title" content="{article['title']}">
<meta property="og:description" content="{article['desc']}">
<meta property="og:site_name" content="Fiscalidad Canaria">
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"Article","headline":"{article['title']}","author":{{"@type":"Person","name":"Raúl Labao"}},"publisher":{{"@type":"Organization","name":"Fiscalidad Canaria","url":"https://fiscalidadcanaria.com"}},"datePublished":"2026-07-16","dateModified":"2026-07-16","url":"https://fiscalidadcanaria.com/{lang}/blog/{article['slug']}/","inLanguage":"{lang}"}}</script>
{FONTS}
<style>{CSS}</style>
</head>
<body>
<nav>
  <a href="https://fiscalidadcanaria.com/{lang}/" class="nav-logo">Fiscalidad<span>Canaria</span></a>
  <a href="/{lang}/blog/" class="nav-back">← Blog</a>
  <a href="https://fiscalidadcanaria.com/#contacto" class="nav-cta">{data['nav_cta']}</a>
</nav>
<div class="wrap">
  <div class="breadcrumb"><a href="https://fiscalidadcanaria.com/{lang}/">{data['nav_back'].replace('← ','')}</a> · <a href="/{lang}/blog/">Blog</a> · {article['breadcrumb_label']}</div>
  <span class="article-tag">{article['tag']}</span>
  <h1 class="article-h1">{article['title']}</h1>
  <div class="article-meta">{data['by']} <strong style="color:var(--text)">Raúl Labao</strong> · Fiscalidad Canaria · {data['date']} · {article['read_time']} {data['min_read']}</div>
  <div class="body">
    <p>{article['intro']}</p>
    <div class="highlight"><p>{article['highlight']}</p></div>
    {sections_html}
    <div class="cta-box">
      <h3>{data['free_cta_title']}</h3>
      <p>{data['free_cta_desc']}</p>
      <a href="https://fiscalidadcanaria.com/#contacto" class="btn">{data['free_cta_btn']}</a>
    </div>
  </div>
</div>
<footer>{data['footer']} · <a href="https://fiscalidadcanaria.com/{lang}/" style="color:var(--muted)">fiscalidadcanaria.com</a> · <a href="mailto:fiscal@alfiscocanaria.com" style="color:var(--muted)">fiscal@alfiscocanaria.com</a></footer>
</body>
</html>'''


for lang, data in LANGS.items():
    # Blog index
    blog_dir = f'{lang}/blog'
    os.makedirs(blog_dir, exist_ok=True)
    with open(f'{blog_dir}/index.html', 'w', encoding='utf-8') as f:
        f.write(make_blog_index(lang, data))
    print(f'✓ {blog_dir}/index.html')

    # Articles
    for article in data['articles']:
        art_dir = f'{lang}/blog/{article["slug"]}'
        os.makedirs(art_dir, exist_ok=True)
        with open(f'{art_dir}/index.html', 'w', encoding='utf-8') as f:
            f.write(make_article(lang, data, article))
        print(f'  ✓ {art_dir}/index.html')

print('\nDone.')
