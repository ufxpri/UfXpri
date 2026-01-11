import os
import glob
from openai import OpenAI

# Configuration
BASE_DIR = r"g:\내 드라이브\03_회사\00_커리어"
GUIDE_FILE = os.path.join(BASE_DIR, "summary_guide.md")

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
                    # Remove surrounding quotes if present
                    value = value.strip().strip("'").strip('"')
                    os.environ[key.strip()] = value

def get_api_key():
    """Get OpenAI API key from environment variable or user input."""
    # Try loading .env first
    load_env_file()
    
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("OPENAI_API_KEY not found in environment variables.")
        api_key = input("Please enter your OpenAI API key: ").strip()
    return api_key

def read_file_content(filepath):
    """Read content of a file, returning empty string on failure."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"Skipping file/Could not read {filepath}: {e}")
        return ""

def get_year_content(year_dir):
    """Recursively read all text-based files in the year directory."""
    all_content = []
    
    # Extensions to look for
    extensions = ['*.md', '*.txt', '*.html', '*.json', '*.csv']
    
    print(f"Scanning directory: {year_dir}")
    
    files_found = []
    for ext in extensions:
        # Recursive search for files
        files_found.extend(glob.glob(os.path.join(year_dir, '**', ext), recursive=True))
    
    # Remove duplicates if any (though glob with different extensions shouldn't overlap)
    files_found = sorted(list(set(files_found)))
    
    print(f"Found {len(files_found)} files.")
    
    for filepath in files_found:
        # Skip the output file itself if it exists to avoid loop
        if "Summary_" in os.path.basename(filepath) and "_AI.md" in os.path.basename(filepath):
            continue
            
        print(f"Reading: {filepath}")
        content = read_file_content(filepath)
        if content:
            relative_path = os.path.relpath(filepath, year_dir)
            all_content.append(f"\n--- FILE: {relative_path} ---\n")
            all_content.append(content)
            
    return "".join(all_content)

def summarize_year(year, api_key):
    year_dir = os.path.join(BASE_DIR, str(year))
    
    if not os.path.exists(year_dir):
        print(f"Directory for year {year} not found at {year_dir}")
        return

    # 1. Read the Guide
    print("Reading summary guide...")
    guide_content = read_file_content(GUIDE_FILE)
    if not guide_content:
        print("Failed to read summary_guide.md. Please check the file path.")
        return

    # 2. Read Year Content
    print("Reading year content...")
    year_content = get_year_content(year_dir)
    if not year_content:
        print("No content found for this year.")
        return
    
    print(f"Total content length: {len(year_content)} characters.")

    # 3. Choose Model
    model_name = input("Enter model to use (default: gpt-4o, or type 'o1-preview'): ").strip() or "gpt-4o"
    print(f"Using model: {model_name}")

    # 3. Call OpenAI API
    print("Initializing OpenAI client...")
    client = OpenAI(api_key=api_key)
    
    system_prompt = f"""
You are an expert career coach and technical writer. 
Your task is to summarize the provided career records for the year {year} following the strict guidelines below.

GUIDELINES:
{guide_content}

Output the result in Markdown format.
"""
    
    messages = []
    if model_name.startswith("o1"):
        # o1 models do not support 'system' role in beta, use 'user' instead
        print("Note: Using user role for implementation instructions for o1 model.")
        combined_content = f"{system_prompt}\n\nHere is the content for the year {year}:\n\n{year_content}"
        messages = [
            {"role": "user", "content": combined_content}
        ]
    else:
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Here is the content for the year {year}:\n\n{year_content}"}
        ]

    print("Sending request to OpenAI API (this may take a minute)...")
    try:
        # Provide max_completion_tokens for o1 if needed, otherwise standard
        # o1-preview uses max_completion_tokens, gpt-4o uses max_tokens (optional)
        
        # Note: o1-preview does not support temperature currently (fixed at 1)
        kwargs = {
            "model": model_name,
            "messages": messages
        }
        
        if not model_name.startswith("o1"):
             kwargs["temperature"] = 0.7

        response = client.chat.completions.create(**kwargs)
        
        summary = response.choices[0].message.content
        
        # 4. Save Output
        output_filename = f"Summary_{year}_AI.md"
        output_path = os.path.join(year_dir, output_filename)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(summary)
            
        print(f"\nSuccess! Summary saved to: {output_path}")
        
    except Exception as e:
        print(f"Error communicating with OpenAI: {e}")

if __name__ == "__main__":
    print(f"Base Directory: {BASE_DIR}")
    target_year_input = input("Enter the year you want to summarize (e.g., 2024). Leave empty to summarize ALL years: ").strip()
    
    key = get_api_key()
    if not key:
        print("No API Key provided. Exiting.")
        exit()

    if target_year_input:
        # Process single year
        summarize_year(target_year_input, key)
    else:
        # Process all years
        print("\nNo year specified. Scanning for all year directories...")
        all_items = os.listdir(BASE_DIR)
        years = []
        for item in all_items:
            # Check if it's a directory and looks like a year (4 digits)
            if os.path.isdir(os.path.join(BASE_DIR, item)) and item.isdigit() and len(item) == 4:
                years.append(item)
        
        years.sort()
        if not years:
            print("No year directories found.")
        else:
            print(f"Found years: {', '.join(years)}")
            for year in years:
                print(f"\n{'='*30}\nProcessing Year: {year}\n{'='*30}")
                summarize_year(year, key)
