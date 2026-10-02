# Computational Science Lab (CSL) Website

This repository contains the source code for the [Computational Science Lab](https://computationalscience.nl) website, built with [Hugo](https://gohugo.io/) and the [Blowfish](https://blowfish.page/) theme.

---

## Guide: Editing Your Person Profile

Each lab member has a profile markdown file located in:
```
content/people/<your-name>.md
```
For example: `content/people/dr-m-h-mike-lees.md`.

### How to Edit on GitHub (Recommended)

You can edit your profile directly in your browser without installing anything locally:

1. **Start from the main repository**:  
   Navigate to the [`content/people/`](content/people/) directory.
2. **Open your file**:  
   Click on your profile markdown file (e.g. `dr-m-h-mike-lees.md`).
3. **Click the Edit button** (the pencil icon in the top-right corner):
   - GitHub will show: *"You need to fork this repository to propose changes."*
   - Click the green **"Fork this repository"** button. This creates your personal editing workspace on GitHub.
4. **Make your updates**:  
   Edit your position description, keywords, links, or bio text below the front matter.
5. **Propose your changes**:  
   Click **"Commit changes..."** in the top-right, and select **"Propose changes"**.
6. **Submit a Pull Request**:  
   Click **"Create pull request"**. A lab maintainer will review and merge it, and the website will automatically deploy via GitHub Actions.

> [!TIP]
> **Editing again in the future**: Always start from the main repository link above. If GitHub ever displays a message on your fork saying your branch is behind `master`, simply click **"Sync fork"** &rarr; **"Update branch"** before editing. Alternatively, you can edit locally via `git clone` if you prefer working in a terminal or code editor.

---

### Profile File Structure

Profile files use standard **YAML front matter** enclosed between `---` delimiters:

```yaml
---
title: "dr. M.H. (Mike) Lees"
date: 2024-01-01
draft: false
description: "Group Leader & Associate Professor"
image: "img/people/dr-m-h-mike-lees.jpg"
group: "Faculty"
active: true
email: "m.h.lees@uva.nl"
website: "http://mhlees.com/"
seniority: 1
domain_keywords:
  - "Computational Social Science"
  - "Complex Systems"
method_keywords:
  - "Agent-Based Modeling (ABM)"
  - "Multi-Scale Simulation"
---
```

---

### Field Descriptions

| Field | Type | Description |
|---|---|---|
| `title` | String | Your academic title and full name, e.g. `"dr. M.H. (Mike) Lees"` or `"A. (Alex) Gabel MSc"` |
| `description` | String | Your role or position in the lab, e.g. `"Full Professor"`, `"Associate Professor"`, `"Assistant Professor"`, `"PhD student"`, `"Postdoctoral Researcher"`, or `"Scientific Programmer"` |
| `image` | String | Path to your photo, e.g. `"img/people/your-name.jpg"`. Photos are placed in [`assets/people/`](assets/people/) |
| `group` | String | The section you appear under on the People page: `"Faculty"`, `"PhDs & Postdocs"`, or `"Other"` |
| `active` | Boolean | `true` if you are a current lab member (displayed on the main People page). Set to `false` when leaving the lab (automatically moves your profile to the [Alumni](content/alumni/) page) |
| `seniority` | Integer | Used for ordering members under Faculty (displayed lowest number first):<br>• `1`: Full Professor / Group Leader<br>• `2`: Associate Professor / Professor Emeritus<br>• `3`: Assistant Professor<br>• `4`: Other Faculty, Postdocs, PhD Students, Support Staff |
| `email` | String | (Optional) Your contact email address |
| `website` | String | (Optional) Link to your personal website, UvA profile page, or LinkedIn |
| `domain_keywords` | List | 1 to 3 application domain keywords describing your research (see below) |
| `method_keywords` | List | 1 to 3 computational method keywords describing your technical methods (see below) |

---

### Research Keywords

To maintain consistency across all profiles, please select your keywords from the official lists:

#### 1. Domain Keywords
Full list is in [`domain-keywords.txt`](domain-keywords.txt):
- `Computational Biomedicine`
- `Computational Biology`
- `Computational Social Science`
- `Computational Sustainability`
- `Computational Ecology`
- `Computational Chemistry`
- `Computational Economics`
- `Computational Finance`
- `Computational Materials Science`
- `Computational Physics`
- `Computational Health`
- `Computational Neuroscience`
- `Computational Psychology`
- `Quantum Simulation`
- `Complex Systems`

#### 2. Method Keywords
Full list is in [`method-keywords.txt`](method-keywords.txt):
- `Multi-Scale Simulation`
- `Network Science`
- `Agent-Based Modeling (ABM)`
- `Digital Twins`
- `Data-Driven Modeling & AI`
- `Information Theory`
- `System Dynamics & Causal Modeling`
- `High-Performance Computing (HPC)`
- `Scientific Machine Learning (SciML)`
- `Quantum Computing`
- `Game Theory`
- `Credibility & Verification`
- `Scientific Visualisation`

#### How to Format Keywords in YAML

Use the list syntax with indentation:

```yaml
domain_keywords:
  - "Computational Biomedicine"
  - "Complex Systems"

method_keywords:
  - "Multi-Scale Simulation"
  - "Data-Driven Modeling & AI"
```

Alternatively, bracket format is also supported:
```yaml
domain_keywords: ["Computational Biomedicine", "Complex Systems"]
method_keywords: ["Multi-Scale Simulation", "Data-Driven Modeling & AI"]
```

---

### Profile Photo Guidelines

1. **Location**: Place your photo inside the [`assets/people/`](assets/people/) folder.
2. **Format**: JPG or PNG (use a square aspect ratio; the website crops it into a circle).
3. **Reference**: Set `image: "img/people/<filename>.jpg"` in your markdown front matter.
4. If no photo is provided, a placeholder avatar will automatically be displayed.

---

### Adding a New Person

To add a new lab member:

1. Create a new markdown file in `content/people/` following the naming convention `<first-initial>-<lastname>-<degree>.md` (e.g., `j-doe-phd.md`), or run:
   ```bash
   hugo new content/people/j-doe-phd.md
   ```
2. Add your photo to `assets/people/` and fill in your front matter fields.

---

### Testing Locally

To preview your changes locally before committing:

```bash
hugo server
```
Then visit `http://localhost:1313/people` in your browser.
