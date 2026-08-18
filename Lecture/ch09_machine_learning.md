Ch09 Introduction to Machine Learning
===

# Python 機器學習入門

本章將引導你進入人工智慧中最核心的領域——**機器學習 (Machine Learning, ML)**。我們將學習機器學習的根本哲學、重要學術觀念，並使用 Python 的主流套件 `Scikit-Learn`（簡稱 `sklearn`）實作多種經典的監督式與非監督式學習任務。

本章包含以下核心單元：
* **9.1 機器學習基礎觀念**：學習 AI、ML 與深度學習 (DL) 的關係、監督與非監督式學習的本質差異，以及偏差與變異的平衡 (Bias-Variance Tradeoff)。
* **9.2 監督式學習：分類任務與超參數調校**：實作 KNN、決策樹與隨機森林 (Random Forest) 分類器，並使用網格搜尋法 (Grid Search) 進行模型調參。
* **9.3 監督式學習：迴歸任務與評估指標**：探討多元線性迴歸模型、L1/L2 正規化（Lasso/Ridge），與 $R^2$、MAE、MSE 等指標的數學意義。
* **9.4 非監督式學習：K-Means 分群與肘部法**：使用 K-Means 進行無標籤聚類，探討肘部法 (Elbow Method) 尋找最佳分群數，並簡介 DBScan 密度分群。
* **9.5 關鍵觀念與特徵工程**：探討過擬合/欠擬合、交叉驗證、特徵標準化與獨熱編碼 (One-Hot Encoding)。
* **9.6 綜合實作專題：紅酒品質預測分類器**。

---

## 9.1 機器學習基礎觀念

### 9.1.1 人工智慧、機器學習與深度學習的關係

很多初學者容易混淆 AI、ML 和 DL，它們的層次結構如下：
* **人工智慧 (Artificial Intelligence, AI)**：最廣義的範疇，指任何能讓電腦模擬人類智慧的技術（包含傳統的規則引擎、專家系統與啟發式演算法）。
* **機器學習 (Machine Learning, ML)**：AI 的子領域。電腦**不需要人類顯式編寫規則**，而是直接從歷史數據中「自我學習」並歸納出規律。
* **深度學習 (Deep Learning, DL)**：ML 的子領域。它使用多層的**類神經網路 (Artificial Neural Networks)** 來學習高度複雜的特徵（如影像辨識、自然語言處理）。

### 9.1.2 機器學習的三大核心任務

1. **監督式學習 (Supervised Learning)**：
   * 資料包含特徵 ($X$) 與標籤 ($y$)。
   * **分類 (Classification)**：標籤為離散的類別。
   * **迴歸 (Regression)**：標籤為連續的數值。
2. **非監督式學習 (Unsupervised Learning)**：
   * 資料只有特徵 ($X$)，沒有標籤。
   * **分群 (Clustering)**：自動將相似的樣本聚在一起。
3. **強化學習 (Reinforcement Learning)**：
   * 透過與環境互動（試錯），藉由獎勵與懲罰機制訓練代理人 (Agent) 做出最佳決策（如 AlphaGo、自駕車控制）。

### 9.1.3 偏差與變異的平衡 (Bias-Variance Tradeoff)

在評估機器學習模型時，我們通常會將預測誤差拆解為三個部分：**偏差 (Bias)**、**變異 (Variance)**，以及**不可避免的隨機噪聲 (Irreducible Error)**：
* **偏差 (Bias)**：代表模型對真實關係的錯誤假設。高偏差意指模型過於簡單（欠擬合），無法學好訓練集中的結構（如：用直線強行擬合二次曲線）。
* **變異 (Variance)**：代表模型對訓練資料細微波動的敏感度。高變異意指模型過於複雜（過擬合），背下了訓練集中的隨機噪聲。當輸入全新測試數據時，預測結果會大幅波動。

```
高 Bias / 低 Variance (Underfitting)   <----[ 平衡折衷點 ]----> 低 Bias / 高 Variance (Overfitting)
   (模型太簡單，學習力不足)                                         (模型太複雜，背下噪聲)
```

