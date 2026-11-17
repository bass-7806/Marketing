# Search Openverse (CC0 / CC BY only), list candidates; download one with --get <n>.
# usage: openverse_sfx.py "<query>" [--get N --out file]
import sys, json, urllib.request, urllib.parse
q = sys.argv[1]
url = "https://api.openverse.org/v1/audio/?" + urllib.parse.urlencode({"q": q, "license": "cc0,by", "page_size": 12})
d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "hf-sfx/1.0"}), timeout=90))
res = [r for r in d.get("results", []) if (r.get("duration") or 999999) <= 30000]
if "--get" in sys.argv:
    r = res[int(sys.argv[sys.argv.index("--get") + 1])]; out = sys.argv[sys.argv.index("--out") + 1]
    data = urllib.request.urlopen(urllib.request.Request(r["url"], headers={"User-Agent": "hf-sfx/1.0"}), timeout=120).read()
    open(out, "wb").write(data)
    print(json.dumps({"file": out, "title": r["title"], "creator": r.get("creator"), "license": r["license"], "license_version": r.get("license_version"), "source": r.get("foreign_landing_url")}, ensure_ascii=False))
else:
    for i, r in enumerate(res):
        print(i, r["license"], f'{(r.get("duration") or 0)/1000:.1f}s', r.get("filetype"), "|", r["title"][:60], "|", r.get("creator"))
