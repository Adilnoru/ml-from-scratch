from sklearn.datasets import load_breast_cancer

data = load_breast_cancer()

print(data["data"].shape)
print(data["target"].shape)
print(data["feature_names"])
print(data["target_names"])
print(data["DESCR"])
print(data["filename"])