機器學習工程師的任務，就是尋找一個平衡點，使總誤差最小。

---

## 9.2 監督式學習：分類任務與超參數調校

分類任務是工程中最常見的應用。本節我們將深入探討三種經典分類器：**K-近鄰演算法 (KNN)**、**決策樹 (Decision Tree)** 與 **隨機森林 (Random Forest)**，並示範如何優化模型。

### 9.2.1 K-近鄰演算法 (KNN) 的數學原理

KNN 是一種「基於距離」的無參數演算法。當預測一個新樣本時，它會計算該點與訓練集中所有點的距離，找出最近的 $K$ 個鄰居，並以「多數決」決定新樣本的類別。
最常用的距離公式為**歐氏距離 (Euclidean Distance)**：

$$d(\mathbf{p}, \mathbf{q}) = \sqrt{\sum_{i=1}^{n} (p_i - q_i)^2$$

另一種為**曼哈頓距離 (Manhattan Distance)**：

$$d(\mathbf{p}, \mathbf{q}) = \sum_{i=1}^{n} |p_i - q_i|$$

### 9.2.2 決策樹 (Decision Tree) 原理

決策樹是透過一連串的「二分問答」將資料進行分割。它在每次分割時，會尋求讓子節點的**不純度 (Impurity)** 最低。常用的不純度指標為 **吉尼係數 (Gini Impurity)**：

$$Gini(D) = 1 - \sum_{i=1}^{C} P_i^2$$

其中 $P_i$ 是節點中第 $i$ 類樣本所佔的比例。Gini 越接近 0，代表該節點的資料類別越純。

### 9.2.3 整合集成學習：隨機森林 (Random Forest)

決策樹雖然直觀，但極易產生過擬合（高 Variance）。為了降低變異度，我們可以建構多個決策樹，並將它們的預測結果取平均（迴歸）或多數決（分類），這稱為 **集成學習 (Ensemble Learning)**。
隨機森林的兩個「隨機」要素：
1. **Bagging (Bootstrap Aggregating)**：隨機且有放回地抽取部分樣本訓練每棵樹。
2. **特徵隨機子集**：在每個節點分裂時，隨機選取部分特徵進行最優分裂評估，防止單一強特徵主導整棵樹。

### 9.2.4 實踐程式碼：雙模型對比與網格搜尋調參 (Grid Search)

在實務中，我們不能隨便猜測超參數（如 KNN 的 $K$ 值或決策樹的最大深度）。我們可以使用 `GridSearchCV` 自動嘗試各種超參數組合，並配合**交叉驗證 (Cross-Validation)** 找出最佳模型：

```python
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# 1. 載入鳶尾花資料集並分割
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.3, random_state=42
)

# 2. KNN 超參數網格搜尋
# 我們想要嘗試不同的 K (n_neighbors) 與距離計算方法 (weights)
knn_param_grid = {
    'n_neighbors': [1, 3, 5, 7, 9, 11],
    'weights': ['uniform', 'distance'],
    'metric': ['euclidean', 'manhattan']
}

# 使用 5 折交叉驗證 (cv=5) 進行網格搜尋
knn_grid = GridSearchCV(KNeighborsClassifier(), knn_param_grid, cv=5, scoring='accuracy')
knn_grid.fit(X_train, y_train)

print("=== KNN 參數調優結果 ===")
print(f"最佳參數組合：{knn_grid.best_params_}")
print(f"交叉驗證最佳分數：{knn_grid.best_score_:.4f}")

# 使用最佳模型對測試集進行預測
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

print("=== 決策樹參數調優結果 ===")
print(f"最佳參數組合：{tree_grid.best_params_}")
print(f"交叉驗證最佳分數：{tree_grid.best_score_:.4f}")

best_tree = tree_grid.best_estimator_
tree_pred = best_tree.predict(X_test)
print(f"測試集最終準確度：{accuracy_score(y_test, tree_pred):.4f}\n")


# 4. 隨機森林分類器測試
rf_model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
rf_model.fit(X_train, y_train)
rf_pred = rf_model.predict(X_test)
print("=== 隨機森林分類器結果 ===")
print(f"測試集準確度: {accuracy_score(y_test, rf_pred):.4f}")
```

---

### **9.2.5 隨堂測驗 (CCQ 1)**

**問題**

在機器學習中，使用 `GridSearchCV` 進行「超參數網格搜尋與交叉驗證」的主要目的為何？

A) 為了加速模型訓練的速度，避免使用 CPU。
B) 自動在各種參數組合中，透過交叉驗證找出最能防止過擬合且泛化能力最佳的參數設定。
C) 為了將無標籤的資料集進行自動分群。
D) 將特徵維度進行降維以利於繪圖。

