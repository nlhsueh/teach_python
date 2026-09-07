# 10_ibike_analysis.py - 模擬台中市政府 iBike 開放資料讀入與基本解析
import json

# 模擬 iBike API 回傳的簡化 JSON 資料結構
mock_ibike_json = """
{
    "retVal": {
        "2001": {
            "sno": "2001",
            "sna": "逢甲大學",
            "tot": "40",
            "sbi": "24",
            "sarea": "西屯區"
        },
        "2002": {
            "sno": "2002",
            "sna": "秋紅谷",
            "tot": "30",
            "sbi": "10",
            "sarea": "西屯區"
        },
        "2003": {
            "sno": "2003",
            "sna": "台中火車站",
            "tot": "60",
            "sbi": "5",
            "sarea": "中區"
        }
    }
}
"""

# 1. 讀取 JSON 資料
data = json.loads(mock_ibike_json)
stations = data["retVal"]

# 2. 進行簡單統計分析 (例如：各站點車輛資訊與統計)
print("--- 逢甲大學與秋紅谷等站點借車狀況 ---")
for sno, info in stations.items():
    name = info["sna"]
    total_slots = int(info["tot"])
    available_bikes = int(info["sbi"])
    area = info["sarea"]
    ratio = (available_bikes / total_slots) * 100
    print(f"區域: {area} | 站點: {name} | 總格數: {total_slots} | 可借車輛: {available_bikes} | 車輛充足率: {ratio:.1f}%")
