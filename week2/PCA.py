from sklearn import datasets
wine=datasets.load_wine()
X=wine.data
Y=wine.target
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1, random_state=29,shuffle=True,stratify=Y)
from sklearn.preprocessing import StandardScaler
scalar=StandardScaler()
X_train_std=scalar.fit_transform(X_train)
X_test_std=scalar.transform(X_test)
from sklearn.decomposition import PCA
pca=PCA(n_components=2)
X_train_reduced=pca.fit_transform(X_train_std)
X_test_reduced=pca.transform(X_test_std)
#print("降维前：",X_test_std[:3],sep='/n')
#print("降维后：",X_test_PCA[:3],sep='/n')
from sklearn.linear_model import LogisticRegression
lr=LogisticRegression()
lr.fit(X_train_reduced,Y_train)
Y_pred=lr.predict(X_test_reduced)
from sklearn.metrics import accuracy_score
accuracy=accuracy_score(Y_test,Y_pred)
print("Accuracy: ",accuracy)