<details>
<summary>點擊查看【隨堂測驗】答案與解析</summary>

**正確答案：B) 自動在各種參數組合中，透過交叉驗證找出最能防止過擬合且泛化能力最佳的參數設定。**

* **解析**：
  * `GridSearchCV` 會以「窮舉法」測試我們設定的網格內所有參數組合。
  * 對每組參數使用「K-折交叉驗證（K-Fold Cross Validation）」評估，以避免單次資料切片造成的偏差，最終挑選出平均效能最優異的引數組合，故選 B。

</details>

---

### **9.2.6 隨堂測驗 (CCQ 2)**

**問題**

當決策樹（Decision Tree）的 `max_depth` (最大深度) 參數設定為 `None`（即不限制樹的深度）時，模型通常會面臨什麼風險？

A) 模型會因為結構過於簡單而產生欠擬合 (Underfitting)。
B) 決策樹會無法進行多類別分類。
C) 決策樹會不斷分裂直到葉節點完全純淨，極易產生過擬合 (Overfitting) 並喪失對新測試資料的預測能力。
D) 程式會因為死迴圈而當機。

<details>
<summary>點擊查看【隨堂測驗】答案與解析</summary>

**正確答案：C) 決策樹會不斷分裂直到葉節點完全純淨，極易產生過擬合 (Overfitting) 並喪失對新測試資料的預測能力。**

* **解析**：
  * 若不限制最大深度，決策樹會盡可能將每一個訓練集樣本分得清清楚楚，甚至「背下」噪聲。
  * 這會導致樹狀圖極其複雜（過擬合），使得在訓練集上準確度為 100%，但在測試集上表現低落。限制樹的深度（剪枝，Pruning）是防止決策樹過擬合的常用手段。

</details>

---

## 9.3 監督式學習：迴歸任務與評估指標

當預測目標是連續數值時，我們會使用迴歸模型。

### 9.3.1 多元線性迴歸 (Multiple Linear Regression)

在現實生活中，預測結果通常受多個特徵影響。例如房價（$y$）不僅與坪數（$x_1$）有關，還受房間數（$x_2$）和屋齡（$x_3$）影響。其模型公式為：

$$\hat{y} = w_1 x_1 + w_2 x_2 + w_3 x_3 + b$$

我們的目標是透過**最小平方法 (Ordinary Least Squares, OLS)**，找到一組權重 $w$ 與截距 $b$，使得預測值 $\hat{y}$ 與真實值 $y$ 的誤差平方和最小。

### 9.3.2 正規化方法防止過擬合 (Lasso & Ridge)

當我們特徵非常多，或者特徵間高度相關時，線性迴歸容易對噪聲過擬合，導致權重 $w$ 的數值異常巨大。這時我們可以在損失函數中加入對權重大小的懲罰（正規化）：
1. **脊迴歸 (Ridge Regression / L2 正規化)**：
   $$\text{Loss} = \sum (y_i - \hat{y}_i)^2 + \alpha \sum w_j^2$$
   * 它會傾向於讓所有權重 $w$ 均勻地縮小，但不會縮減到絕對 0。
2. **套索迴歸 (Lasso Regression / L1 正規化)**：
   $$\text{Loss} = \sum (y_i - \hat{y}_i)^2 + \alpha \sum |w_j|$$
   * 它會強制讓一些不重要特徵的權重完全變為 0，具有特徵篩選 (Feature Selection) 的效果。

