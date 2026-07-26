import glob, re
import os

for f in glob.glob('css/*.css'):
    with open(f, 'r') as file:
        content = file.read()
    
    if content:
        # Avoid adding it multiple times
        if "background-color: var(--color-primary);" not in content.split('.heroo')[1].split('}')[0] if '.heroo' in content else False:
            new_content = re.sub(r'\.heroo\s*\{', '.heroo {\n    background-color: var(--color-primary);', content)
            with open(f, 'w') as file:
                file.write(new_content)
