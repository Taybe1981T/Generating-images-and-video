import os

base = "C:/Users/taybe kraa/Desktop/New folder/"
p = base + "ai_studio_code.html"

with open(p, "r", encoding="utf-8") as f:
    s = f.read()

# Add CSS status features
css = """.status-banner { display: flex; align-items: center; gap: 10px; padding: 10px 14px; border-radius: 8px; font-size: 13px; font-weight: 600; margin-top: 10px; border: 1px solid transparent; }
.status-success { background: #064e3b; color: #bbf7d0; border-color: #10b981; }
.status-error { background: #7f1d1d; color: #fecaca; border-color: #ef4444; }
.status-info { background: #1e3a8a; color: #bfdbfe; border-color: #3b82f6; }
.duration-info { display: flex; gap: 18px; font-size: 11px; color: #9ca3af; margin-top: 6px; flex-wrap: wrap; }
.duration-item { display: flex; align-items: center; gap: 6px; }
.copyable-errors { background: #000; color: #f87171; font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; font-size: 11px; padding: 10px; border-radius: 6px; max-height: 180px; overflow-y: auto; white-space: pre-wrap; word-break: break-all; border: 1px solid #ef4444; margin-top: 6px; }
.copy-btn { background: #374151; color: #fff; border: 1px solid #6b7280; padding: 4px 10px; border-radius: 4px; cursor: pointer; font-size: 11px; margin-left: auto; }
.copy-btn:hover { background: #4b5563; }
.retry-notice { background: #450a0a; color: #fecaca; border: 1px solid #ef4444; padding: 10px 14px; border-radius: 8px; margin-top: 10px; font-size: 13px; font-weight: 600; display: flex; align-items: center; gap: 10px; }"""

anchor = "</style>"
if anchor in s:
    s = s.replace(anchor, css + "</style>", 1)
    print("CSS added")

with open(p, "w", encoding="utf-8") as f:
    f.write(s)
print("CSS done")