from weasyprint import HTML
from pathlib import Path

# مسار حفظ PDF
desktop = Path.home() / 'Desktop'
output_pdf = desktop / 'Smart_Test.pdf'

html_content = """
<html>
<head>
    <meta charset="UTF-8">
    <style>
        body { 
            direction: rtl; 
            text-align: right; 
            font-family: sans-serif; 
            padding: 20px;
        }
        .question { 
            background: #f4f4f4; 
            padding: 10px; 
            border-right: 5px solid #2ecc71; 
            margin-bottom: 10px;
        }
    </style>
</head>
<body>
    <h1>اختبار الرياضيات الذكي</h1>
    <div class="question">
        <b>س 1:</b> ما هو ناتج تكامل الدالة القوية؟
    </div>
    <p>أ) x^2 + c</p>
    <p>ب) 2x</p>
</body>
</html>
"""

# التحويل في سطر واحد فقط!
HTML(string=html_content).write_pdf(output_pdf)

print(f"تم إنشاء الملف بنجاح في: {output_pdf}")