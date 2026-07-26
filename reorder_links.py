import glob, re

for f in glob.glob("*.html"):
    if f == "impact_guide.html":
        continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
        
    # Match the contact link, the whitespace, and the impact link
    contact_pattern = r'(<a\b[^>]*href="contact\.html"[^>]*>.*?</a>)'
    impact_pattern = r'(<a\b[^>]*href="impact\.html"[^>]*>.*?</a>)'
    
    full_pattern = contact_pattern + r'(\s*)' + impact_pattern
    
    # Swap them
    new_content = re.sub(full_pattern, r'\3\2\1', content, flags=re.DOTALL)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(new_content)
