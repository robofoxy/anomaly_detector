from import_data import *
from sklearn import svm
from sklearn.metrics import f1_score
from sklearn import preprocessing
import pickle

def evaluate_svm(arr, test_y, le):
	sz = len(arr)
	res = []
	acc = 0

	for i in range(sz):
		#print [int(test_y[i][0])], "      ", [int(arr[i])]
		#print "test_y:", le.inverse_transform([int(test_y[i][0])]), "actual_r:", le.inverse_transform([int(arr[i])])
		if test_y[i][0] == arr[i]:
			acc += 1
		#print "ACC = ", acc, "SZ = ", sz
	return float(acc) / sz

if __name__=='__main__':

	train_x, train_y, test_x, test_y, le = fetch_training_testing_data()
	
	clf = svm.SVC(C=0.225, cache_size=400, class_weight=None, coef0=0.0, decision_function_shape='ovr', degree=2, gamma=2.8, kernel='rbf', max_iter=-1, probability=False, random_state=None, shrinking=True, verbose=False,tol=0.0147)
	
	clf.fit(train_x,train_y)
	
	prediction = clf.predict(test_x)
	
	
	print "Accuracy =", evaluate(prediction, test_y, le)
	print "F1-Score =", f1_score(test_y, prediction, average='macro')
	
	
