import re

# Fix gallery.html
with open('gallery.html', 'r', encoding='utf-8') as f:
    gallery = f.read()

gallery = gallery.replace('''            <a class="navbar-brand" href="home.html">
                Spiders
            </a>''', '<a class="navbar-brand" href="home.html"><h1>MindWell</h1></a>')

gallery = gallery.replace('''                    <a href="impact.html" class="link">Impact</a>
            <a class="nav-link link" href="contact.html">''', '''                    <a class="nav-link link" href="impact.html">Impact</a>
                    <a class="nav-link link" href="contact.html">''')

with open('gallery.html', 'w', encoding='utf-8') as f:
    f.write(gallery)


# Fix contact.html by wrapping its main content with home.html's header/footer
with open('home.html', 'r', encoding='utf-8') as f:
    home = f.read()

with open('contact.html', 'r', encoding='utf-8') as f:
    contact = f.read()

# Extract header from home.html (up to </header>)
header_part = home[:home.find('</header>') + len('</header>')]
# Also we need to inject contact.css instead of home.css, or keep both.
# home.html head has:
# <link href="css/home.css" rel="stylesheet">
header_part = header_part.replace('<link href="css/home.css" rel="stylesheet">', '<link href="css/home.css" rel="stylesheet">\n    <link href="css/contact.css" rel="stylesheet">')
# And change title to Contact Us
header_part = header_part.replace('<title>Menatl Health</title>', '<title>Contact Us — Mindwell</title>')

# Extract footer from home.html (from <footer class="site-footer"> onwards)
footer_part = home[home.find('<footer class="site-footer">'):]

# Extract main content from contact.html
main_match = re.search(r'(<section class="contact-split">.*?</section>)', contact, flags=re.DOTALL)
if main_match:
    main_content = main_match.group(1)
else:
    print("Could not find main content in contact.html")
    main_content = ""

# Assemble contact.html
new_contact = header_part + "\n\n<main class=\"contact-main\">\n" + main_content + "\n</main>\n\n" + footer_part

with open('contact.html', 'w', encoding='utf-8') as f:
    f.write(new_contact)
