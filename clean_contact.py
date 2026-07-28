import re

with open('css/contact.css', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove header styles
content = re.sub(r'/\* Header: start from here \*/.*?(?=\.contact-split)', '', content, flags=re.DOTALL)

# Remove footer styles
content = re.sub(r'\.site-footer\s*\{.*?(?=\s*/\* ================= RESPONSIVE)', '', content, flags=re.DOTALL)

# Remove .header, .link, .site-footer from max-width 700px
content = re.sub(r'\s*\.header\s*\{[^}]+\}', '', content)
content = re.sub(r'\s*\.link\s*\{[^}]+\}', '', content)
content = re.sub(r'\s*\.site-footer\s*\{[^}]+\}', '', content)

with open('css/contact.css', 'w', encoding='utf-8') as f:
    f.write(content)
