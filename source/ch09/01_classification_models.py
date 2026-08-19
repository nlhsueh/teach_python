# 01_classification_models.py - 經典監督式分類器對比 (KNN, 決策樹, 隨機森林)

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# 1. 載入鳶尾花資料集 (Iris Dataset)
iris = load_iris()
X = iris.data
y = iris.target

# 2. 切分資料集為 70% 訓練集與 30% 測試集
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# 3. 建立並訓練三個經典分類器
# (1) K-近鄰演算法 (KNN)
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
knn_pred = knn.predict(X_test)
knn_acc = accuracy_score(y_test, knn_pred)

# (2) 決策樹分類器 (Decision Tree)
dt = DecisionTreeClassifier(max_depth=4, random_state=42)
dt.fit(X_train, y_train)
dt_pred = dt.predict(X_test)
dt_acc = accuracy_score(y_test, dt_pred)

# (3) 隨機森林集成分類器 (Random Forest)
rf = RandomForestClassifier(n_estimators=100, max_depth=4, random_state=42)
rf.fit(X_train, y_train)
rf_pred = rf.predict(X_test)
rf_acc = accuracy_score(y_test, rf_pred)

# 4. 輸出評估結果比較
print("=== 鳶尾花資料集分類評估結果 ===")
print(f"1. K-近鄰演算法 (KNN) 準確度: {knn_acc * 100:.2f}%")
print(f"2. 決策樹 (Decision Tree) 準確度: {dt_acc * 100:.2f}%")
print(f"3. 隨機森林 (Random Forest) 準確度: {rf_acc * 100:.2f}%")

print("\n隨機森林詳細分類報告：")
print(classification_report(y_test, rf_pred, target_names=iris.target_names))
