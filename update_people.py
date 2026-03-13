import os
import re

content_dir = 'content/people'

def get_group(role):
    role_lower = role.lower()
    if 'professor' in role_lower or 'lecturer' in role_lower:
        return 'Faculty'
    elif 'phd' in role_lower or 'postdoc' in role_lower:
        return 'PhDs & Postdocs'
    else:
        return 'Other'

def update_person_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # Extract front matter
    fm_match = re.search(r'\+\+\+(.*?)\+\+\+', content, re.DOTALL)
    if not fm_match:
        return

    fm_content = fm_match.group(1)
    body_content = content[fm_match.end():].strip()

    # Extract current values
    title_match = re.search(r'title = "(.*?)"', fm_content)
    role_match = re.search(r'description = "(.*?)"', fm_content)
    image_match = re.search(r'image = "(.*?)"', fm_content)
    
    title = title_match.group(1) if title_match else ""
    role = role_match.group(1) if role_match else ""
    image = image_match.group(1) if image_match else ""
    
    # Determine group
    group = get_group(role)
    
    # Extract website from body
    website = ""
    link_match = re.search(r'\[Profile Link\]\((.*?)\)', body_content)
    if link_match:
        website = link_match.group(1)
        # Remove the link from body if desired, but user didn't ask to remove it. 
        # But having it in front matter is better.
    
    # Construct new front matter
    new_fm = "+++\n"
    new_fm += f'title = "{title}"\n'
    new_fm += f'date = 2024-01-01\n'
    new_fm += f'draft = false\n'
    new_fm += f'description = "{role}"\n'
    new_fm += f'image = "{image}"\n'
    new_fm += f'group = "{group}"\n'
    new_fm += f'email = ""\n'
    new_fm += f'website = "{website}"\n'
    new_fm += "+++\n"
    
    # Write back
    with open(filepath, 'w') as f:
        f.write(new_fm + "\n" + body_content)

for filename in os.listdir(content_dir):
    if filename.endswith(".md") and filename != "_index.md":
        update_person_file(os.path.join(content_dir, filename))
        print(f"Updated {filename}")
