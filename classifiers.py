#LOGISTICS REGRESSION
x = df.Age.values.reshape(-1,1)
y = df.Target.values
from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest = train_test_split(x,y, test_size = 0.25, random_state = 0)
ss = StandardScaler()
xtrain = ss.fit_transform(xtrain)
xtrain
xtest = ss.fit_transform(xtest)
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()
logreg.fit(xtrain,ytrain)
ypred = logreg.predict(xtest)
from sklearn.metrics import confusion_matrix








#RandomForestClassifier

from sklearn.ensemble import RandomForestClassifier
rfcl = RandomForestClassifier(n_estimators = 200, criterion = 'entropy')
rfcl.fit(xtrain, ytrain)
ypredrf = rfcl.predict(xtest)
cmrf = confusion_matrix(ytest,ypredrf)
cmrf

#DecisionTreeClassifier
from sklearn.tree import DecisionTreeClassifier
dtcl = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
dtcl.fit(xtrain,ytrain)


#KNN CLASSIFICATION
from sklearn.neighbors import KNeighborsClassifier
kncl =KNeighborsClassifier(n_neighbors = 3, metric = 'minkowski',p =2)
kncl.fit(xtrain,ytrain)
ypredknn = kncl.predict(xtest)

#NAIVE BAYES CLASSIFIER
from sklearn.naive_bayes import GaussianNB
nbcl = GaussianNB()
nbcl.fit(xtrain,ytrain)


