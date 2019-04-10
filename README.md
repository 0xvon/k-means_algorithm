# k-menas法
教師なし学習、クラスタリングの主力アルゴリズム「k-means法」をnumpyベースで実装しました

試しに以下のコードを付け足して見てください

```Python
clusters = 2
dataset = datasets.make_blobs(centers=clusters)
features = dataset[0]

pred, centroids = k_means(clusters, features)
print(pred)

# 各要素をラベルごとに色付けして表示する
for index, label in enumerate(pred):
    if label == 0:
        plt.scatter(features[index][:][0], features[index][:][1], color="r")
    if label == 1:
        plt.scatter(features[index][:][0], features[index][:][1], color="b")

plt.show()
```

すると上手くクラスタリングされます
`scikit-learn`とは使い勝手が違うので注意してください

<img src="https://aidemyexstorage.blob.core.windows.net/aidemycontents/1554885576220354.png">