### 9.3.3 評估指標的數學定義

1. **平均絕對誤差 (Mean Absolute Error, MAE)**：
   $$MAE = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i|$$
   * 優點：物理意義直觀（平均誤差多少單位），對極端值較不敏感。
2. **均方誤差 (Mean Squared Error, MSE)**：
   $$MSE = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2$$
   * 特性：將誤差平方，對極端值非常敏感。
3. **決定係數 ($R^2$ Score, Coefficient of Determination)**：
   $$R^2 = 1 - \frac{\sum (y_i - \hat{y}_i)^2}{\sum (y_i - \bar{y}_i)^2}$$
   * 其反映模型對真實數據變異的解釋程度。

### 9.3.4 實踐程式碼：多元迴歸與正規化分析

```python
import numpy as np
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# 1. 產生模擬房產數據
np.random.seed(42)
num_samples = 150

size = 10 + 40 * np.random.rand(num_samples, 1)    # 10 ~ 50 坪
rooms = np.random.randint(1, 5, size=(num_samples, 1))  # 1 ~ 4 房
age = np.random.randint(1, 30, size=(num_samples, 1))   # 1 ~ 30 年屋齡

# 特徵矩陣 X (包含三個欄位)
X = np.hstack([size, rooms, age])

# 真實房價 (萬元) = 40*坪數 + 150*房間數 - 5*屋齡 + 100 + 噪聲
y = 40 * size + 150 * rooms - 5 * age + 100 + 80 * np.random.randn(num_samples, 1)
y = y.squeeze()

# 2. 分割資料集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. 訓練多元線性迴歸與脊迴歸模型
model = LinearRegression()
model.fit(X_train, y_train)

ridge_model = Ridge(alpha=10.0) # 設定懲罰項強度
ridge_model.fit(X_train, y_train)

# 4. 輸出模型學到的公式參數比較
print("=== Linear Regression weights ===")
print(f"坪數權重: {model.coef_[0]:.2f}, 房間權重: {model.coef_[1]:.2f}, 屋齡權重: {model.coef_[2]:.2f}")

print("\n=== Ridge Regression weights (L2 Penalty) ===")
print(f"坪數權重: {ridge_model.coef_[0]:.2f}, 房間權重: {ridge_model.coef_[1]:.2f}, 屋齡權重: {ridge_model.coef_[2]:.2f}")

# 5. 進行預測與評估
y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("\n=== Linear Regression 測試集評估指標 ===")
print(f"平均絕對誤差 (MAE): {mae:.2f} 萬元")
print(f"均方根誤差 (RMSE): {rmse:.2f} 萬元")
print(f"決定係數 (R2 Score): {r2:.4f}")
```

---

### **9.3.5 隨堂測驗 (CCQ 3)**

**問題**

在評估房價預測模型的效能時，若我們算出模型的決定係數 $R^2$ 值為 `0.85`，這代表什麼工程含義？

A) 該模型只預測對了 85% 的資料，剩下的 15% 資料全部預測錯誤。
B) 該模型所預測的房價比真實房價平均貴了 85 萬元。
C) 模型中的自變數（坪數、屋齡等特徵）能夠解釋因變數（房價）中 85% 的變異量。
D) 模型有 85% 的機率會產生過擬合。

<details>
<summary>點擊查看【隨堂測驗】答案與解析</summary>

**正確答案：C) 模型中的自變數（坪數、屋齡等特徵）能夠解釋因變數（房價）中 85% 的變異量。**

* **解析**：
  * $R^2$ 稱為決定係數，衡量的是模型擬合優度。
  * $R^2 = 0.85$ 表示系統總變異量中有 85% 可以由模型的迴歸方程式（自變數）所解釋，是評估迴歸擬合效能最通用的相對指標，故選 C。

</details>

---

## 9.4 非監督式學習：K-Means 資料分群與肘部法

