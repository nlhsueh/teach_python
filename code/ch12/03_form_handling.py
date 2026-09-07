# 03_form_handling.py - Jinja2 模板渲染與 GET/POST 表單處理

from flask import Flask, request, render_template_string

app = Flask(__name__)

# 定義 HTML 模板字串 (含有 Jinja2 語法與 CSS 美化)
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Flask 表單處理示範</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; margin: 40px; background-color: #f8fafc; }
        .card { background: white; padding: 24px; border-radius: 8px; box-shadow: 0 2px 6px rgba(0,0,0,0.08); width: 420px; }
        input[type=text], textarea { width: 100%; padding: 8px; margin-top: 6px; margin-bottom: 16px; border: 1px solid #cbd5e1; border-radius: 4px; box-sizing: border-box; }
        input[type=submit] { background-color: #0284c7; color: white; border: none; padding: 10px 18px; cursor: pointer; border-radius: 4px; font-weight: bold; }
        input[type=submit]:hover { background-color: #0369a1; }
    </style>
</head>
<body>
    <div class="card">
        <h2>聯絡助教表單</h2>
        <!-- 表單使用 POST 方法提交至 /submit 路由 -->
        <form action="/submit" method="POST">
            <label for="student_name"><strong>學生姓名：</strong></label>
            <input type="text" id="student_name" name="username" placeholder="請輸入姓名..." required>
            
            <label for="msg"><strong>問題內容：</strong></label>
            <textarea id="msg" name="message" rows="4" placeholder="請輸入您想詢問的程式問題..." required></textarea>
            
            <input type="submit" value="送出問題 ➔">
        </form>
    </div>
</body>
</html>
"""

# 1. 首頁表單展示路由 (GET)
@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

# 2. 表單接收與處理路由 (POST)
@app.route('/submit', methods=['POST'])
def handle_submit():
    # 使用 request.form.get 讀取 POST 請求中的表單欄位
    name = request.form.get('username')
    message = request.form.get('message')
    
    # 渲染結果網頁
    result_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>提交成功</title>
        <style>
            body {{ font-family: sans-serif; margin: 40px; background-color: #f8fafc; }}
            .card {{ background: white; padding: 24px; border-radius: 8px; box-shadow: 0 2px 6px rgba(0,0,0,0.08); width: 420px; }}
            .quote {{ background: #f1f5f9; padding: 12px; border-left: 4px solid #0284c7; margin: 16px 0; border-radius: 4px; }}
        </style>
    </head>
    <body>
        <div class="card">
            <h2 style="color: #16a34a;">✅ 提交成功！</h2>
            <p>感謝學生 <strong>{name}</strong> 的留言。</p>
            <div class="quote">
                <strong>留言內容：</strong><br>
                {message}
            </div>
            <p><a href="/" style="color: #0284c7; text-decoration: none;">➔ 返回表單頁面</a></p>
        </div>
    </body>
    </html>
    """
    return render_template_string(result_html)

if __name__ == '__main__':
    print("啟動表單伺服器，請在瀏覽器開啟: http://127.0.0.1:5000/")
    app.run(debug=True)
