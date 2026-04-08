import os
import codecs
import re

app_py_path = r"d:\Terraform IaC\iac-generator\backend\app.py"
templates_dir = r"d:\Terraform IaC\iac-generator\backend\templates"
index_html_path = os.path.join(templates_dir, "index.html")

os.makedirs(templates_dir, exist_ok=True)

with codecs.open(app_py_path, "r", encoding="utf-8") as f:
    content = f.read()

# Try to extract INDEX_HTML
match = re.search(r'INDEX_HTML\s*=\s*"""(.*?)"""', content, flags=re.DOTALL)
if match:
    html_content = match.group(1).strip()
    
    # 1. Update HTML: single line hero text
    html_content = html_content.replace('<h1 class="hero-title"><span class="gradient-text">Modern Infrastructure as Code,</span><br>Now with Agentic AI.</h1>',
                                        '<h1 class="hero-title" style="white-space: nowrap;"><span class="gradient-text">Modern Infrastructure as Code,</span> Now with Agentic AI.</h1>')
    
    # 2. Add marquee CSS and HTML
    marquee_css = """
        .marquee-container {
            width: 100%;
            overflow: hidden;
            background: #ffffff;
            padding: 40px 0;
            white-space: nowrap;
            position: relative;
            margin-top: 50px;
        }
        .marquee-container:before, .marquee-container:after {
            content: "";
            position: absolute;
            top: 0;
            width: 150px;
            height: 100%;
            z-index: 2;
        }
        .marquee-container:before { left: 0; background: linear-gradient(to right, white, transparent); }
        .marquee-container:after { right: 0; background: linear-gradient(to left, white, transparent); }
        
        .marquee-content {
            display: inline-block;
            animation: marquee 30s linear infinite;
        }
        @keyframes marquee {
            0%   { transform: translate3d(0, 0, 0); }
            100% { transform: translate3d(-50%, 0, 0); }
        }
        .marquee-item {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            height: 40px;
            margin: 0 40px;
            filter: grayscale(100%) opacity(60%);
            transition: all 0.2s;
        }
        .marquee-item:hover {
            filter: grayscale(0%) opacity(100%);
        }
        .marquee-item img {
            max-height: 100%;
        }
    """
    html_content = html_content.replace('/* New Landing Page Styles */', '/* New Landing Page Styles */' + marquee_css)
    
    marquee_html = """
        <div style="width: 100%; text-align: center; color: #666; font-size: 14px; margin-top: 60px;">Trusted by over 3,700 innovative companies</div>
        <div class="marquee-container">
            <div class="marquee-content">
                <!-- First set -->
                <div class="marquee-item"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/docker/docker-original-wordmark.svg" alt="Docker"></div>
                <div class="marquee-item"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/unity/unity-original-wordmark.svg" style="filter: invert(1); max-height: 50px;" alt="Unity"></div>
                <div class="marquee-item"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/github/github-original-wordmark.svg" style="filter: invert(1); max-height: 50px;" alt="GitHub"></div>
                <div class="marquee-item"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/azure/azure-original-wordmark.svg" alt="Azure"></div>
                <div class="marquee-item"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/supabase/supabase-original-wordmark.svg" alt="Supabase"></div>
                <div class="marquee-item"><b style="font-size:24px; color:#111;">Moderna</b></div>
                <div class="marquee-item"><b style="font-size:24px; color:#111;">Deloitte.</b></div>
                <div class="marquee-item"><b style="font-size:24px; color:#111;">STOKE</b></div>
                <!-- Duplicate set for seamless looping -->
                <div class="marquee-item"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/docker/docker-original-wordmark.svg" alt="Docker"></div>
                <div class="marquee-item"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/unity/unity-original-wordmark.svg" style="filter: invert(1); max-height: 50px;" alt="Unity"></div>
                <div class="marquee-item"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/github/github-original-wordmark.svg" style="filter: invert(1); max-height: 50px;" alt="GitHub"></div>
                <div class="marquee-item"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/azure/azure-original-wordmark.svg" alt="Azure"></div>
                <div class="marquee-item"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/supabase/supabase-original-wordmark.svg" alt="Supabase"></div>
                <div class="marquee-item"><b style="font-size:24px; color:#111;">Moderna</b></div>
                <div class="marquee-item"><b style="font-size:24px; color:#111;">Deloitte.</b></div>
                <div class="marquee-item"><b style="font-size:24px; color:#111;">STOKE</b></div>
            </div>
        </div>
    """
    
    # Insert marquee below hero buttons
    html_content = html_content.replace('<button class="btn-secondary">Contact Us</button>\n            </div>\n        </div>',
                                        '<button class="btn-secondary">Contact Us</button>\n            </div>\n        </div>\n' + marquee_html)
    
    # 3. Update Landing Page Background to White
    html_content = html_content.replace('background: #0a0a0a; z-index: 10;', 'background: #ffffff; z-index: 10; color: #111;')
    html_content = html_content.replace('.hero-subtitle { font-size: 18px; color: #999;', '.hero-subtitle { font-size: 18px; color: #555;')
    html_content = html_content.replace('.landing-header .nav-links { display: flex; gap: 30px; align-items: center; font-size: 14px; color: #aaa; font-weight: 500;}',
                                        '.landing-header .nav-links { display: flex; gap: 30px; align-items: center; font-size: 14px; color: #555; font-weight: 500;}')
    html_content = html_content.replace('.landing-header .nav-links a { color: #ccc;', '.landing-header .nav-links a { color: #333;')
    html_content = html_content.replace('.landing-header .nav-links a:hover { color: #fff; }', '.landing-header .nav-links a:hover { color: #000; }')
    html_content = html_content.replace('.landing-header { display: flex; justify-content: space-between; align-items: center; padding: 10px 40px; border-bottom: 1px solid #222;',
                                        '.landing-header { display: flex; justify-content: space-between; align-items: center; padding: 10px 40px; border-bottom: 1px solid #eee;')
    
    # Save the extracted template
    with codecs.open(index_html_path, "w", encoding="utf-8") as t:
        t.write("<!DOCTYPE html>\n" + html_content)

    # 4. Modify app.py to remove INDEX_HTML and use render_template
    # Replace first block
    content = content.replace('from flask import Flask, request, jsonify, Response, stream_with_context',
                              'from flask import Flask, request, jsonify, Response, stream_with_context, render_template')
    
    content = re.sub(r'INDEX_HTML\s*=\s*""".*?"""', '', content, flags=re.DOTALL)
    
    content = content.replace('def index():\n    return INDEX_HTML', 'def index():\n    return render_template("index.html")')
    
    with codecs.open(app_py_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Extraction and modification successful")
else:
    print("Could not find INDEX_HTML block in app.py")
