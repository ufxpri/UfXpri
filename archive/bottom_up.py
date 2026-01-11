"""
extractor/bottom_up.py

This module extracts and summarizes raw data from source files (e.g., time series, summaries, feedback) for incremental sections.
"""
import os
import re
from typing import List, Dict

def extract_projects_from_markdown(content: str) -> List[Dict]:
    """
    Extracts project sections from a structured markdown summary.
    Returns a list of project dictionaries.
    """
    projects = []
    # Regex to find project blocks
    project_blocks = re.split(r'\*\*프로젝트명:\*\*', content)[1:]
    for block in project_blocks:
        lines = block.strip().split('\n')
        name = lines[0].strip().replace('*', '').replace(' ', '')
        role = tech = ''
        problem = action = result = ''
        for line in lines[1:]:
            if '역할 및 기여도' in line:
                role = line.split(':', 1)[-1].strip().replace('*', '')
            elif '기술 스택' in line:
                tech = line.split(':', 1)[-1].strip().replace('*', '')
            elif '*Problem:*' in line:
                problem = line.split(':', 1)[-1].strip()
            elif '*Action:*' in line:
                action = line.split(':', 1)[-1].strip()
            elif '*Result:*' in line:
                result = line.split(':', 1)[-1].strip()
        projects.append({
            'name': name,
            'role': role,
            'tech_stack': tech,
            'problem': problem,
            'action': action,
            'result': result
        })
    return projects

def extract_operations_from_markdown(content: str) -> Dict:
    """
    Extracts operation/KPI data from a structured markdown summary.
    Returns a dictionary of operation data.
    """
    op_data = {}
    if '조직 기여 및 운영' in content:
        op_section = content.split('조직 기여 및 운영')[1]
        for line in op_section.split('\n'):
            if '인프라/환경 개선' in line:
                op_data['infra'] = line.split(':', 1)[-1].strip()
            elif '프로세스 개선' in line:
                op_data['process'] = line.split(':', 1)[-1].strip()
            elif '수치화된 KPI' in line:
                op_data['kpi'] = line.split(':', 1)[-1].strip()
    return op_data

def extract_summary_file(path: str) -> Dict:
    """
    Extracts all relevant data from a summary markdown file.
    """
    with open(path, encoding='utf-8') as f:
        content = f.read()
    projects = extract_projects_from_markdown(content)
    operations = extract_operations_from_markdown(content)
    return {
        'file': path,
        'projects': projects,
        'operations': operations
    }

def extract_raw_entries(source_dir: str) -> List[Dict]:
    """
    Extracts all summary markdown files in the directory.
    """
    entries = []
    for root, _, files in os.walk(source_dir):
        for fname in files:
            if fname.endswith('.md') and 'Summary' in fname:
                path = os.path.join(root, fname)
                entry = extract_summary_file(path)
                entries.append(entry)
    return entries

# Example usage
if __name__ == "__main__":
    entries = extract_raw_entries("../2025")
    print(entries)
