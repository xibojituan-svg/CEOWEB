
import csv
import os
import random
import re

# Configuration
SOURCE_CSV = "/Users/jdm/Downloads/xiboceoweb/CompanyAnalysis/SKU销售GMV及占比.csv"
OUTPUT_DIR = "/Users/jdm/Downloads/xiboceoweb/SKU"

# Enhanced Template
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{sku_name} - 职业技能认证与教学质量看板 | Xibo Education</title>
    <style>
        :root {{
            --primary: #FF4500;
            --dark: #1a1a1a;
            --light: #f5f5f5;
            --text: #333;
            --success: #22c55e;
            --warning: #f59e0b;
        }}
        body {{
            font-family: "Helvetica Neue", Helvetica, "PingFang SC", "Microsoft YaHei", sans-serif;
            margin: 0;
            padding: 0;
            color: var(--text);
            background: #fff;
            line-height: 1.6;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }}
        
        /* Breadcrumb */
        .breadcrumb {{
            padding: 20px 0;
            font-size: 0.9rem;
            color: #666;
        }}
        .breadcrumb a {{
            color: #666;
            text-decoration: none;
        }}
        .breadcrumb a:hover {{
            color: var(--primary);
            text-decoration: underline;
        }}
        .breadcrumb span {{
            margin: 0 5px;
            color: #ccc;
        }}

        /* Header */
        header {{
            background: var(--dark);
            color: white;
            padding: 20px 0;
        }}
        header .logo {{
            font-weight: 800;
            font-size: 1.5rem;
            color: var(--primary);
            text-decoration: none;
        }}

        /* Hero */
        .hero {{
            background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
            color: white;
            padding: 80px 0;
            text-align: center;
        }}
        .hero h1 {{
            font-size: 3rem;
            margin-bottom: 20px;
        }}
        .hero p {{
            font-size: 1.2rem;
            opacity: 0.8;
            max-width: 800px;
            margin: 0 auto 40px;
        }}
        .btn {{
            display: inline-block;
            background: var(--primary);
            color: white;
            padding: 15px 40px;
            border-radius: 30px;
            text-decoration: none;
            font-weight: bold;
            transition: all 0.3s;
        }}
        .btn:hover {{
            background: #e03e00;
            transform: translateY(-2px);
        }}

        /* Sections */
        section {{
            padding: 60px 0;
            border-bottom: 1px solid #eee;
        }}
        h2 {{
            text-align: center;
            font-size: 2rem;
            margin-bottom: 50px;
        }}

        /* Product Description */
        .grid-2 {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 50px;
            align-items: start;
        }}
        .feature-list li {{
            margin-bottom: 15px;
            position: relative;
            padding-left: 25px;
            list-style: none;
        }}
        .feature-list li::before {{
            content: "✓";
            color: var(--primary);
            position: absolute;
            left: 0;
            font-weight: bold;
        }}
        
        /* Teacher Profile */
        .teacher-profile {{
            background: #fff;
            border: 1px solid #eee;
            padding: 30px;
            border-radius: 8px;
            text-align: center;
            box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        }}
        .teacher-img {{
            width: 120px;
            height: 120px;
            border-radius: 50%;
            background: #ddd;
            margin: 0 auto 20px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 2rem;
            color: #888;
        }}

        /* Detailed Curriculum Table */
        .curriculum-table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 30px;
            background: white;
            box-shadow: 0 2px 15px rgba(0,0,0,0.05);
        }}
        .curriculum-table th, .curriculum-table td {{
            padding: 15px 20px;
            text-align: left;
            border-bottom: 1px solid #eee;
        }}
        .curriculum-table th {{
            background: #f8fafc;
            font-weight: 600;
            color: var(--dark);
        }}
        .curriculum-table tr:hover {{
            background: #fdfdfd;
        }}
        .module-tag {{
            display: inline-block;
            padding: 2px 8px;
            border-radius: 4px;
            font-size: 0.8rem;
            background: #e0f2fe;
            color: #0284c7;
            margin-right: 5px;
        }}

        /* Simulation Dashboard */
        .dashboard {{
            background: #f8fafc;
            padding: 40px;
            border-radius: 12px;
            border: 1px solid #e2e8f0;
        }}
        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-bottom: 40px;
        }}
        .stat-box {{
            background: white;
            padding: 20px;
            border-radius: 8px;
            text-align: center;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        }}
        .stat-value {{
            font-size: 2.5rem;
            font-weight: 800;
            color: var(--dark);
        }}
        .stat-label {{
            color: #64748b;
            font-size: 0.9rem;
        }}
        
        /* Video Simulation */
        .video-placeholder {{
            background: #000;
            width: 100%;
            height: 400px;
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            flex-direction: column;
            position: relative;
        }}
        .play-btn {{
            width: 80px;
            height: 80px;
            background: rgba(255,255,255,0.2);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 40px;
            cursor: pointer;
            backdrop-filter: blur(5px);
        }}

        /* Footer */
        footer {{
            text-align: center;
            padding: 40px 0;
            color: #999;
            background: #fff;
        }}
    </style>
