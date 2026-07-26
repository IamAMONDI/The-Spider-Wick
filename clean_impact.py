import re

with open('css/impact.css', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove header styles (from /* Header & Footer to .impact-main)
content = re.sub(r'/\* Header & Footer.*?/\* ---- Impact Main Content ---- \*/', '/* ---- Impact Main Content ---- */', content, flags=re.DOTALL)

# Remove footer styles (from /* ---- Footer to /* === MEDIA QUERIES)
content = re.sub(r'/\* ---- Footer.*?/\* ==========================================================\s*MEDIA QUERIES', '/* ==========================================================\n   MEDIA QUERIES', content, flags=re.DOTALL)

# Remove .header, .header-1, .link from max-width 900px
content = re.sub(r'\s*\.header \{[^}]+\}\s*\.header-1 \{[^}]+\}\s*\.link \{[^}]+\}', '', content)

# Remove .site-footer from max-width 600px
content = re.sub(r'\s*\.site-footer \{[^}]+\}', '', content)

with open('css/impact.css', 'w', encoding='utf-8') as f:
    f.write(content)
