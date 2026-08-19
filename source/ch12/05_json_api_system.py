# 05_json_api_system.py - 進階挑戰專題：RESTful JSON API 與防呆錯誤處理

from flask import Flask, request, jsonify, abort

app = Flask(__name__)

# 模擬資料庫
student_db = [
    {"id": "101", "name": "張小明", "python_score": 92, "class": "電機一"},
    {"id": "102", "name": "李美華", "python_score": 85, "class": "資工二"},
    {"id": "103", "name": "王大同", "python_score": 78, "class": "自控三"}
]

# 1. API 根目錄說明
@app.route('/')
def api_index():
    return """
    <h2>RESTful JSON API 示範伺服器</h2>
    <p>可測試以下端點：</p>
    <ul>
        <li><a href="/api/students">GET /api/students</a> - 取得所有學生 JSON 清單</li>
        <li><a href="/api/students/101">GET /api/students/101</a> - 取得特定學號學生資料</li>
        <li><a href="/api/students/999">GET /api/students/999</a> - 測試 404 錯誤回應</li>
    </ul>
    """

# 2. RESTful API：取得所有學生的 JSON 清單 (GET /api/students)
@app.route('/api/students', methods=['GET'])
def get_all_students():
    # jsonify 會自動將 Python list/dict 轉換為 JSON 規格，並設定 Content-Type: application/json
    return jsonify({
        "status": "success",
        "total_count": len(student_db),
        "data": student_db
    }), 200

# 3. RESTful API：取得單一學生資料 (GET /api/students/<std_id>)
@app.route('/api/students/<std_id>', methods=['GET'])
def get_student_by_id(std_id):
    student = next((s for s in student_db if s["id"] == std_id), None)
    if not student:
        return jsonify({
            "status": "error",
            "message": f"找不到學號為 {std_id} 的學生"
        }), 404
    return jsonify({
        "status": "success",
        "data": student
    }), 200

# 4. RESTful API：新增學生並包含嚴格防呆驗證 (POST /api/students)
@app.route('/api/students', methods=['POST'])
def create_student_api():
    # 支援 JSON 負載 (request.get_json()) 或一般 Form 表單
    data = request.get_json() or request.form
    
    sid = data.get("id")
    sname = data.get("name")
    sclass = data.get("class")
    score = data.get("python_score")

    # 防呆 1：欄位缺漏檢查 (HTTP 400 Bad Request)
    if not sid or not sname or not sclass or score is None:
        return jsonify({
            "status": "error",
            "message": "資料缺漏：id, name, class, python_score 皆為必填欄位"
        }), 400

    # 防呆 2：學號重複檢查 (HTTP 400 Bad Request)
    if any(s["id"] == sid for s in student_db):
        return jsonify({
            "status": "error",
            "message": f"學號 {sid} 已存在，請勿重複登記"
        }), 400

    # 防呆 3：成績範圍驗證 (0 ~ 100)
    try:
        score_int = int(score)
        if not (0 <= score_int <= 100):
            raise ValueError
    except (ValueError, TypeError):
        return jsonify({
            "status": "error",
            "message": "成績格式錯誤：python_score 必須為 0 至 100 之間的整數"
        }), 400

    new_std = {
        "id": str(sid),
        "name": str(sname),
        "class": str(sclass),
        "python_score": score_int
    }
    student_db.append(new_std)

    return jsonify({
        "status": "success",
        "message": "學生資料登記成功",
        "data": new_std
    }), 201

if __name__ == '__main__':
    print("啟動 RESTful API 伺服器，請在瀏覽器開啟: http://127.0.0.1:5000/api/students")
    app.run(debug=True)