非監督式學習在無標籤資料（如客戶分群、異常檢測）中應用廣泛。

### 9.4.1 K-Means 分群原理與限制

K-Means 將資料點指派給最近的群心，並迭代更新群心。
然而，K-Means 有兩個主要缺點：
1. **必須事先指定分群數 $K$**。
2. 對初始群心的位置敏感。Scikit-Learn 預設採用 `K-Means++` 演算法優化初始群心選擇。

此外，K-Means 假設資料群是呈「圓形球狀」且大小相近的分佈。如果資料群呈彎曲的新月形或長條狀，K-Means 的效果會非常差。這種情況下需要採用基於密度的分群演算法，如 **DBSCAN**。

### 9.4.2 肘部法 (Elbow Method) 尋找最佳 $K$ 值

為了找到最佳的群數 $K$，我們可以計算不同 $K$ 值下系統的**群內誤差平方和 (Within-Cluster Sum of Squares, WCSS)**，在 `sklearn` 中稱為 `inertia_`：

$$WCSS = \sum_{j=1}^{K} \sum_{i \in S_j} \|\mathbf{x}_i - \boldsymbol{\mu}_j\|^2$$

當 $K$ 值增加時，`inertia_` 必然會下降。但當 $K$ 達到某個臨界值後，下降幅度會明顯變平緩。這個轉折點（狀似手肘彎曲處）即為最佳的 $K$ 值。

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

# 1. 產生模擬的 2D 聚類資料 (設定實際有 4 個中心)
X, _ = make_blobs(n_samples=500, centers=4, cluster_std=0.7, random_state=42)

# 2. 計算不同 K 值的 Inertia 數值
inertia_list = []
k_range = range(1, 10)

for k in k_range:
    kmeans = KMeans(n_clusters=k, n_init='auto', random_state=42)
    kmeans.fit(X)
    inertia_list.append(kmeans.inertia_) # 獲取 WCSS 誤差和

# 3. 繪製肘部曲線圖
plt.figure(figsize=(8, 5))
plt.plot(k_range, inertia_list, marker='o', color='teal', linewidth=2)
plt.xlabel('Number of Clusters (K)')
plt.ylabel('Inertia (WCSS)')
plt.title('Elbow Method for Optimal K')
plt.grid(True)
plt.axvline(x=4, color='red', linestyle='--', label='Elbow Point (K=4)')
plt.legend()
plt.show()
```

---

### **9.4.3 隨堂測驗 (CCQ 4)**

**問題**

在實施 K-Means 分群時，使用「肘部法 (Elbow Method)」繪製曲線圖，下列哪一個關於轉折點（手肘處）的說法是正確的？

A) 轉折點代表 Inertia (WCSS) 開始變為負值的地方。
B) 轉折點代表在此群數之後，增加群數所能降低的群內誤差和幅度明顯變小，是邊際效應的轉折點。
C) 轉折點代表分群準確度達到 100% 的臨界點。
D) 轉折點後的 $K$ 值代表模型開始欠擬合。

<details>
<summary>點擊查看【隨堂測驗】答案與解析</summary>

**正確答案：B) 轉折點代表在此群數之後，增加群數所能降低的群內誤差和幅度明顯變小，是邊際效應的轉折點。**

* **解析**：
  * 當 $K$ 小於真實群數時，增加 $K$ 會劇烈降低誤差和。
  * 一旦 $K$ 超過真實群數，再細分群組所能降低的誤差和就微乎其微。因此，這個折線彎曲的地方就是平衡分群複雜度與誤差的最佳折衷點，故選 B。

</details>

---

## 9.5 關鍵觀念與特徵工程 (Feature Engineering)

資料前處理往往決定了機器學習的成敗。

### 9.5.1 特徵標準化 (Standardization) 與最小最大縮放 (MinMax Scaling)

* **StandardScaler (Z-Score 標準化)**：將資料縮放為平均數為 0，標準差為 1 的分佈。適合大多數演算法，對包含極端值的資料較具魯棒性。
* **MinMaxScaler (離差標準化)**：將資料等比例壓縮至 $[0, 1]$ 之間。

### 9.5.2 獨熱編碼 (One-Hot Encoding) 處理類別特徵

機器學習模型只認識數字。如果資料欄位包含「城市（台北、台中、高雄）」等非數值類別，我們不能直接將其編碼為 $1, 2, 3$，因為模型會誤以為存在順序關係。
我們必須使用**獨熱編碼 (One-Hot Encoding)**，將其轉為二進位獨立欄位：

```python
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

