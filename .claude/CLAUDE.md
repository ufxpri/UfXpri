# Resume Generation Pipeline - Project Memory

## Project Overview
This is a **career management and resume generation system** that uses Claude Code skills to intelligently process career data through a three-stage pipeline.

## Architecture: Extract → Synthesize → Translate

### Stage 1: Extractor (resume-extractor skill)
**Purpose**: Transform raw yearly career documents into structured components

**Input**:
- Yearly directories (e.g., `2024/`)
- Raw markdown files: quarterly reviews, project descriptions, retrospectives

**Output** (per year):
- `what_i_did_YYYY.md` - Factual accomplishments and deliverables
- `my_thoughts_YYYY.md` - Reflections, learnings, personal growth
- `performance_YYYY.md` - Quantifiable metrics and business impact

**Why this matters**: Separating facts from reflections from metrics makes synthesis much more intelligent and flexible.

### Stage 2: Synthesizer (resume-synthesizer skill)
**Purpose**: Create a cohesive professional resume from structured components

**Input**:
- All `what_i_did_*.md` files (all years)
- All `my_thoughts_*.md` files (all years)
- All `performance_*.md` files (all years)
- `Profile.md` (personal info, education)

**Output**:
- `RESUME.md` - Professional resume with:
  - Header & value proposition
  - Professional summary
  - Technical skills
  - Work experience (chronological, impact-focused)
  - Education & certifications

**Why this matters**: LLM can intelligently connect learnings to results, identify career progression patterns, and craft compelling narratives.

### Stage 3: Translator (resume-translator skill)
**Purpose**: Adapt resume for different formats, languages, or audiences

**Input**:
- `RESUME.md` (or any resume file)

**Output** (examples):
- `RESUME_EN.md` - English translation
- `RESUME_technical.md` - Adapted for technical IC roles
- `RESUME_manager.md` - Adapted for engineering manager roles
- `RESUME.pdf` - PDF format
- `RESUME.html` - Web format

**Why this matters**: One source of truth, many audience-specific versions. No manual rewriting needed.

## File Structure

```
G:\내 드라이브\03_회사\00_커리어/
├── .claude/
│   ├── CLAUDE.md                                    [this file]
│   └── skills/
│       ├── resume-extractor/
│       │   └── SKILL.md                             [extraction logic]
│       ├── resume-synthesizer/
│       │   └── SKILL.md                             [synthesis logic]
│       └── resume-translator/
│           └── SKILL.md                             [translation logic]
│
├── Profile.md                                       [personal info, education]
│
├── 2024/
│   ├── 1분기.md, 2분기.md, 3분기.md, 4분기.md        [raw quarterly data]
│   ├── Project_Timeline.md                          [raw project data]
│   ├── what_i_did_2024.md                           [extracted: accomplishments]
│   ├── my_thoughts_2024.md                          [extracted: reflections]
│   ├── performance_2024.md                          [extracted: metrics]
│   └── Summary_2024_AI.md                           [legacy AI summary]
│
├── 2023/
│   └── [same structure]
│
├── RESUME.md                                        [synthesized resume]
├── RESUME_EN.md                                     [translated to English]
├── RESUME_technical.md                              [adapted for IC roles]
│
└── archive/
    └── generate_resume.py                           [legacy Python script]
```

## Usage Workflow

### Initial Setup (One-time)
1. Organize yearly career data into directories (2020/, 2021/, etc.)
2. Create/update `Profile.md` with personal info

### Regular Usage

#### Extract yearly data (do this once per year)
```
User: "Extract 2024 career data"
Claude: [Invokes resume-extractor skill automatically]
        → Reads 2024/*.md files
        → Generates what_i_did_2024.md, my_thoughts_2024.md, performance_2024.md
```

#### Generate resume (do this when needed)
```
User: "Generate my resume"
Claude: [Invokes resume-synthesizer skill automatically]
        → Reads all what_i_did_*.md, my_thoughts_*.md, performance_*.md
        → Reads Profile.md
        → Generates RESUME.md
```

#### Translate/adapt resume (do this for applications)
```
User: "Create an English version for a technical role at Google"
Claude: [Invokes resume-translator skill automatically]
        → Reads RESUME.md
        → Translates to English
        → Adapts for technical IC audience
        → Emphasizes distributed systems, scale
        → Generates RESUME_EN_technical_google.md
```

## Key Design Principles

