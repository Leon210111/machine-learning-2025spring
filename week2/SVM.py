from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score


wine=datasets.load_wine()
X=wine.data
Y=wine.target

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.29, random_state=29,shuffle=True,stratify=Y)
scalar=StandardScaler()
X_train=scalar.fit_transform(X_train)
X_test=scalar.transform(X_test)
svm_model=SVC(kernel='rbf',C=1.0,gamma='scale',random_state=29)
svm_model.fit(X_train,Y_train)
Y_pred=svm_model.predict(X_test)
accuracy=accuracy_score(Y_test,Y_pred)
print("Accuracy: ",accuracy)