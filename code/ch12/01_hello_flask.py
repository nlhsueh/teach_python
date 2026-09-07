# 01_hello_flask.py - 最簡 Flask 網頁伺服器與路由基礎

from flask import Flask

# 1. 建立 Flask 應用程式實例
# __name__ 代表目前執行的 Python 模組名稱，Flask 會以此決定資源根目錄
app = Flask(__name__)

# 2. 定義首頁路由 (Route)
# 當使用者在瀏覽器造訪首頁 '/' 時，執行 index() 函式並將 HTML 回傳顯示
@app.route('/')
def index():
    return """
    <h1>歡迎來到 Python Flask 網頁伺服器！</h1>
    <p>這是你的第一個動態網頁，代表後端 Python 伺服器正在本機 5000 埠正常運作中。</p>
    <hr>
    <p><a href="/about">前往「關於我們」頁面</a></p>
    """

# 3. 定義第二個路由路徑 '/about'
@app.route('/about')
def about():
    return """
    <h2>關於我們</h2>
    <p>本系統使用 Python 3.12 與 Flask 微型 Web 框架建構。</p>
    <p><a href="/">返回首頁</a></p>
    """

# 4. 啟動伺服器
if __name__ == '__main__':
    # debug=True 會啟動「自動重載機制 (Hot Reload)」與詳細除錯頁面
    # 預設會在 http://127.0.0.1:5000/ 運行
    print("啟動 Flask 伺服器，請在瀏覽器開啟: http://127.0.0.1:5000/")
    app.run(debug=True)
