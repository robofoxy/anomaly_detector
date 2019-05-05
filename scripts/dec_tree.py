from import_data import *
from sklearn import tree
from sklearn.metrics import f1_score
from sklearn import preprocessing
import pickle

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


	clf = tree.DecisionTreeClassifier(criterion='entropy', splitter='best', max_depth=None, min_samples_split=40, min_samples_leaf=1, min_weight_fraction_leaf=0.0, max_features='log2', random_state=None, max_leaf_nodes=None, min_impurity_decrease=0.0, min_impurity_split=None, class_weight=None, presort=False)
	
	print "preprocessing is done!"
	print "ready to train!"
	clf = clf.fit(train_x, train_y)
	print "training is done!"
	print type(test_x)
	print test_x.shape
	print test_x
	prediction = clf.predict(test_x)
	print "Testing is done!"
	print ""
	print "Accuracy =", evaluate_tree(prediction, test_y, le)
	print "F1-Score =", f1_score(test_y, prediction, average='macro' )
	tree.export_graphviz(clf, out_file='tree.dot', feature_names=attribute_list[ : len(attribute_list)-1])
	pickle.dump(clf, open('tree_model.sav', 'wb'))

	# for import model:
	# clf = pickle.load(open(filename, 'rb'))

