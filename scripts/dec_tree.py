from import_data import *
from sklearn import tree
from sklearn.metrics import f1_score

#training_dataset = import_dataset(training_file)
test_dataset = import_dataset(test_file)

train_x, train_y = fetch_training_data()
test_x, test_y = fetch_test_data()

print "ready to train!"

print train_x.shape
print train_y.shape
print test_x.shape
print test_y.shape

