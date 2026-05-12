import re, os

base = '/Users/rayhsu/Projects/websites/stitch_orozco_visuals_digital_experience'
site_dir = os.path.join(base, 'site')
os.makedirs(site_dir, exist_ok=True)

files = {
    'home_orozco_visuals/code.html': 'index.html',
    'about_orozco_visuals/code.html': 'about.html',
    'portfolio_orozco_visuals/code.html': 'portfolio.html',
    'investment_orozco_visuals/code.html': 'investment.html',
    'book_your_session_orozco_visuals/code.html': 'book.html',
    'graduation_orozco_visuals/code.html': 'graduation.html',
}

nav_replacements = [
    ('href="#">HOME</a>',                       'href="index.html">HOME</a>'),
    ('href="#">WORK</a>',                       'href="portfolio.html">WORK</a>'),
    ('href="#">PRICING</a>',                    'href="investment.html">PRICING</a>'),
    ('href="#">ABOUT</a>',                      'href="about.html">ABOUT</a>'),
    ('href="#">BOOK</a>',                       'href="book.html">BOOK</a>'),
    ('href="#">GRADUATION</a>',                 'href="graduation.html">GRADUATION</a>'),
    ("href=\"#\">LET'S TELL YOUR STORY</a>",   "href=\"book.html\">LET'S TELL YOUR STORY</a>"),
    ('href="#">CONTACT</a>',                    'href="book.html">CONTACT</a>'),
    ('href="#">INSTAGRAM</a>',                  'href="#">INSTAGRAM</a>'),
    ('href="#">FACEBOOK</a>',                   'href="#">FACEBOOK</a>'),
    ('href="#">READ OUR STORY</a>',             'href="about.html">READ OUR STORY</a>'),
    ('href="#">VIEW PORTFOLIO</a>',             'href="portfolio.html">VIEW PORTFOLIO</a>'),
    ('href="#">GET IN TOUCH</a>',               'href="book.html">GET IN TOUCH</a>'),
    ('href="#">INQUIRE NOW</a>',                'href="book.html">INQUIRE NOW</a>'),
    ('href="#">REQUEST BROCHURE</a>',           'href="book.html">REQUEST BROCHURE</a>'),
    ('href="#">DISCOVER ALL WORK</a>',          'href="portfolio.html">DISCOVER ALL WORK</a>'),
]

button_replacements = [
    ('BOOK NOW',            'book.html'),
    ('INQUIRE NOW',         'book.html'),
    ('CHECK AVAILABILITY',  'book.html'),
    ('VIEW PORTFOLIO',      'portfolio.html'),
    ('VIEW PRICING',        'investment.html'),
    ('RESERVE PREMIER',     'book.html'),
    ('SELECT SESSION',      'book.html'),
    ('GROUP BOOKING',       'book.html'),
    ('INQUIRE FOR DATES',   'book.html'),
    ('BOOK SESSION',        'book.html'),
]

for src_rel, dst_name in files.items():
    src = os.path.join(base, src_rel)
    with open(src, 'r') as f:
        content = f.read()

    for old, new in nav_replacements:
        content = content.replace(old, new)

    for label, url in button_replacements:
        content = re.sub(
            rf'<button([^>]*)>{re.escape(label)}</button>',
            rf'<a href="{url}"\1 style="display:inline-block;text-decoration:none;text-align:center;">{label}</a>',
            content
        )

    dst = os.path.join(site_dir, dst_name)
    with open(dst, 'w') as f:
        f.write(content)
    print(f'  {src_rel}  →  {dst_name}')

print('Done.')
