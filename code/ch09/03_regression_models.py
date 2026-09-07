# 03_regression_models.py - 監督式多元線性迴歸、L1/L2 正規化與模型評估 (MAE, RMSE, R2)

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

# 特徵矩陣 X
X = np.hstack([size, rooms, age])

# 真實房價 (萬元) = 40*坪數 + 150*房間數 - 5*屋齡 + 100 + 隨機噪聲
y = 40 * size + 150 * rooms - 5 * age + 100 + 80 * np.random.randn(num_samples, 1)
y = y.squeeze()

# 2. 分割訓練集與測試集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. 訓練多元線性迴歸、脊迴歸 (Ridge) 與套索迴歸 (Lasso)
lr = LinearRegression()
lr.fit(X_train, y_train)

ridge = Ridge(alpha=10.0)
ridge.fit(X_train, y_train)

lasso = Lasso(alpha=5.0)
lasso.fit(X_train, y_train)

# 4. 輸出權重比較
print("=== 模型權重係數比較 ===")
print(f"Linear Regression 權重: 坪數={lr.coef_[0]:.2f}, 房間={lr.coef_[1]:.2f}, 屋齡={lr.coef_[2]:.2f}, 截距={lr.intercept_:.2f}")
print(f"Ridge (L2) 權重:        坪數={ridge.coef_[0]:.2f}, 房間={ridge.coef_[1]:.2f}, 屋齡={ridge.coef_[2]:.2f}")
print(f"Lasso (L1) 權重:        坪數={lasso.coef_[0]:.2f}, 房間={lasso.coef_[1]:.2f}, 屋齡={lasso.coef_[2]:.2f}")

# 5. 線性迴歸測試集預測與評估指標
y_pred = lr.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("\n=== Linear Regression 測試集評估指標 ===")
print(f"平均絕對誤差 (MAE): {mae:.2f} 萬元")
print(f"均方根誤差 (RMSE):   {rmse:.2f} 萬元")
print(f"決定係數 (R2 Score): {r2:.4f}")
