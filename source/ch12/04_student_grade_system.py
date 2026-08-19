# 04_student_grade_system.py - 綜合實作專案：成績查詢與登記系統

from flask import Flask, request, render_template_string, redirect, url_for

app = Flask(__name__)

# 模擬資料庫：儲存學生學籍與成績資料 (記憶體中)
student_db = [
    {"id": "101", "name": "張小明", "python_score": 92, "class": "電機一"},
    {"id": "102", "name": "李美華", "python_score": 85, "class": "資工二"},
    {"id": "103", "name": "王大同", "python_score": 78, "class": "自控三"}
]

# 定義首頁模板 (包含學生成績表格與新增學生表單)
INDEX_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>資電學院成績登記系統</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; margin: 40px; background-color: #f4f6f9; }
        .container { max-width: 800px; margin: 0 auto; }
        .card { background: white; padding: 24px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.08); margin-bottom: 24px; }
        table { border-collapse: collapse; width: 100%; margin-top: 12px; }
        th, td { padding: 12px; text-align: left; border-bottom: 1px solid #e2e8f0; }
        th { background-color: #0056b3; color: white; border-radius: 4px 4px 0 0; }
        tr:nth-child(even) { background-color: #f8fafc; }
        .grade-a { color: #16a34a; font-weight: bold; }
        .grade-b { color: #d97706; font-weight: bold; }
        .grade-c { color: #dc2626; font-weight: bold; }
        .form-row { display: flex; gap: 12px; margin-bottom: 12px; }
        .form-group { flex: 1; }
        label { font-size: 13px; font-weight: bold; color: #475569; display: block; margin-bottom: 4px; }
        input[type=text], input[type=number] { width: 100%; padding: 8px; border: 1px solid #cbd5e1; border-radius: 4px; box-sizing: border-box; }
        input[type=submit] { background-color: #28a745; color: white; border: none; padding: 10px 20px; cursor: pointer; border-radius: 4px; font-weight: bold; }
        input[type=submit]:hover { background-color: #218838; }
        .search-btn { background-color: #007bff !important; }
        .search-btn:hover { background-color: #0069d9 !important; }
    </style>
</head>
<body>
    <div class="container">
        <h2>Python 程式設計 - 成績登記查詢系統</h2>
        
        <!-- 1. 搜尋區塊 (GET /search) -->
        <div class="card">
            <h3 style="margin-top: 0;">🔍 快速查詢學生</h3>
            <form action="/search" method="GET" style="display: flex; gap: 8px;">
                <input type="text" name="query_name" placeholder="輸入學生姓名 (如：張小明)..." required style="flex: 1;">
                <input type="submit" value="查詢" class="search-btn">
            </form>
        </div>

        <!-- 2. 學生列表展示 (Jinja2 for 迴圈與 if 判斷) -->
        <div class="card">
            <h3 style="margin-top: 0;">📋 目前已登記學生列表</h3>
            <table>
                <tr>
                    <th>學號</th>
                    <th>班級</th>
                    <th>姓名</th>
                    <th>Python 成績</th>
                    <th>評等</th>
                </tr>
                {% for std in students %}
                <tr>
                    <td>{{ std.id }}</td>
                    <td>{{ std.class }}</td>
                    <td><strong>{{ std.name }}</strong></td>
                    <td>{{ std.python_score }} 分</td>
                    <td>
                        {% if std.python_score >= 90 %}
                            <span class="grade-a">A+</span>
                        {% elif std.python_score >= 80 %}
                            <span class="grade-a">A</span>
                        {% elif std.python_score >= 70 %}
                            <span class="grade-b">B</span>
                        {% else %}
                            <span class="grade-c">C</span>
                        {% endif %}
                    </td>
                </tr>
                {% endfor %}
            </table>
        </div>

        <!-- 3. 新增學生資料表單 (POST /add) -->
        <div class="card">
            <h3 style="margin-top: 0;">➕ 登記新學生成績</h3>
            <form action="/add" method="POST">
                <div class="form-row">
                    <div class="form-group">
                        <label>學號：</label>
                        <input type="text" name="std_id" placeholder="如 104" required>
                    </div>
                    <div class="form-group">
                        <label>班級：</label>
                        <input type="text" name="std_class" placeholder="如 電機一" required>
                    </div>
                    <div class="form-group">
                        <label>姓名：</label>
                        <input type="text" name="std_name" placeholder="如 林志玲" required>
                    </div>
                    <div class="form-group">
                        <label>Python 成績：</label>
                        <input type="number" name="std_score" min="0" max="100" placeholder="0~100" required>
                    </div>
                </div>
                <input type="submit" value="＋ 新增登記">
            </form>
        </div>
    </div>
</body>
</html>
"""

# 1. 系統首頁路由
@app.route('/')
def home():
    # 將學生的 dictionary list 傳給 Jinja2 渲染
    return render_template_string(INDEX_TEMPLATE, students=student_db)

# 2. 新增學生路由 (只接收 POST)
@app.route('/add', methods=['POST'])
def add_student():
    # 讀取表單資料
    sid = request.form.get('std_id')
    sclass = request.form.get('std_class')
    sname = request.form.get('std_name')
    sscore = int(request.form.get('std_score'))

    # 建立新字典並附加到資料庫中
    new_student = {
        "id": sid,
        "class": sclass,
        "name": sname,
        "python_score": sscore
    }
    student_db.append(new_student)
    
    # 登記成功後，重新導向 (Redirect) 回首頁以更新表格列表
    return redirect('/')

# 3. 搜尋學生路由 (接收 GET 查詢參數)
@app.route('/search', methods=['GET'])
def search_student():
    query = request.args.get('query_name', '').strip()
    
    # 過濾出包含關鍵字姓名的學生
    results = [std for std in student_db if query in std['name']]
    
    result_template = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>查詢結果</title>
        <style>
            body { font-family: sans-serif; margin: 40px; background-color: #f4f6f9; }
            .card { background: white; padding: 24px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.08); max-width: 600px; }
            ul { line-height: 2; }
            a { color: #0056b3; text-decoration: none; font-weight: bold; }
        </style>
    </head>
    <body>
        <div class="card">
            <h2>查詢結果 (關鍵字：{{ query }})</h2>
            {% if matched_list %}
                <ul>
                {% for std in matched_list %}
                    <li>[{{ std.class }}] 學號：{{ std.id }} - <strong>{{ std.name }}</strong>：Python 成績 = {{ std.python_score }} 分</li>
                {% endfor %}
                </ul>
            {% else %}
                <p style="color: #dc2626; font-weight: bold;">⚠️ 找不到符合關鍵字「{{ query }}」的學生資料。</p>
            {% endif %}
            <p><a href="/">➔ 返回首頁列表</a></p>
        </div>
    </body>
    </html>
    """
    return render_template_string(result_template, matched_list=results, query=query)

if __name__ == '__main__':
    print("啟動學生管理系統伺服器，請在瀏覽器開啟: http://127.0.0.1:5000/")
    app.run(debug=True)
