"""Build the Bwell apple.com/th-pattern prototypes into a static Netlify site.

Usage: python3 build.py <output-dir>

Wraps each prototype page into a full HTML document, blocks search indexing
(prototype copy mirrors bwell.co.th), copies only the assets each page uses and
rewires "learn more" links so the pages click through to each other. Buy links
keep pointing at the live bwell.co.th product pages.
"""
import os
import re
import shutil
import sys

SRC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else os.path.join(SRC, "netlify", "dist"))

PAGES = {
    "index.html": "bwell-home-prototype.html",
    "robot-vacuum.html": "bwell-category-robot-prototype.html",
    "ultra-t20.html": "bwell-product-t20-prototype.html",
    "support.html": "bwell-support-prototype.html",
    "compare.html": "bwell-compare-robot-prototype.html",
    "global-nav.html": "bwell-nav-prototype.html",
}
T20_LIVE = "https://bwell.co.th/product/robot-vacuum-cleaner-bwell-ultra-t20/"
ROBOT_LIVE = "https://bwell.co.th/robot-vacuum/"
HEAD_EXTRA = '<meta name="robots" content="noindex,nofollow">\n<link rel="icon" href="home-assets/bwell-logo.png">\n'


def wrap(src: str) -> str:
    head, sep, body = src.partition("</style>\n")
    if not sep:
        raise SystemExit("page has no </style> boundary")
    return ('<!doctype html>\n<html lang="th">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width,initial-scale=1">\n'
            + HEAD_EXTRA + head + "</style>\n</head>\n<body>\n" + body + "\n</body>\n</html>\n")


def set_href(html: str, nav_pattern: str, target: str) -> str:
    """Point every anchor whose data-nav matches nav_pattern at target."""
    def repl(m):
        tag = m.group(0)
        if re.search(r'data-nav="(%s)"' % nav_pattern, tag):
            tag = re.sub(r'href="[^"]*"', 'href="%s"' % target, tag, count=1)
        return tag
    return re.sub(r'<a\b[^>]*>', repl, html)


def rewire(name: str, html: str) -> str:
    # Shared: logo goes home, nav robot tab and footer robot link go to the category page
    html = html.replace('<a class="gn-logo" href="#"', '<a class="gn-logo" href="index.html"')
    html = html.replace("href=\"#${key}\"", "href=\"${({'c-robot':'robot-vacuum.html','support':'support.html'})[key]||'#'+key}\"")
    html = html.replace('<li><a href="#">Ultra T20 OmniBase <span class="tag">New</span></a></li>',
                        '<li><a href="ultra-t20.html">Ultra T20 OmniBase <span class="tag">New</span></a></li>')
    html = html.replace('<li><a href="#">เปรียบเทียบทุกรุ่น</a></li></ul></div>\n    <div class="gn-group"><h3>ซื้อหุ่นยนต์ดูดฝุ่น',
                        '<li><a href="compare.html">เปรียบเทียบทุกรุ่น</a></li></ul></div>\n    <div class="gn-group"><h3>ซื้อหุ่นยนต์ดูดฝุ่น')
    html = set_href(html, r"[a-z0-9/]+/footer/เลือกซื้อและเรียนรู้/หุ่นยนต์ดูดฝุ่น", "robot-vacuum.html")
    html = set_href(html, r"[a-z0-9/]+/footer/breadcrumb/home", "index.html")
    if name == "index.html":
        html = set_href(html, r"home/hero/t20/learn|home/ribbon/t20|home/gallery/t20", "ultra-t20.html")
        html = set_href(html, r"home/hero/t20/buy", T20_LIVE)
    elif name == "robot-vacuum.html":
        html = set_href(html, r"cat/robot/(chapter/t20|prio/learn|lineup/t20/learn)", "ultra-t20.html")
        html = set_href(html, r"cat/robot/(which/fullcompare|lineup/compare|chapter/compare)", "compare.html")
    elif name == "compare.html":
        html = html.replace('href="${m.url}" data-nav="compare/head/${k}/learn"',
                            'href="${k===\'t20\'?\'ultra-t20.html\':m.url}" data-nav="compare/head/${k}/learn"')
        html = set_href(html, r"compare/(help/category|footer/breadcrumb/robot-vacuum)", "robot-vacuum.html")
    elif name == "support.html":
        html = set_href(html, r"support/product/robot", "robot-vacuum.html")
    elif name == "ultra-t20.html":
        html = set_href(html, r"pdp/t20/footer/breadcrumb/robot-vacuum", "robot-vacuum.html")
    return html


def main():
    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)
    used = set()
    for out_name, src_name in PAGES.items():
        html = rewire(out_name, wrap(open(os.path.join(SRC, src_name), encoding="utf-8").read()))
        used.update(re.findall(r'((?:home|product)-assets/[A-Za-z0-9._-]+)', html))
        open(os.path.join(OUT, out_name), "w", encoding="utf-8").write(html)
    for rel in sorted(used):
        os.makedirs(os.path.join(OUT, os.path.dirname(rel)), exist_ok=True)
        shutil.copy2(os.path.join(SRC, rel), os.path.join(OUT, rel))
    open(os.path.join(OUT, "robots.txt"), "w").write("User-agent: *\nDisallow: /\n")
    open(os.path.join(OUT, "netlify.toml"), "w").write(
        '[build]\n  publish = "."\n  command = "echo static"\n\n'
        '[[headers]]\n  for = "/*"\n  [headers.values]\n    X-Robots-Tag = "noindex, nofollow"\n')
    print(f"built {len(PAGES)} pages and {len(used)} assets into {OUT}")


if __name__ == "__main__":
    main()