</head>
<body>

    <header>
        <div class="container">
            <a href="../index.html" class="logo">XIBO 喜播教育</a>
        </div>
    </header>

    <div class="container">
        <div class="breadcrumb">
            <a href="../index.html">首页</a>
            <span>&gt;</span>
            <a href="../SKU_Revenue_Analysis_2026.html">SKU 营收拆解</a>
            <span>&gt;</span>
            <span style="color: #333;">{sku_name}</span>
        </div>
    </div>

    <div class="hero">
        <div class="container">
            <div style="text-transform: uppercase; letter-spacing: 2px; font-size: 0.9rem; margin-bottom: 20px; opacity: 0.8;">职业技能认证课程</div>
            <h1>{sku_name}</h1>
            <p>基于真实行业需求的实战课程，融合AI技术与名师指导，助力学员实现“技能变现”与“职业进阶”。</p>
            <a href="#" class="btn">立即加入训练营</a>
        </div>
    </div>

    <section>
        <div class="container">
            <div class="grid-2">
                <div>
                    <h2>产品说明书</h2>
                    <p style="font-size: 1.1rem; color: #666; margin-bottom: 30px;">
                        本课程专为{target_audience}设计，通过{duration}周的系统化训练，
                        帮助学员掌握{sku_name}的核心技能。课程采用“学-练-测-评”闭环模式，
                        确保每一位学员都能达到行业交付标准。
                    </p>
                    <div style="background: #fff8f0; padding: 20px; border-left: 4px solid var(--primary); margin-bottom: 25px;">
                        <h4 style="margin: 0 0 10px 0; color: var(--primary);">✨ 课程亮点 (Highlights)</h4>
                        <ul class="feature-list" style="margin: 0;">
                            {highlights_html}
                        </ul>
                    </div>
                </div>
                
                <div class="teacher-profile">
                    <div class="teacher-img">{teacher_last_name}</div>
                    <h3 style="margin: 0 0 5px 0;">{teacher_name}</h3>
                    <div style="color: var(--primary); font-weight: bold; margin-bottom: 15px;">{teacher_title}</div>
                    <p style="font-size: 0.9rem; color: #666; font-style: italic;">
                        "{teacher_quote}"
                    </p>
                    <hr style="border: 0; border-top: 1px solid #eee; margin: 20px 0;">
                    <div style="font-size: 0.85rem; color: #999;">
                        行业经验：15年+ | 累计学员：50,000+
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section style="background: #f9f9f9;">
        <div class="container">
            <h2>职业学校课程设计 (Curriculum)</h2>
            <div style="text-align: center; max-width: 800px; margin: 0 auto;">
                <p>对标行业标准，实战驱动教学。</p>
            </div>
            
            <table class="curriculum-table">
                <thead>
                    <tr>
                        <th style="width: 15%;">周次</th>
                        <th style="width: 25%;">模块主题</th>
                        <th>核心内容 & 实战任务</th>
                    </tr>
                </thead>
                <tbody>
                    {curriculum_rows}
                </tbody>
            </table>
        </div>
    </section>

    <section>
        <div class="container">
            <h2>教学现场模拟</h2>
            <div class="video-placeholder">
                <div class="play-btn">▶</div>
                <div style="margin-top: 20px;">点击预览 {sku_name} 核心课程片段</div>
                <div style="position: absolute; bottom: 20px; right: 20px; font-size: 0.8rem; opacity: 0.7;">
                    Simulation Mode: Preview
                </div>
            </div>
        </div>
    </section>

    <section style="background: #fff;">
        <div class="container">
            <h2>质量与效果看板 (Quality Dashboard)</h2>
            <p style="text-align: center; color: #666; margin-bottom: 40px;">
                实时监控教学质量，确保每一分投入都有回报。
            </p>
            
            <div class="dashboard">
                <div class="stats-grid">
                    <div class="stat-box">
                        <div class="stat-value" style="color: var(--success);">{pass_rate}%</div>
                        <div class="stat-label">课程通关率</div>
                    </div>
                    <div class="stat-box">
                        <div class="stat-value" style="color: var(--primary);">{employment_rate}%</div>
                        <div class="stat-label">副业/就业接单率</div>
                    </div>
                    <div class="stat-box">
                        <div class="stat-value">{sat_score}</div>
                        <div class="stat-label">学员满意度 (NPS)</div>
                    </div>
                    <div class="stat-box">
                        <div class="stat-value" style="color: var(--warning);">+{income_boost}</div>
                        <div class="stat-label">平均月增收 (元)</div>
                    </div>
                </div>

                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px;">
                    <!-- Simple Bar Chart Simulation -->
                    <div style="background: white; padding: 20px; border-radius: 8px;">
                        <h4 style="margin-top: 0;">技能掌握度分布</h4>
                        <div style="margin-top: 20px;">
                            <div style="display: flex; align-items: center; margin-bottom: 10px;">
                                <span style="width: 60px; font-size: 0.8rem;">优秀</span>
                                <div style="flex: 1; height: 10px; background: #eee; border-radius: 5px; margin: 0 10px;">
                                    <div style="width: 35%; height: 100%; background: var(--success); border-radius: 5px;"></div>
                                </div>
                                <span style="font-size: 0.8rem;">35%</span>
                            </div>
                            <div style="display: flex; align-items: center; margin-bottom: 10px;">
                                <span style="width: 60px; font-size: 0.8rem;">良好</span>
                                <div style="flex: 1; height: 10px; background: #eee; border-radius: 5px; margin: 0 10px;">
                                    <div style="width: 45%; height: 100%; background: var(--primary); border-radius: 5px;"></div>
                                </div>
                                <span style="font-size: 0.8rem;">45%</span>
                            </div>
                            <div style="display: flex; align-items: center; margin-bottom: 10px;">
                                <span style="width: 60px; font-size: 0.8rem;">合格</span>
                                <div style="flex: 1; height: 10px; background: #eee; border-radius: 5px; margin: 0 10px;">
                                    <div style="width: 20%; height: 100%; background: var(--warning); border-radius: 5px;"></div>
                                </div>
                                <span style="font-size: 0.8rem;">20%</span>
                            </div>
                        </div>
                    </div>

                    <!-- Testimonial -->
                    <div style="background: white; padding: 20px; border-radius: 8px; display: flex; flex-direction: column; justify-content: center;">
                        <div style="font-style: italic; color: #666;">
                            "这门课程完全改变了我的职业轨迹。特别是实战环节，让我第一次接到了{income_boost}元的商单！"
                        </div>
                        <div style="margin-top: 15px; font-weight: bold; text-align: right;">
                            —— 优秀学员 {student_name}
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <footer>
        <div class="container">
            <p>&copy; 2026 喜播教育集团 Xibo Education Group. All Rights Reserved.</p>
        </div>
    </footer>

