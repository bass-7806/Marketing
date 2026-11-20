import json, os
H = os.path.dirname(os.path.abspath(__file__))
d = open(os.path.join(H, "data.json"), encoding="utf-8").read()
d = json.dumps(json.loads(d), ensure_ascii=False).replace("</", "<\\/")
t = open(os.path.join(H, "playbook_template.html"), encoding="utf-8").read()
open(os.path.join(H, "bwell-key-message-playbook.html"), "w", encoding="utf-8").write(t.replace("/*__DATA__*/", d))
print("ok")
