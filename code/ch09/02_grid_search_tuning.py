# 02_grid_search_tuning.py - 交叉驗證與超參數網格搜尋 (GridSearchCV)

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# 1. 載入鳶尾花資料集並切分
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.3, random_state=42
)

# 2. KNN 超參數網格搜尋
# 測試不同 K 值、權重與距離度量
knn_param_grid = {
    'n_neighbors': [1, 3, 5, 7, 9, 11],
    'weights': ['uniform', 'distance'],
    'metric': ['euclidean', 'manhattan']
}

# 使用 5 折交叉驗證 (cv=5) 進行網格搜尋
knn_grid = GridSearchCV(KNeighborsClassifier(), knn_param_grid, cv=5, scoring='accuracy')
knn_grid.fit(X_train, y_train)

print("=== [1. KNN 參數調優結果] ===")
print(f"最佳參數組合：{knn_grid.best_params_}")
print(f"交叉驗證最佳分數 (CV Score)：{knn_grid.best_score_:.4f}")

best_knn = knn_grid.best_estimator_
knn_pred = best_knn.predict(X_test)
print(f"測試集最終準確度：{accuracy_score(y_test, knn_pred):.4f}\n")

# 3. 決策樹超參數網格搜尋
tree_param_grid = {
    'criterion': ['gini', 'entropy'],
    'max_depth': [3, 4, 5, 6, None],
    'min_samples_split': [2, 5, 10]
}

tree_grid = GridSearchCV(DecisionTreeClassifier(random_state=42), tree_param_grid, cv=5, scoring='accuracy')
tree_grid.fit(X_train, y_train)

print("=== [2. 決策樹參數調優結果] ===")
print(f"最佳參數組合：{tree_grid.best_params_}")
print(f"交叉驗證最佳分數 (CV Score)：{tree_grid.best_score_:.4f}")

best_tree = tree_grid.best_estimator_
tree_pred = best_tree.predict(X_test)
print(f"測試集最終準確度：{accuracy_score(y_test, tree_pred):.4f}")
