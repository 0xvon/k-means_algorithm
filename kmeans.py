import numpy as np
from sklearn import datasets
import matplotlib.pyplot as plt

def k_means(k, arr):
    centroids = np.random.randint(np.max(arr), size=(k, arr.ndim))

    error = 0.1

    for i in range(1000):

        labels = []

        # データの1つ1つを精査
        for index, data in enumerate(arr):

            min_distance = 10000000  # なるべく大きい数
            min_label = 0
            # セントロイド一つ一つと精査
            for cluster, centroid in enumerate(centroids):
                eucrid_distance = np.linalg.norm(data - centroid, ord=2)
                if min_distance > eucrid_distance:
                    min_distance = eucrid_distance
                    min_label = cluster

            labels.append(min_label)

        centroids_new = centroids
        for cluster in range(k):

            gravity_center = np.array([0, 0], dtype=np.float)
            for index, label in enumerate(labels):
                # 重心の計算
                if label == cluster:
                    gravity_center+= arr[index]

            gravity_center /= len(arr)
            centroids_new[cluster] = gravity_center

        er = []
        for cluster in range(k):
            centroid_error = np.linalg.norm(centroids_new[cluster] - centroids[cluster], ord=2)
            er.append(centroid_error)

        if np.mean(er) < error:
            centroids = centroids_new
            continue

        break

    return labels, centroids_new
