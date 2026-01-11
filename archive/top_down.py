"""
synthesizer/top_down.py

This module synthesizes the structured data into Markdown resume sections in the professional order.
"""
from typing import List, Dict

# TODO: Integrate LangChain for section synthesis and Markdown formatting

def synthesize_resume(structured_entries: List[Dict], section_order: List[str]) -> str:
    """
    Synthesizes the resume in Markdown format from structured entries and section order.
    """
    # Placeholder: just list entries for now
    md = "# Resume\n\n"
    for section in section_order:
        md += f"## {section}\n\n"
        for entry in structured_entries:
            md += f"- {entry.get('file', '')}\n"
        md += "\n"
    return md

# Example usage
if __name__ == "__main__":
    from translator.translate_and_reorder import translate_and_reorder
    from extractor.bottom_up import extract_raw_entries
    import yaml
    with open("../config/section_mapping.yaml", encoding='utf-8') as f:
        config = yaml.safe_load(f)
    raw = extract_raw_entries("../2025")
    structured = translate_and_reorder(raw)
    md = synthesize_resume(structured, config['section_order'])
    print(md)
