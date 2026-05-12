import re, os

base = '/Users/rayhsu/Projects/websites/stitch_orozco_visuals_digital_experience'

MOBILE_DRAWER = '''\
<!-- Mobile Menu Drawer -->
<div id="mobile-menu" class="fixed inset-0 z-[200] hidden" role="dialog" aria-modal="true">
  <div class="absolute inset-0 bg-black/60 backdrop-blur-sm" onclick="document.getElementById('mobile-menu').classList.add('hidden')"></div>
  <div class="absolute top-0 left-0 h-full w-72 bg-surface flex flex-col py-10 px-10 shadow-2xl">
    <button onclick="document.getElementById('mobile-menu').classList.add('hidden')" class="self-end mb-12 text-primary hover:opacity-60 transition-opacity">
      <span class="material-symbols-outlined text-2xl">close</span>
    </button>
    <nav class="flex flex-col gap-10 flex-1">
      <a href="index.html"      class="font-label-sm text-label-sm tracking-[0.2em] uppercase text-primary hover:opacity-60 transition-opacity">HOME</a>
      <a href="about.html"      class="font-label-sm text-label-sm tracking-[0.2em] uppercase text-on-surface-variant hover:opacity-60 transition-opacity">ABOUT</a>
      <a href="portfolio.html"  class="font-label-sm text-label-sm tracking-[0.2em] uppercase text-on-surface-variant hover:opacity-60 transition-opacity">WORK</a>
      <a href="investment.html" class="font-label-sm text-label-sm tracking-[0.2em] uppercase text-on-surface-variant hover:opacity-60 transition-opacity">PRICING</a>
      <a href="graduation.html" class="font-label-sm text-label-sm tracking-[0.2em] uppercase text-on-surface-variant hover:opacity-60 transition-opacity">GRADUATION</a>
    </nav>
    <a href="book.html" class="font-label-sm text-label-sm tracking-[0.2em] uppercase bg-primary text-on-primary py-4 text-center hover:opacity-80 transition-opacity mt-10">BOOK NOW</a>
  </div>
</div>
'''

def make_bottom_nav(active):
    a = "text-tertiary-fixed font-bold translate-y-[-2px]"
    i = "text-on-primary-fixed-variant opacity-60"
    items = [
        ("home",          "index.html",      "HOME",    active == "home"),
        ("photo_library", "portfolio.html",  "WORK",    active == "work"),
        ("payments",      "investment.html", "PRICING", active == "pricing"),
        ("calendar_today","book.html",       "BOOK",    active == "book"),
    ]
    links = []
    for icon, url, label, is_active in items:
        cls = a if is_active else i
        links.append(
            f'<a class="flex flex-col items-center justify-center {cls}" href="{url}">\n'
            f'<span class="material-symbols-outlined">{icon}</span>\n'
            f'<span class="font-label-sm text-[10px] mt-1 tracking-widest">{label}</span>\n'
            f'</a>'
        )
    return (
        '<!-- BottomNavBar (Mobile Only) -->\n'
        '<nav class="md:hidden fixed bottom-0 left-0 w-full flex justify-around items-center py-4 px-2 bg-primary z-50 shadow-2xl">\n'
        + '\n'.join(links) +
        '\n</nav>'
    )

def find_bottom_nav_start(content):
    for marker in ['<!-- BottomNavBar', '<!-- Mobile Navigation Bar', '<!-- Mobile Navigation']:
        idx = content.rfind(marker)
        if idx != -1:
            return idx
    # fall back: last md:hidden fixed bottom-0 block
    last = -1
    for m in re.finditer(r'<(?:nav|div)[^>]+md:hidden[^>]+bottom-0', content):
        last = m.start()
    return last

pages = {
    'index.html':      'home',
    'about.html':      'home',   # about active isn't a bottom-nav item; home stays neutral
    'portfolio.html':  'work',
    'investment.html': 'pricing',
    'book.html':       'book',
    'graduation.html': 'book',
}

for filename, active in pages.items():
    path = os.path.join(base, filename)
    with open(path) as f:
        content = f.read()

    # 1. Strip existing bottom nav section
    idx = find_bottom_nav_start(content)
    if idx != -1:
        content = content[:idx].rstrip()
    else:
        # fallback: strip </body></html>
        content = content.rsplit('</body>', 1)[0].rstrip()

    # 2. Append drawer + bottom nav + closing tags
    content += '\n' + MOBILE_DRAWER + '\n' + make_bottom_nav(active) + '\n</body></html>'

    # 3. Wire up hamburger icon (first occurrence of material-symbols-outlined span containing "menu")
    content = re.sub(
        r'(<span\b[^>]*\bmaterial-symbols-outlined\b[^>]*)(>menu</span>)',
        lambda m: m.group(1).rstrip() + ' onclick="document.getElementById(\'mobile-menu\').classList.remove(\'hidden\')" style="cursor:pointer"' + m.group(2),
        content,
        count=1
    )

    # 4. Wire up the mobile calendar icon in the header (index.html has one)
    content = re.sub(
        r'<div class="md:hidden">\s*<span class="material-symbols-outlined">calendar_today</span>\s*</div>',
        '<a href="book.html" class="md:hidden"><span class="material-symbols-outlined">calendar_today</span></a>',
        content
    )

    with open(path, 'w') as f:
        f.write(content)
    print(f'  Fixed: {filename}')

print('Done.')
