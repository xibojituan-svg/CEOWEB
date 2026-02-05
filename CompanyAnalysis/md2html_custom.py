
import re
import sys

def parse_markdown(md_content):
    html_lines = []
    html_lines.append("<html><head><meta charset='utf-8'><style>")
    html_lines.append("""
        body { font-family: "Helvetica Neue", Helvetica, Arial, sans-serif; line-height: 1.6; margin: 40px; color: #333; }
        h1 { text-align: center; color: #2c3e50; border-bottom: 2px solid #2c3e50; padding-bottom: 10px; }
        h2 { color: #2980b9; border-bottom: 1px solid #eee; margin-top: 30px; padding-bottom: 5px; }
        ul { margin-bottom: 10px; }
        li { margin-bottom: 5px; }
        p { margin-bottom: 10px; }
        strong { color: #000; font-weight: bold; }
        .page-break { page-break-after: always; }
    """)
    html_lines.append("</style></head><body>")

    lines = md_content.split('\n')
    in_ul = False
    in_nested_ul = False
    
    for line in lines:
        stripped = line.strip()
        
        # Headers
        if line.startswith('# '):
            if in_nested_ul: html_lines.append("</ul>"); in_nested_ul = False
            if in_ul: html_lines.append("</ul>"); in_ul = False
            html_lines.append(f"<h1>{line[2:]}</h1>")
            continue
        if line.startswith('## '):
            if in_nested_ul: html_lines.append("</ul>"); in_nested_ul = False
            if in_ul: html_lines.append("</ul>"); in_ul = False
            html_lines.append(f"<h2>{line[3:]}</h2>")
            continue
            
        # Lists
        if line.startswith('* '):
            if in_nested_ul: html_lines.append("</ul>"); in_nested_ul = False
            if not in_ul:
                html_lines.append("<ul>")
                in_ul = True
            content = line[2:]
            content = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', content)
            html_lines.append(f"<li>{content}</li>")
            continue
            
        if line.startswith('    * '):
            if not in_ul: # Should not happen based on structure but safety first
                html_lines.append("<ul>")
                in_ul = True
            if not in_nested_ul:
                html_lines.append("<ul>") # This is technically invalid HTML (ul inside ul without li), but browsers/printers often handle it, or we should put it in previous li. 
                # Better approach: close the previous LI? No, nested lists should be inside LI. 
                # For simplicity in this specific document structure, let's just make it a deeper list.
                in_nested_ul = True
            
            content = line[6:]
            content = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', content)
            html_lines.append(f"<li>{content}</li>")
            continue
            
        # Close lists if not a list line and not empty
        if stripped and not line.startswith('*') and not line.startswith('    *'):
            if in_nested_ul: html_lines.append("</ul>"); in_nested_ul = False
            if in_ul: html_lines.append("</ul>"); in_ul = False
        
        # HR
        if line.startswith('---'):
            html_lines.append("<hr/>")
            continue
            
        # Paragraphs
        if stripped:
            content = line
            content = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', content)
            html_lines.append(f"<p>{content}</p>")
    
    if in_nested_ul: html_lines.append("</ul>")
    if in_ul: html_lines.append("</ul>")
    
    html_lines.append("</body></html>")
    return "\n".join(html_lines)

if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    html = parse_markdown(content)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html)
