from import_data import *
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import f1_score
from sklearn import preprocessing
import pickle
from sklearn.externals import joblib

def evaluate_network(arr, test_y):
	sz = len(arr)
	res = []
	acc = 0

	for i in range(sz):
		if test_y[i][0] == arr[i]:
			acc += 1
	return float(acc) / sz


if __name__=='__main__':

	train_x, train_y, test_x, test_y, le = fetch_training_testing_data()
	
	train_x = train_x.astype(float)
	train_y = train_y.astype(float)
	test_x = test_x.astype(float)
	test_y = test_y.astype(float)
	print "After preprocessing"
	for i in range(4,20):
		for j in range(8,20):
			for k in range(4,20):
				print ""
				clf = MLPClassifier(solver='adam', alpha=0.00001, hidden_layer_sizes=(i, j, k), random_state=1)
				print "ANN Classifier is created!"
				clf.fit(train_x, train_y)
				print "Training is done!"
				joblib.dump(clf, 'ann.pkl')
				prediction = clf.predict(test_x)
				print "Testing is done!"
				print "RESULTS:", i, j, k, 'adam'
				print "Accuracy =", evaluate_network(prediction, test_y)
				print "F1-Score =", f1_score(test_y, prediction, average='macro' )
	
