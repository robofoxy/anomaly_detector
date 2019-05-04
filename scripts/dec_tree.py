from import_data import *
from sklearn import tree
from sklearn.metrics import f1_score

training_dataset = import_dataset(training_file)
test_dataset = import_dataset(test_file)

print "ready to train!"
