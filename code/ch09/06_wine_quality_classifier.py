# 06_wine_quality_classifier.py - 綜合實作專案：紅酒品質多重分類器設計

import pandas as pd
import numpy as np
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, accuracy_score

# 1. 載入紅酒資料集 (包含 13 種化學成分特徵，預測 3 種不同產地酒廠)
wine = load_wine()
X = wine.data
y = wine.target

print(f"資料集維度: {X.shape[0]} 筆樣本，{X.shape[1]} 個特徵")
print(f"分類標籤類別: {wine.target_names}")

# 2. 切分訓練集與測試集 (75% : 25%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# 3. 特徵標準化
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test) # 測試集必須使用訓練集統計量轉換

# 4. 建立決策樹分類器並配置參數網格
dt_classifier = DecisionTreeClassifier(random_state=42)

param_grid = {
    'criterion': ['gini', 'entropy'],
    'max_depth': [3, 4, 5, 7, 10],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

# 5. 進行 5 折交叉驗證網格搜尋
print("\n正在進行 5-Fold GridSearchCV 參數調優...")
grid_search = GridSearchCV(dt_classifier, param_grid, cv=5, scoring='accuracy')
grid_search.fit(X_train_scaled, y_train)

print(f"最佳參數組合: {grid_search.best_params_}")
print(f"交叉驗證最高 Accuracy: {grid_search.best_score_ * 100:.2f}%")

# 6. 使用最佳參數模型進行測試集評估
best_model = grid_search.best_estimator_
y_pred = best_model.predict(X_test_scaled)

test_acc = accuracy_score(y_test, y_pred)
print(f"\n測試集最終 Accuracy: {test_acc * 100:.2f}%")

# 7. 輸出詳細分類評估報告 (Precision, Recall, F1-Score)
print("\n=== 詳細分類評估報告 ===")
print(classification_report(y_test, y_pred, target_names=wine.target_names))
