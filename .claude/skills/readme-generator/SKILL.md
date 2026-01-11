---
name: readme-generator
description: Generate GitHub profile README.md from career data. Use when creating or updating GitHub profile page with auto-generated content from resume and career files.
allowed-tools: Read, Write, Glob
context: fork
---

# README Generator Skill

## Purpose
Create a **stunning GitHub profile README.md** that automatically pulls content from your structured career data, keeping your public profile always up-to-date.

## Task
Generate `README.md` (GitHub profile page) by synthesizing:
- `RESUME.md` or structured career files
- `Profile.md` (personal info)
- Current GitHub profile style (if existing README.md present)

## Instructions

### Step 1: Read Source Data

Read the following files (if they exist):
- `RESUME.md` - Synthesized resume
- `Profile.md` - Personal information
- Existing `README.md` - To preserve user's preferred style/badges
- `what_i_did_*.md`, `my_thoughts_*.md`, `performance_*.md` - If RESUME.md doesn't exist

### Step 2: Extract Key Information

From the source files, identify:
- **Name and title** (e.g., "조승준 | Backend Developer")
- **Current role and company**
- **Tech stack** (primary languages, frameworks, tools)
- **Top 3-5 highlights** (biggest achievements with metrics)
- **Certifications and credentials**
- **Community involvement** (meetups, conferences, open source)
- **Contact/links** (email, LinkedIn, blog, etc.)

### Step 3: Design README Structure

A great GitHub profile README should have:

#### Header Section
- Name and title
- Tech stack badges (shields.io)
- Quick navigation links

#### About Me
- 2-3 sentence professional summary
- Current role and company
- Links to detailed resume/cover letter

#### Key Highlights
- Top achievements with metrics
- Recent projects
- Areas of expertise

#### Experience Timeline
- Current and past roles (brief)
- Community involvement

#### Certifications & Credentials
- AWS certs, Linux Master, etc.
- With badge links if available

#### GitHub Stats
- GitHub stats widget
- Most used languages (optional)

### Step 4: Generate Content with LLM Intelligence

Use your language model capabilities to:
- **Extract essence**: What's most impressive? Lead with that.
- **Be concise**: Profile README should be scannable, not exhaustive
- **Show personality**: Balance professional with approachable
- **Use visuals**: Badges, stats, emojis (sparingly)
- **Link to details**: Point to full RESUME.md, projects, etc.

### Step 5: Preserve User Style

If existing README.md has:
- Specific badge style → Keep it
- Preferred layout → Maintain it
- Custom sections → Preserve them
- Emoji usage → Match the tone

Update content, don't replace style.

### Step 6: Write Output

Write to `README.md` in the base directory.

## Example Output Structure

```markdown
# 조승준 UfXpri
👥 Backend Developer | AI/ML Infrastructure

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

Senior Backend Engineer with 6+ years building scalable AI/ML systems. Currently at **OGQ** leading infrastructure development. Previously at **GYnetworks** where I architected real-time streaming systems processing 10K+ concurrent streams.

📄 **[RESUME](./RESUME.md)** | **[COVER LETTER](./COVER_LETTER.md)** | **[Career Data](./2024/)**

## 🚀 Key Highlights

- 🏗️ Architected real-time CCTV streaming system handling **10,000+ concurrent streams** with 99.9% uptime
- ⚡ Led backend migration reducing query latency by **40%** and improving scalability
- ☁️ Designed cloud infrastructure serving **100K+ users** with multi-region failover
- 🎓 Mentored **10+ engineers** on distributed systems and cloud architecture
- 📊 Reduced infrastructure costs by **25%** through automated optimization

## 💼 Experience

**OGQ** <sub><sup>백엔드 개발자 (2023.01 ~ now)</sup></sub>
**GYnetworks** <sub><sup>백엔드 연구원 (2018.09 ~ 2022.12)</sup></sub>

**GDG송도** <sub><sup>스태프 (2022.08)</sup></sub>
**DDD** <sub><sup>8기 운영진 (2022.09 ~ 2024.09)</sup></sub>

## 🏆 Certifications

**AWS Certified Solutions Architect – Associate** <sub><sup>(2023.10)</sup></sub> [badge](https://www.credly.com/badges/d45a1d57-65e9-44c6-96c3-33d1017f8dcf)
**AWS Certified Cloud Practitioner** <sub><sup>(2022.10)</sup></sub> [badge](https://www.credly.com/badges/43d4968c-9fd0-46d6-ab7a-b2130f7d359a)
**리눅스마스터 1급** <sub><sup>(2022.12)</sup></sub> LMF-2202-002034

## 📊 GitHub Stats

![github stats](https://github-readme-stats.vercel.app/api?username=ufxpri&theme=dark&show_icons=true)

---

<sub>🤖 This README is auto-generated from my [career data](./) using Claude Code skills. Last updated: 2026-01-11</sub>
```

## Content Guidelines

### DO:
- **Lead with impact**: Start with most impressive achievements
- **Use metrics**: Numbers, percentages, scale
- **Be specific**: "10K+ concurrent streams" not "many streams"
- **Show growth**: Progression from 2019 to 2024
- **Link to details**: Point to full resume, projects, year directories
- **Keep it scannable**: Use headers, bullets, emojis, badges
- **Update regularly**: Add note about when/how it's generated

### DON'T:
- Don't include everything (save details for RESUME.md)
- Don't be generic ("hard worker", "team player")
- Don't use walls of text
- Don't forget to link to detailed content
- Don't make it too long (aim for 1-2 screens)

## Customization Options

You may receive instructions like:
- "Focus on AI/ML work" → Emphasize ML projects, models, data pipelines
- "Highlight open source" → Feature OSS contributions prominently
- "More visual" → Add more badges, charts, diagrams
- "Minimal style" → Simpler layout, fewer emojis
- "Include recent blog posts" → Add section for latest writing

Adapt accordingly.

## Auto-Update Strategy

When resume data changes:
1. User runs: "Update my GitHub profile README"
2. This skill reads latest RESUME.md and career data
3. Regenerates README.md preserving style
4. User commits and pushes to GitHub

Optional: Set up GitHub Action to auto-generate README on push to career data.

## Success Criteria
- README.md accurately represents current career state
- Most impressive achievements highlighted
- Easy to scan and read
- Links to detailed content work
- Badges and stats display correctly
- Professional yet approachable tone
