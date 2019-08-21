import numpy as np

d = 7
train_n = 1000
test_n = 10000

X_train = np.random.choice([0, 1], size=(train_n, d), p=[1./2, 1./2])
X_test = np.random.choice([0, 1], size=(test_n, d), p=[1./2, 1./2])
Y_train = np.zeros(train_n)
Y_test = np.zeros(test_n)

for i in range(train_n):
	Y_train[i] = np.sum(X_train[i])%2

for i in range(test_n):
	Y_test[i] = np.sum(X_test[i])%2


X_train.sort()
X_test.sort()

def get_data():
	return (X_train,Y_train,X_test,Y_test)