</body>
</html>
"""

TEACHERS = [
    {"name": "王明军", "title": "中国演播艺术大师", "quote": "声音是有温度的，我教你如何用声音传递情感。"},
    {"name": "艾宝良", "title": "顶级有声演播家", "quote": "演播不是念字，而是创造画面。"},
    {"name": "李野墨", "title": "资深演播艺术家", "quote": "基本功是艺术的灵魂。"},
    {"name": "张震", "title": "商业配音专家", "quote": "不仅要好听，更要值钱。"},
    {"name": "苏秦", "title": "金牌课程制作人", "quote": "做最懂学员的实战课程。"}
]

HIGHLIGHTS_POOL = [
    "独家签约名师亲自授课，保障教学质量",
    "提供真实商业项目练手，优秀学员直接签约",
    "1v1 助教全天候答疑，拒绝孤单学习",
    "AI 辅助作业批改，实时反馈学习问题",
    "结业即推荐就业，对接海量副业资源",
    "终身免费复训权限，持续跟进行业新技术",
    "配套千元级专业硬件设备，一步到位",
]

CURRICULUM_MODULES = [
    {"week": "Week 1", "title": "行业认知与基础入门", "content": "了解行业发展趋势，掌握软件基础操作，完成第一次声音/作品录制。"},
    {"week": "Week 2", "title": "核心技能专项训练", "content": "针对性突破核心难点（如气息、剪辑逻辑、AI提示词），建立专业护城河。"},
    {"week": "Week 3", "title": "商业案例拆解与模仿", "content": "精选10+真实商业爆款案例，逐帧/逐句拆解，还原大神创作思路。"},
    {"week": "Week 4", "title": "实战项目演练 (PBL)", "content": "领取真实模拟订单，在助教指导下完成全流程交付，模拟真实职场环境。"},
    {"week": "Week 5", "title": "进阶技巧与风格化", "content": "探索个人风格，差异化竞争。掌握高级技巧，提升作品质感。"},
    {"week": "Week 6", "title": "运营变现与渠道对接", "content": "账号运营SOP，接单平台入驻指南，报价与谈判技巧。"},
    {"week": "Week 7", "title": "毕业作品打磨", "content": "导师1v1指导毕业设计，打造可以写进简历的完美作品集。"},
    {"week": "Week 8", "title": "职业规划与签约", "content": "模拟面试，简历优化，优秀学员签约考核。"},
]

def clean_filename(name):
    """Sanitize sku name for filename."""
    name = name.replace('L1+L2', 'L1_Plus_L2')
    name = re.sub(r'[^\w\u4e00-\u9fff\-_]', '', name)
    return name

def generate_sku_pages():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        
    skus = set()
    
    with open(SOURCE_CSV, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader) # Skip header
        for row in reader:
            if not row or len(row) < 2: 
                continue
            
            sku_name = row[1].strip()
            
            if not sku_name or sku_name == "SKU" or sku_name == "Total" or sku_name == "合计":
                continue
                
            skus.add(sku_name)

    print(f"Found {len(skus)} unique SKUs.")

    for sku_name in skus:
        filename = clean_filename(sku_name) + ".html"
        filepath = os.path.join(OUTPUT_DIR, filename)
        
        # Simulation Data
        pass_rate = random.randint(85, 99)
        employment_rate = random.randint(55, 95)
        sat_score = random.randint(80, 98)
        income_boost = random.choice([500, 1000, 1500, 2000, 3000, 5000])
        student_name = random.choice(["张*", "王*", "李*", "赵*", "刘*"])
        
        target_audience = "零基础学员"
        if "L2" in sku_name or "进阶" in sku_name:
            target_audience = "有一定基础的进阶学员"
        elif "L3" in sku_name or "大师" in sku_name:
            target_audience = "追求极致的专业从业者"
            
        duration = random.choice([4, 8, 12, 16])

        # Teacher Info
        teacher = random.choice(TEACHERS)
        
        # Highlights
        highlights = random.sample(HIGHLIGHTS_POOL, 4)
        highlights_html = "".join([f"<li>{h}</li>" for h in highlights])

        # Curriculum Rows
        curriculum_html = ""
        for mod in CURRICULUM_MODULES:
            curriculum_html += f"""
            <tr>
                <td><span class="module-tag">{mod['week']}</span></td>
                <td><strong>{mod['title']}</strong></td>
                <td style="color: #666;">{mod['content']}</td>
            </tr>
            """

        html_content = HTML_TEMPLATE.format(
            sku_name=sku_name,
            pass_rate=pass_rate,
            employment_rate=employment_rate,
            sat_score=sat_score,
            income_boost=income_boost,
            student_name=student_name,
            target_audience=target_audience,
            duration=duration,
            teacher_name=teacher['name'],
            teacher_title=teacher['title'],
            teacher_quote=teacher['quote'],
            teacher_last_name=teacher['name'][0],
            highlights_html=highlights_html,
            curriculum_rows=curriculum_html
        )
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html_content)
            
        print(f"Generated: {filepath}")

    print("Generation complete.")

if __name__ == "__main__":
    generate_sku_pages()
