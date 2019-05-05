from import_data import *
from sklearn import tree
from sklearn.metrics import f1_score
from sklearn import preprocessing

print "preprocessing is starting!"
#training_dataset = import_dataset(training_file)
#test_dataset = import_dataset(test_file)


def evaluate_tree(arr, test_y, le):
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

	while(True):
		clf = tree.DecisionTreeClassifier(criterion="gini", min_samples_split=50, class_weight="balanced")
		#clf = tree.DecisionTreeClassifier(criterion='gini', splitter='best', max_depth=None, min_samples_split=0.35, min_samples_leaf=1, min_weight_fraction_leaf=0.0, max_features='log2', random_state=None, max_leaf_nodes=None, min_impurity_decrease=0.0, min_impurity_split=None, class_weight=None, presort=False)
		
		print "preprocessing is done!"
		print "ready to train!"
		clf = clf.fit(train_x, train_y)
		print "training is done!"
		arr = clf.predict(test_x)
		cur = evaluate_tree(arr, test_y, le)
		print "Accuracy:", cur
		break
		