### 1. File-Based Pipeline
- Each stage produces **observable intermediate files**
- Easy to debug: inspect files at each stage
- Easy to iterate: edit files manually if needed
- Resilient: re-run only failed stages

### 2. LLM-Powered Intelligence
- No rigid parsing or templates
- Handles variations in file structure gracefully
- Self-corrects when encountering unexpected formats
- Provides reasoning for categorization decisions

### 3. Separation of Concerns
- **Facts** (what_i_did) vs **Reflections** (my_thoughts) vs **Metrics** (performance)
- Makes synthesis more intelligent
- Enables flexible combination strategies

### 4. One Source of Truth
- Raw yearly data → Extracted components → Synthesized resume → Translated versions
- No manual copy-paste
- Changes to raw data propagate through pipeline

## Migration from Old System

### Old Python Script (`generate_resume.py`)
- **Extractor**: `get_summaries()` - simple glob + read
- **Synthesizer**: OpenAI API call with prompt
- **Translator**: Implicit in system prompt (language handling)

**Problems**:
- ❌ Tight coupling (in-memory strings)
- ❌ Not inspectable (black box)
- ❌ Hard to debug
- ❌ Requires API key management

### New Skills System
- **Extractor**: resume-extractor skill
- **Synthesizer**: resume-synthesizer skill
- **Translator**: resume-translator skill

**Advantages**:
- ✅ Loose coupling (file-based)
- ✅ Inspectable (MD files at each stage)
- ✅ Easy to debug (check intermediate outputs)
- ✅ No API key needed (uses Claude Code's model)
- ✅ Automatic invocation (skills auto-trigger)
- ✅ Self-correcting (LLM handles edge cases)

## Common Tasks

### Add new year's data
1. Create `YYYY/` directory
2. Add quarterly reviews, project files, etc.
3. Run: "Extract YYYY career data"

### Update existing resume
1. Edit raw yearly files (e.g., `2024/1분기.md`)
2. Run: "Re-extract 2024 data"
3. Run: "Regenerate resume"

### Create role-specific resume
1. Run: "Create a version for [target role] at [company]"
2. Example: "Create a version for Engineering Manager at Netflix"

### Translate to another language
1. Run: "Translate resume to [language]"
2. Example: "Translate resume to English"

### Debug extraction
1. Check: `YYYY/what_i_did_YYYY.md` - Are accomplishments captured?
2. Check: `YYYY/my_thoughts_YYYY.md` - Are learnings captured?
3. Check: `YYYY/performance_YYYY.md` - Are metrics captured?
4. If incorrect: Edit manually or provide feedback to re-extract

### Debug synthesis
1. Check: `RESUME.md` - Is narrative coherent?
2. Check: Are metrics from performance files included?
3. Check: Is career progression clear?
4. If incorrect: Run "Regenerate resume with focus on [X]"

## Tips for Best Results

### For Extraction
- Keep raw yearly files well-organized (by quarter or project)
- Include dates and numbers in raw data
- Separate different types of content (don't mix retrospectives with project docs)

### For Synthesis
- Ensure Profile.md is up-to-date
- Be specific when requesting resume: "Focus on leadership" vs "Focus on technical depth"
- Iterate: Generate → Review → Refine → Regenerate

### For Translation
- Specify target: "Technical IC at Google" vs "EM at startup"
- Provide context: Company culture, role requirements
- Request multiple versions for different applications

## Troubleshooting

### Skill not triggering automatically?
- Ensure `.claude/skills/*/SKILL.md` exists
- Check skill description matches your request
- Try more explicit language: "Use resume-synthesizer skill"

### Extraction categorizing incorrectly?
- Provide more context in raw files
- Or: Manually edit extracted files
- Or: Give feedback: "Re-extract, treating project docs as accomplishments"

### Resume too generic?
- Request specific focus: "Emphasize distributed systems experience"
- Or: Use translator skill to adapt for audience

### Missing content in resume?
- Check intermediate files (what_i_did, my_thoughts, performance)
- If missing there: Re-extract with guidance
- If present there but not in resume: Request "Regenerate resume including all performance metrics"

## Future Enhancements

- Slash commands for common workflows (`/extract-all-years`, `/update-resume`)
- Hooks to auto-extract when new yearly files are added
- Support for multiple resume templates (academic, startup, corporate)
- Integration with job description matching (analyze JD, adapt resume)
- Version control and diff tracking for resume changes
