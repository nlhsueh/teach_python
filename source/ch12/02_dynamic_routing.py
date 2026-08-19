# 02_dynamic_routing.py - Flask 動態路由與 URL 參數擷取

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h2>Flask 動態路由示範首頁</h2>
    <ul>
        <li><a href="/user/alex">訪問 Alex 的個人專區 (/user/alex)</a></li>
        <li><a href="/user/mary">訪問 Mary 的個人專區 (/user/mary)</a></li>
        <li><a href="/post/101">閱讀第 101 篇文章 (/post/101)</a></li>
        <li><a href="/post/205">閱讀第 205 篇文章 (/post/205)</a></li>
    </ul>
    """

# 1. 動態字串路由：<username> 會被自動作為參數傳入函式中
@app.route('/user/<username>')
def show_user_profile(username):
    return f"""
    <h2>會員個人檔案專區</h2>
    <p>歡迎回來，<strong style="color: #0284c7; font-size: 1.2em;">{username}</strong>！</p>
    <p>這是為您動態生成的專屬個人頁面。</p>
    <p><a href="/">返回首頁</a></p>
    """

# 2. 限定參數型態為整數：<int:post_id>
# 若使用者輸入非數字（如 /post/abc），Flask 會自動返回 404 Not Found
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f"""
    <h2>文章展示系統</h2>
    <p>您目前正在閱讀 <strong>第 {post_id} 篇</strong> 文章的內容。</p>
    <p>（資料庫查詢文章 ID = {post_id} 的段落與留言...）</p>
    <p><a href="/">返回首頁</a></p>
    """

if __name__ == '__main__':
    print("啟動動態路由伺服器，請在瀏覽器開啟: http://127.0.0.1:5000/")
    app.run(debug=True)
