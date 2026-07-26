import glob, re

def add_link():
    files = glob.glob("*.html")
    for f in files:
        if f == "impact.html" or f == "impact_guide.html":
            continue
        
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
            
        # The navbar link usually contains 'contact.html' inside a <nav> or a div with class 'header-1' or 'navbar-nav'
        # We can find all <a> tags that point to contact.html, and insert an impact.html link right after them.
        
        # 1. Replace the header Contact link
        # It's an a tag with class "nav-link link" or "link"
        # We'll use a regex that captures the contact.html <a> tag and appends impact.html.
        
        def replacer(match):
            original = match.group(0)
            
            # If it's a footer link
            if "footer-link" in original:
                return original + '\n                    <a href="impact.html" class="footer-link">\n                        Impact\n                    </a>'
            
            # If it's the home/about/mission navbar
            elif "<h3>" in original:
                return original + '\n\n                    <a class="nav-link link" href="impact.html"><h3>Impact</h3></a>'
            
            # If it's the contact.html or generic navbar
            else:
                return original + '\n            <a href="impact.html" class="link">Impact</a>'
        
        # This regex matches the entire <a> block for contact.html
        # Note: In home.html, there's another link: <a href="contact.html" class="contact">Connect with us</a> which we SHOULD NOT replace with an impact link, but if we do, it's not the end of the world.
        # Actually, let's only target links that say "Contact", "Contact Us", or "Contact us".
        
        # Replace only if it contains 'nav-link', 'link', or 'footer-link'
        new_content = re.sub(r'<a[^>]*href="contact\.html"[^>]*>.*?</a>', 
                             lambda m: replacer(m) if ('class="link' in m.group(0) or 'nav-link' in m.group(0) or 'footer-link' in m.group(0)) else m.group(0), 
                             content, flags=re.DOTALL)
                             
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)

add_link()
