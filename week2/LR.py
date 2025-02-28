from sklearn.linear_model import LogisticRegression
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
wine=datasets.load_wine()
X=wine.data
Y=wine.target
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.29, random_state=29,shuffle=True,stratify=Y)
from sklearn.preprocessing import StandardScaler
scalar=StandardScaler()
X_train_std=scalar.fit_transform(X_train)
X_test_std=scalar.transform(X_test)
lr=LogisticRegression()
lr.fit(X_train_std,Y_train)
Y_pred=lr.predict(X_test_std)
accuracy=accuracy_score(Y_test,Y_pred)
print("Accuracy: ",accuracy)