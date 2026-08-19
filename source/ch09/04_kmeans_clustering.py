# 04_kmeans_clustering.py - 非監督式學習：K-Means 資料分群與肘部法 (Elbow Method)

import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

# 1. 產生模擬的 2D 聚類資料 (設定實際有 4 個分群中心)
X, y_true = make_blobs(n_samples=500, centers=4, cluster_std=0.7, random_state=42)

# 2. 計算不同 K 值的 Inertia (群內誤差平方和 WCSS)
inertia_list = []
k_range = range(1, 10)

for k in k_range:
    kmeans = KMeans(n_clusters=k, n_init='auto', random_state=42)
    kmeans.fit(X)
    inertia_list.append(kmeans.inertia_)
    print(f"K = {k}, Inertia (WCSS) = {kmeans.inertia_:.2f}")

# 3. 繪製肘部曲線圖
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.scatter(X[:, 0], X[:, 1], s=20, color='gray', alpha=0.6)
plt.title("Raw Unlabeled Data (make_blobs)")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(k_range, inertia_list, marker='o', color='teal', linewidth=2)
plt.xlabel('Number of Clusters (K)')
plt.ylabel('Inertia (WCSS)')
plt.title('Elbow Method for Optimal K')
plt.grid(True)
plt.axvline(x=4, color='red', linestyle='--', label='Elbow Point (K=4)')
plt.legend()

plt.tight_layout()
plt.show()
