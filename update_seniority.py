import os
import re

# Define seniority order (lower number = higher seniority)
seniority_map = {
    "Peter Sloot": 1,
    "Alfons Hoekstra": 2,
    "Drona Kandhai": 3,
    "Peter Coveney": 4,
    "Rob Belleman": 5,
    "Valeria Krzhizhanovskaya": 6,
    "Rick Quax": 7,
    "Mike Lees": 8,
    "Derek Groen": 9,
    "Wouter Huberts": 10,
    "Johan Bollen": 11,
    "Gabor Zavadsky": 12, # Note: Check spelling in file
    "Gábor Závodszky": 12,
    "Jie Li": 13,
    "Vivek Sheraton Muniraj": 14,
    "Sven Karbach": 15,
    "Victoria Garibay": 16,
    "Vítor Vasconcelos": 17,
    "Debraj Roy": 18,
    "Andrea Tabi": 19,
    "Giulia Pederzani": 20,
    "Clélia de Mulatier": 21,
    "Ben Meylahn": 22,
    "Alberto Pérez de Alba Ortíz": 23,
    "Tanzhe Tang": 24,
    "Mark Wijzenbroek": 25,
    "Vittorio Nespeca": 26,
    "Rafiazka Hilman": 27,
    "Joey van der Kaaij": 28,
    "Jaap Kaandorp": 29
}

people_dir = "content/people"

for filename in os.listdir(people_dir):
    if filename.endswith(".md") and filename != "_index.md":
        filepath = os.path.join(people_dir, filename)
        with open(filepath, "r") as f:
            content = f.read()
        
        # Check if it's TOML frontmatter
        if content.startswith("+++"):
            # Extract frontmatter block
            fm_match = re.search(r'^\+\+\+(.*?)\+\+\+', content, re.DOTALL)
            if fm_match:
                fm_content = fm_match.group(1)
                
                # Check for group = "Faculty"
                if 'group = "Faculty"' in fm_content or "group = 'Faculty'" in fm_content:
                    # Extract title
                    title_match = re.search(r'title\s*=\s*["\'](.*?)["\']', fm_content)
                    if title_match:
                        title = title_match.group(1)
                        seniority = 99 # Default
                        matched_name = None
                        
                        # Find matching seniority
                        for name, rank in seniority_map.items():
                            parts = name.split()
                            if all(part.lower() in title.lower() for part in parts):
                                seniority = rank
                                matched_name = name
                                break
                        
                        # Check if seniority is already set
                        if 'seniority =' not in fm_content:
                            # Insert seniority line before closing +++
                            new_fm_content = fm_content.rstrip() + f'\nseniority = {seniority}\n'
                            new_content = content.replace(fm_content, new_fm_content)
                            
                            with open(filepath, "w") as f:
                                f.write(new_content)
                            
                            if matched_name:
                                print(f"Updated {filename}: matched '{matched_name}' -> seniority {seniority}")
                            else:
                                print(f"Updated {filename}: no match -> seniority {seniority}")
                        else:
                            # Update existing seniority
                            new_fm_content = re.sub(r'seniority\s*=\s*\d+', f'seniority = {seniority}', fm_content)
                            new_content = content.replace(fm_content, new_fm_content)
                            with open(filepath, "w") as f:
                                f.write(new_content)
                            print(f"Updated existing seniority for {filename} to {seniority}")

print("Finished updating seniority.")
