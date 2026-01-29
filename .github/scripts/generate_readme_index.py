#!/usr/bin/env python3
import re
from pathlib import Path

EXCLUDED_DIRS={'.git','.github','__pycache__'}
EXCLUDED_FILES={'README.md','CONTRIBUTING.md','INFO.md','LICENSE'}

ROOT=Path('.')
START='<!-- AUTO-GENERATED-INDEX:START -->'
END='<!-- AUTO-GENERATED-INDEX:END -->'

def write_readme(path:Path,lines):
    readme=path/'README.md'
    block=f"{START}\n"+'\n'.join(lines)+f"\n{END}"
    if readme.exists():
        content=readme.read_text(encoding='utf-8')
        if START in content and END in content:
            content=re.sub(
                re.escape(START)+'.*?'+re.escape(END),
                block,
                content,
                flags=re.DOTALL
            )
        else:
            content=content.rstrip()+"\n\n"+block
    else:
        content=f"# {path.name}\n\n{block}"
    readme.write_text(content,encoding='utf-8')

def generate_root_readme():
    lines=[
        f"- [{d.name}](/{d.name})"
        for d in sorted(ROOT.iterdir())
        if d.is_dir() and d.name not in EXCLUDED_DIRS
    ]
    write_readme(ROOT,lines)

def generate_section_readme(section:Path):
    lines=[]

    for d in sorted(section.iterdir()):
        if not d.is_dir() or d.name in EXCLUDED_DIRS:
            continue
        lines.append(f"- [{d.name}](/{d.as_posix()})")
        for f in sorted(d.glob('*.md')):
            if f.name in EXCLUDED_FILES:
                continue
            rel=f.relative_to(section).as_posix()
            lines.append(f"  - [{rel}](/{f.as_posix()})")

    for f in sorted(section.glob('*.md')):
        if f.name in EXCLUDED_FILES:
            continue
        lines.append(f"- [{f.name}](/{f.as_posix()})")

    write_readme(section,lines)

if __name__=='__main__':
    generate_root_readme()
    for d in sorted(ROOT.iterdir()):
        if d.is_dir() and d.name not in EXCLUDED_DIRS:
            generate_section_readme(d)