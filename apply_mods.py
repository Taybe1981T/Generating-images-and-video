import os

base = "C:/Users/taybe kraa/Desktop/New folder/"
p = base + "ai_studio_code.html"

with open(p, "r", encoding="utf-8") as f:
    s = f.read()

# 1. Add CSS
new_css = """.status-banner { display: flex; align-items: center; gap: 10px; padding: 10px 14px; border-radius: 8px; font-size: 13px; font-weight: 600; margin-top: 10px; border: 1px solid transparent; }
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
assert anchor in s
s = s.replace(anchor, new_css + "</style>", 1)

# 2. Add HTML status block after terminal section
html_block = """                <!-- حالة التوليد والمدة والأخطاء -->
                <div id="generationStatus" class="hidden space-y-3">
                    <div id="statusBanner" class="status-banner status-info">
                        <i class="fa-solid fa-info-circle"></i> <span id="statusText">جارٍ التوليد...</span>
                    </div>
                    <div class="duration-info">
                        <div class="duration-item"><i class="fa-solid fa-clock"></i> <span>المدة قبل التوليد: <span id="durationBefore">-</span></span></div>
                        <div class="duration-item"><i class="fa-solid fa-clock"></i> <span>المدة بعد التوليد: <span id="durationAfter">-</span></span></div>
                    </div>
                    <div id="errorsContainer" class="hidden">
                        <div class="flex justify-between items-start mb-2">
                            <span class="text-xs font-bold text-red-400">⚠️ أخطاء التوليد:</span>
                            <button onclick="copyErrors()" class="copy-btn">نسخ الأخطاء</button>
                        </div>
                        <div id="errorsList" class="copyable-errors"></div>
                    </div>
                </div>

                <!-- إشعار فشل التوليد -->
                <div id="retryNotice" class="retry-notice hidden">
                    <i class="fa-solid fa-triangle-exclamation"></i> فشل التوليد — أعد المحاولة بعد التحقق من المفاتيح أو الرصيد.
                </div>

            </div>"""

# Find the anchor: the closing of terminal section then col-span-7 closing
# We know the structure: after terminal div closes, then col-span-7 closes
# Let's find the location by looking for the col-span-7 div end
# Actually, let's insert after the generatingCard and before the end of col-span-7
# We'll find the location by searching for the text that marks the end of main content area

# Insert the block after the generatingCard div closes and before the closing of col-span-7
# Looking at the structure, we need to insert it after the terminal div closing marker
# The marker is: the closing of the terminal card div, then the closing of the col-span-7 div

# Actually, let's just find where the outputSection is and insert before it, or find another anchor
# Let's find the text that appears after the terminal section in the current file

# Let's use a different approach - find the location of 'outputSection' and insert the block before it
# But outputSection is already at the top... Let's find the right place

# Actually, re-reading the requirements: the status block should be AFTER the terminal section
# and BELOW the output video area... Wait, let me re-read.

# The user wants: "عند انتهاء توليد يعرض فيديو او صورة في صفحة التوليد" and "قسم سجل الأحداث المباشر (terminal) — أسفلهم"

# So the status should be UNDER the terminal section, still in the main column

# Let's find where the terminal section ends by looking for its closing patterns
# In the current file, the terminal section ends with the </div> tags

# Let me search for a reliable anchor
search_text = "                <!-- Ø§Ù„Ø¹Ù…ÙˆØ¯ Ø§Ù„Ø±Ø¦ÙŠØ³ÙŠ:"
idx = s.find(search_text)
if idx != -1:
    # Found, now find the end marker after it
    end_marker = "                <!-- الفيديو الحقيقي الناتج"
    idx2 = s.find(end_marker, idx)
    if idx2 != -1:
        # Insert the block between idx and idx2... actually we want to insert it before the outputSection maybe?
        # Let me just use a different approach: insert the block right before the closing of col-span-7
        # The col-span-7 closing is:            </div>\n        </div>\n    </div>
        # Let's find that
        col7_closing = "                </div>\n        </div>\n    </div>"
        idx_end = s.find(col7_closing)
        if idx_end != -1:
            # Insert the block right before this closing
            s = s[:idx_end] + html_block + s[idx_end:]
            print("Inserted status block before col-span-7 closing")
        else:
            print("Could not find col-span-7 closing")
    else:
        print("Could not find end marker after terminal")
else:
    print("Could not find search text")

# Save
with open(p, "w", encoding="utf-8") as f:
    f.write(s)

print("Modification script completed")
os._exit(0)
"]