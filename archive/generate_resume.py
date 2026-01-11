import os
import glob
from openai import OpenAI

# Configuration
BASE_DIR = r"g:\내 드라이브\03_회사\00_커리어"
PROFILE_FILE = os.path.join(BASE_DIR, "Profile.md")
OUTPUT_FILE = os.path.join(BASE_DIR, "RESUME.md")

def load_env_file():
    """Load .env file from the current directory if it exists."""
    env_path = os.path.join(BASE_DIR, ".env")
    if os.path.exists(env_path):
        print(f"Loading .env from {env_path}")
        with open(env_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                if '=' in line:
                    key, value = line.split('=', 1)
                    value = value.strip().strip("'").strip('"')
                    os.environ[key.strip()] = value

def get_api_key():
    """Get OpenAI API key from environment variable or user input."""
    load_env_file()
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("OPENAI_API_KEY not found in environment variables.")
        api_key = input("Please enter your OpenAI API key: ").strip()
    return api_key

def read_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return ""

def get_summaries():
    """Find and read all Summary_*_AI.md files."""
    summaries = []
    pattern = os.path.join(BASE_DIR, "**", "Summary_*_AI.md")
    files = glob.glob(pattern, recursive=True)
    
    # Sort by year (extracted from filename) descending
    # Filename format expected: Summary_2024_AI.md
    def extract_year(filepath):
        basename = os.path.basename(filepath)
        # Simple extraction assumes 4 digits in name
        import re
        match = re.search(r'\d{4}', basename)
        return int(match.group()) if match else 0
        
    files.sort(key=extract_year, reverse=True)
    
    print(f"Found {len(files)} annual summary files.")
    
    for f in files:
        year = extract_year(f)
        content = read_file(f)
        if content:
            summaries.append(f"\n\n## Year {year}\n{content}")
            
    return "".join(summaries)

def generate_resume(api_key):
    # 1. Gather Data
    print("Reading Profile...")
    profile_content = read_file(PROFILE_FILE)
    
    print("Gathering Yearly Summaries...")
    summaries_content = get_summaries()
    
    if not profile_content and not summaries_content:
        print("No content found to generate resume.")
        return

    full_context = f"""
# CANDIDATE PROFILE
{profile_content}

# ANNUAL PERFORMANCE SUMMARIES
{summaries_content}
"""
    print(f"Total context length: {len(full_context)} characters.")

    # 2. Choose Model
    model_name = input("Enter model to use (default: gpt-4o, or type 'o1-preview'): ").strip() or "gpt-4o"
    print(f"Using model: {model_name}")

    # 3. Construct Prompt
    client = OpenAI(api_key=api_key)
    
    system_instruction = """
You are a top-tier Resume Writer and Career Consultant for high-level software engineers.
Your task is to synthesize the provided candidate profile and annual performance summaries into a single, highly professional RESUME in Markdown format.

## GUIDELINES:
1.  **Structure**:
    -   **Header**: Name, Title, Contact Info (from Profile), one-line value proposition.
    -   **Professional Summary**: 3-4 sentence powerful summary of the candidate's career, strengths, and impact.
    -   **Technical Skills**: Aggregate skills from all years. Group them logically (e.g., Languages, Frameworks, AI/ML, DevOps).
    -   **Work Experience**: Reverse chronological order. Consolidate yearly summaries into role-based entries.
        -   Focus on **Impact** and **Results** (numbers, percentages) rather than just tasks.
        -   Use bullet points.
    -   **Key Projects**: Highlight the top 3-5 most impressive projects across all years.
    -   **Education & Certifications**: From Profile.

2.  **Tone**: Professional, confident, results-oriented.
3.  **Language**: Korean (judging by the input), but Technical terms should be in English where appropriate.
4.  **Formatting**: Clean Markdown with clear headers.

DO NOT simply copy-paste the annual summaries. synthesize them into a coherent career narrative.
"""

    messages = []
    if model_name.startswith("o1"):
        # o1 models support only user role
        messages = [
            {"role": "user", "content": f"{system_instruction}\n\n---\n\nHere is the candidate's data:\n{full_context}"}
        ]
    else:
        messages = [
            {"role": "system", "content": system_instruction},
            {"role": "user", "content": f"Here is the candidate's data:\n{full_context}"}
        ]

    # 4. Call API
    print("Generating Resume (this may take a minute)...")
    try:
        kwargs = {
            "model": model_name,
            "messages": messages
        }
        if not model_name.startswith("o1"):
             kwargs["temperature"] = 0.5 # Lower temp for professional consistency

        response = client.chat.completions.create(**kwargs)
        resume_content = response.choices[0].message.content
        
        # 5. Save
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            f.write(resume_content)
            
        print(f"\nSuccess! RESUME generated at: {OUTPUT_FILE}")
        
    except Exception as e:
        print(f"Error generating resume: {e}")

if __name__ == "__main__":
    key = get_api_key()
    if key:
        generate_resume(key)
