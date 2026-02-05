
import re
import sys

def parse_markdown_content(lines):
    html_lines = []
    
    in_ul = False
    in_nested_ul = False
    in_table = False
    table_rows = []
    
    def close_lists():
        nonlocal in_ul, in_nested_ul
        if in_nested_ul: html_lines.append("</ul>"); in_nested_ul = False
        if in_ul: html_lines.append("</ul>"); in_ul = False

    def process_table(rows):
        if not rows: return
        html_lines.append("<table border='1' style='border-collapse: collapse; width: 100%; margin-bottom: 20px;'>")
        
        # Header
        header = rows[0]
        cols = [c.strip() for c in header.strip('|').split('|')]
        html_lines.append("<thead><tr>")
        for c in cols:
            html_lines.append(f"<th style='padding: 8px; background-color: #f2f2f2; text-align: left;'>{format_inline(c)}</th>")
        html_lines.append("</tr></thead>")
        
        # Body
        html_lines.append("<tbody>")
        start_idx = 1
        # Check if second row is separator
        if len(rows) > 1 and set(rows[1].strip()) <= {'|', '-', ':', ' '}:
            start_idx = 2
            
        for row in rows[start_idx:]:
            cols = [c.strip() for c in row.strip('|').split('|')]
            html_lines.append("<tr>")
            for c in cols:
                html_lines.append(f"<td style='padding: 8px; border: 1px solid #ddd;'>{format_inline(c)}</td>")
            html_lines.append("</tr>")
        html_lines.append("</tbody></table>")

    def format_inline(text):
        # Bold
        text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
        # Links
        text = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', text)
        return text

    for i, line in enumerate(lines):
        stripped = line.strip()
        
        # Table detection
        if stripped.startswith('|'):
            close_lists()
            in_table = True
            table_rows.append(stripped)
            continue
        else:
            if in_table:
                process_table(table_rows)
                table_rows = []
                in_table = False

        if not stripped:
            close_lists()
            continue

        # Headers
        if line.startswith('# '):
            close_lists()
            html_lines.append(f"<h1>{format_inline(line[2:])}</h1>")
            continue
        if line.startswith('## '):
            close_lists()
            html_lines.append(f"<h2>{format_inline(line[3:])}</h2>")
            continue
        if line.startswith('### '):
            close_lists()
            html_lines.append(f"<h3>{format_inline(line[4:])}</h3>")
            continue
            
        # Lists
        if line.startswith('* '):
            if in_nested_ul: html_lines.append("</ul>"); in_nested_ul = False
            if not in_ul:
                html_lines.append("<ul>")
                in_ul = True
            html_lines.append(f"<li>{format_inline(line[2:])}</li>")
            continue
            
        if line.startswith('    * ') or line.startswith('\t* '):
            if not in_ul: html_lines.append("<ul>"); in_ul = True
            if not in_nested_ul: html_lines.append("<ul>"); in_nested_ul = True
            html_lines.append(f"<li>{format_inline(line.strip()[2:])}</li>")
            continue
        
        # Close lists if not a list line
        close_lists()
        
        # HR
        if line.startswith('---'):
            html_lines.append("<hr/>")
            continue
            
        # Paragraphs
        html_lines.append(f"<p>{format_inline(trimmed_line(line))}</p>")

    if in_table:
        process_table(table_rows)
    close_lists()
    
    return "\n".join(html_lines)

def trimmed_line(line):
    return line.strip()

def create_html(md_content):
    style = """
        body { font-family: "Helvetica Neue", Helvetica, Arial, sans-serif; line-height: 1.6; margin: 40px; color: #333; max-width: 900px; margin: 40px auto; }
        h1 { text-align: center; color: #2c3e50; border-bottom: 2px solid #2c3e50; padding-bottom: 10px; }
        h2 { color: #2980b9; border-bottom: 1px solid #eee; margin-top: 30px; padding-bottom: 5px; }
        h3 { color: #2c3e50; margin-top: 20px; }
        ul { margin-bottom: 10px; }
        li { margin-bottom: 5px; }
        p { margin-bottom: 10px; }
        strong { color: #000; font-weight: bold; }
        a { color: #2980b9; text-decoration: none; }
        a:hover { text-decoration: underline; }
        hr { border: 0; border-top: 1px solid #eee; margin: 20px 0; }
    """
    
    html = f"""<html>
<head>
    <meta charset='utf-8'>
    <style>{style}</style>
</head>
<body>
{parse_markdown_content(md_content.splitlines())}
</body>
</html>"""
    return html

if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    html_content = create_html(content)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