# 建立包含類別欄位的 DataFrame
df = pd.DataFrame({
    'CustomerID': [101, 102, 103],
    'City': ['Taipei', 'Taichung', 'Kaohsiung'],
    'Gender': ['Male', 'Female', 'Male']
})

print("=== 原始資料 ===")
print(df)

# 使用 pandas 快速取得一熱編碼的 dummy variables
df_encoded = pd.get_dummies(df, columns=['City', 'Gender'], dtype=int)
print("\n=== One-Hot 編碼後的資料 ===")
print(df_encoded)
```

---

### **9.5.3 隨堂測驗 (CCQ 5)**

**問題**

在處理具有「類別特徵（如：科系、血型）」的資料時，為什麼通常不建議直接將它們編碼為簡單的整數值（如資工=1, 電機=2, 機械=3），而是使用 One-Hot Encoding？

A) 因為 Scikit-Learn 的模型只支援輸入 0 或 1。
B) 為了避免模型錯誤地假設這些類別特徵之間存在大小順序或倍數關係。
C) One-Hot Encoding 可以自動刪除重複的特徵。
D) 整數編碼會佔用十倍以上的記憶體。

<details>
<summary>點擊查看【隨堂測驗】答案與解析</summary>

**正確答案：B) 為了避免模型錯誤地假設這些類別特徵之間存在大小順序或倍數關係。**

* **解析**：
  * 若使用 $1, 2, 3$ 編碼，距離型或線性模型會認為「機械 (3)」與「資工 (1)」的距離比「電機 (2)」大，或者認為科系可以做加減乘除。
  * 這不符合物理語意。One-Hot Encoding 透過將每個類別拉成獨立維度，確保它們彼此正交、距離均等，消除數值大小偏見，故選 B。

</details>

---

## 9.6 本章綜合實作專題

### 專題任務：紅酒品質多重分類器設計

**背景說明**：我們將利用 Scikit-Learn 進行一次完整的機器學習專題實作，包含資料前處理、標準化、決策樹模型建置，並透過網格搜尋優化模型來預測紅酒品質。

```python
import pandas as pd
import numpy as np
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, accuracy_score

# 1. 載入紅酒資料集 (包含化學成分特徵，預測 3 種不同酒廠紅酒)
wine = load_wine()
X = wine.data
y = wine.target

# 2. 切分資料集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# 3. 特徵標準化 (確保化學成分單位尺度一致)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test) # 注意測試集只能用 train 計算出來的平均與標準差進行轉換

# 4. 建立決策樹分類器並配置參數網格
dt_classifier = DecisionTreeClassifier(random_state=42)

param_grid = {
    'criterion': ['gini', 'entropy'],
    'max_depth': [3, 4, 5, 7, 10],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

# 5. 進行 5 折交叉驗證網格搜尋
grid_search = GridSearchCV(dt_classifier, param_grid, cv=5, scoring='accuracy')
grid_search.fit(X_train_scaled, y_train)

print(f"最佳參數組合: {grid_search.best_params_}")
print(f"交叉驗證最高 Accuracy: {grid_search.best_score_*100:.2f}%")

# 6. 使用最佳參數模型進行測試評估
best_model = grid_search.best_estimator_
y_pred = best_model.predict(X_test_scaled)

test_acc = accuracy_score(y_test, y_pred)
print(f"\n測試集最終 Accuracy: {test_acc*100:.2f}%")

# 7. 輸出詳細分類指標報告
print("\n詳細分類評估報告：")
print(classification_report(y_test, y_pred, target_names=wine.target_names))
```
