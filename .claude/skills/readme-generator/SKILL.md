---
name: readme-generator
description: Generate GitHub profile README.md from career data. Use when creating or updating GitHub profile page with auto-generated content from resume and career files.
allowed-tools: Read, Write, Glob
context: fork
---

# README Generator Skill

## Purpose
Create a **professional GitHub profile README.md** optimized for the **Korean job market**, focusing on concrete projects and essential hiring information.

## Task
Generate `README.md` (GitHub profile page) by synthesizing:
- `RESUME.md` - For extracting top projects
- `basic_info.md` - Static info (name, contact, education, military, certs)
- `what_i_did_*.md` - For extracting specific project names
- Current GitHub profile style (if existing README.md present)

## Instructions

### Step 1: Read Source Data

Read the following files (if they exist):
- `basic_info.md` - **PRIMARY SOURCE** for static info (name, contact, education, military, certs, career)
- `RESUME.md` - For extracting top projects and achievements
- `what_i_did_*.md` - For specific project names and details
- Existing `README.md` - To preserve user's preferred style/badges

### Step 2: Extract Key Information

From the source files, identify:
- **Name and title** (e.g., "조승준 | Backend Developer")
- **Current role and company**
- **Tech stack** (primary languages, frameworks, tools)
- **Top 3-5 highlights** (biggest achievements with metrics)
- **Certifications and credentials**
- **Community involvement** (meetups, conferences, open source)
- **Contact/links** (email, LinkedIn, blog, etc.)

### Step 3: Design README Structure (Korean Job Market)

**CRITICAL**: For Korean job market, README should be:
- **한글로 작성** (Write entirely in Korean)
- **구체적인 프로젝트 중심** (Focus on concrete project names, not vague metrics)
- **채용 필수 정보 포함** (Include education and military service - mandatory for Korean hiring)

#### Required Structure:

**1. Header**
- 이름 (Name in Korean)
- 직함 (Title in Korean)
- 한 줄 소개 (One-line intro in Korean)

**2. 기술 스택 (Tech Stack)**
- Core technologies only (8-10 badges max)
- Ordered by importance

**3. 경력 (Career)**
- Current company + role + dates
- Previous company + role + dates
- Keep it brief (2-3 lines total)

**4. 주요 프로젝트 (Key Projects)** ⭐ MOST IMPORTANT
- **Use specific project NAMES**, not vague achievements
- Good: "K-water 소양강댐 AI 관제 시스템 - CLIP 모델 최적화, 36대 CCTV 실시간 모니터링"
- Bad: "CPU usage reduced by 50%" (doesn't say WHAT you built)
- Include 3-4 top projects with:
  - Project name (client + system name)
  - What you built
  - Key technologies or achievements

**5. 학력 및 병역 (Education & Military)** ⭐ REQUIRED FOR KOREA
- 대학교 (University) - major, status (재학/졸업)
- 고등학교 (High school) - major, graduation
- 병역 (Military) - status (산업기능요원 만기 전역, etc.)

**6. 자격증 (Certifications)**
- AWS certs, Linux Master, etc.
- Include dates

**7. 연락처 (Contact)**
- Links to resume, cover letter
- Email, GitHub

**8. GitHub Stats** (optional)
- GitHub stats widget

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

## Example Output Structure (Korean Market Standard)

```markdown
# 조승준 (UfXpri)

**백엔드 개발자** | AI/ML 인프라 및 실시간 스트리밍 시스템 구축

---

## 🛠️ 기술 스택
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=flat-square&logo=tensorflow&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Kafka](https://img.shields.io/badge/Kafka-231F20?style=flat-square&logo=apache-kafka&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-232F3E?style=flat-square&logo=amazon-aws&logoColor=white)

---

## 💼 경력

**오지큐 (OGQ)** - 백엔드 개발자 (2023.01 ~ 현재)
**지와이네트웍스 (GYnetworks)** - 백엔드 연구원 (2018.09 ~ 2022.12)

---

## 🚀 주요 프로젝트

**K-water 소양강댐 AI 관제 시스템** (2024)
- CLIP 모델 최적화로 CPU 사용량 51.5% 절감 (330% → 160%)
- 36대 CCTV 실시간 모니터링 시스템 구축

**네이버 MyBox Kafka 비동기 아키텍처** (2025)
- Kafka 기반 대용량 이미지 처리 파이프라인 설계
- GPU 비용 효율화 및 Capacity Planning

**DNA+ 드론 5G 실시간 전송 시스템** (2023)
- C++ 레거시 코드 통합 및 KLV 데이터 실시간 스트리밍
- 드론 영상 5G 전송 프로토콜 구현

**경찰청 Police Lab 2.0 백엔드** (2024)
- Docker 이미지 60% 경량화 (35GB → 12GB)
- Ansible 기반 폐쇄망 배포 자동화

---

## 🎓 학력 및 병역

**인하대학교** 소프트웨어융합공학과 재학 (2025.03 ~)
**인천전자마이스터고** 정보통신기기과 졸업 (2019.01)
**병역** 산업기능요원 만기 전역 (2021.02 ~ 2023.12)

---

## 🏅 자격증

**AWS Certified Solutions Architect – Associate** (2023.10)
**AWS Certified Cloud Practitioner** (2022.10)
**리눅스마스터 1급** (2022.12)

---

## 📫 연락처

📄 [이력서](./RESUME.md) • 💌 [커버레터](./COVER_LETTER.md)
📧 cfi02222@gmail.com • 🐙 [github.com/ufxpri](https://github.com/ufxpri)

---

## 📊 GitHub Stats
![UfXpri's GitHub stats](https://github-readme-stats.vercel.app/api?username=UfXpri&show_icons=true&theme=radical)
```

## Content Guidelines (Korean Job Market)

### DO:
- ✅ **한글로 작성** - Write everything in Korean (except tech terms)
- ✅ **구체적인 프로젝트명 사용** - Use specific project names (client + system)
  - Good: "K-water 소양강댐 AI 관제 시스템"
  - Bad: "AI monitoring system" or "CPU optimization"
- ✅ **학력/병역 필수 포함** - Always include education and military service
- ✅ **간결하게** - Keep it scannable (3-4 top projects, not 10)
- ✅ **핵심만** - Details go to RESUME.md, only highlights in README
- ✅ **기술 스택 정확히** - Only list technologies actually used (8-10 badges max)

### DON'T:
- ❌ **영어로 작성하지 말것** - Don't write in English (this is for Korean hiring managers)
- ❌ **추상적인 성과** - Don't use vague achievements without project context
  - Bad: "Reduced CPU by 50%" (뭘 했는지 모름)
  - Good: "K-water 시스템에서 CLIP 모델 최적화로 CPU 51.5% 절감"
- ❌ **학력/병역 빠뜨리지 말것** - Never omit education/military (Korean recruiters always check)
- ❌ **너무 길게** - Don't make it too long (aim for 1 screen, 2 max)
- ❌ **모든 프로젝트 나열** - Don't list every project (only top 3-4)

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
