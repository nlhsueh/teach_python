# 06_rag_similarity_search.py - 檢索增強生成 (RAG) 與文字相似度知識庫檢索

# 1. 模擬本地企業/校園內部知識庫 (私人文件)
knowledge_base = [
    "電機系辦公室位於資電大樓四樓，開放時間為週一至週五 9:00-17:00。",
    "資工系專題發表會定於 12 月 15 日在體育館二樓舉行。",
    "智慧系統控制實驗室由王教授指導，位於資電大樓 602 室。",
    "Python 程式設計期末考將於第 16 週進行，考試形式為上機考。"
]

def search_related_context(query, database):
    """ 純 Python 關鍵字相似度檢索演算法 (計算字符交集比例) """
    query_words = set(query.lower())
    best_match = None
    max_score = -1
    
    for idx, doc in enumerate(database):
        doc_words = set(doc.lower())
        overlap = len(query_words.intersection(doc_words))
        score = overlap / len(query_words) if len(query_words) > 0 else 0
        
        if score > max_score:
            max_score = score
            best_match = doc
            
    return best_match, max_score

if __name__ == '__main__':
    # 2. 模擬使用者提問
    user_query = "請問電機系辦公室在哪裡？幾點有開？"
    print(f"使用者問題: {user_query}")
    
    # 3. [步驟 1] 檢索相關知識
    retrieved_context, score = search_related_context(user_query, knowledge_base)
    
    print("\n=== [步驟 1: 知識檢索結果] ===")
    print(f"匹配分數: {score:.2f}")
    print(f"檢索到的背景知識: {retrieved_context}")
    
    # 4. [步驟 2] 動態合成含有背景資料的 Prompt
    rag_prompt = f"""
你是一個輔助學生解惑的校園 AI 助理。請嚴格根據以下提供的【背景知識】來回答使用者的【問題】。
如果背景知識中沒有相關資訊，請誠實回答「抱歉，資料庫中查無相關資訊」。

【背景知識】：
{retrieved_context}

【問題】：
{user_query}
"""
    
    print("\n=== [步驟 2: 合成發送給 LLM 的完整 RAG Prompt] ===")
    print(rag_prompt.strip())
    print("\n=== [步驟 3: 說明] ===")
    print("在實際 RAG 系統中，此 prompt 會傳遞給 model.generate_content(rag_prompt)，")
    print("模型即可基於這段真實背景知識，產出精準無幻覺的回答。")
