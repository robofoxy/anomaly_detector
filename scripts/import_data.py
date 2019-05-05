import numpy as np
from sklearn import preprocessing

attribute_list = ['duration', 'protocol_type', 'service', 'flag', 'src_bytes', 'dst_bytes', 'land', 'wrong_fragment', 'urgent', 'hot', 'num_failed_logins', 'logged_in', 'num_compromised', 'root_shell', 'su_attempted', 'num_root', 'num_file_creations', 'num_shells', 'num_access_files', 'num_outbound_cmds', 'is_host_login', 'is_guest_login', 'count', 'srv_count', 'serror_rate', 'srv_serror_rate', 'rerror_rate', 'srv_rerror_rate', 'same_srv_rate', 'diff_srv_rate', 'srv_diff_host_rate', 'dst_host_count', 'dst_host_srv_count', 'dst_host_same_srv_rate', 'dst_host_diff_srv_rate','dst_host_same_src_port_rate', 'dst_host_srv_diff_host_rate', 'dst_host_serror_rate', 'dst_host_srv_serror_rate', 'dst_host_rerror_rate', 'dst_host_srv_rerror_rate', 'type']

training_file = "../data/training.txt"
test_file = "../data/test.txt"



def isfloat(value):
        try:
            float(value)
            return True
        except ValueError:
            return False

def write_set(string_set):
	with open('../scripts/string_set.txt', 'w') as filehandle:
		filehandle.writelines("%s\n" % item for item in string_set)

def read_set():
	with open('../scripts/string_set.txt', 'r') as filehandle:  
		filecontents = filehandle.readlines()
		string_set = []
		for line in filecontents:
			item = line[:-1]
			string_set.append(item)

		return string_set

sset = read_set()

def encode_feature_vector(vector_string):
	vector = vector_string.split(',')
	vector = vector[:len(vector) - 1]

	le = preprocessing.LabelEncoder()
	le.fit(sset)
	for i in range(0, len(vector)):
		if (not vector[i].isdigit()) and (not isfloat(vector[i])):
			vector[i] = str(le.transform([vector[i]])[0])
	return vector

def decode_label(label_arr):
	le = preprocessing.LabelEncoder()
	le.fit(sset)

	return le.inverse_transform([int(label_arr[0])])[0]

def import_dataset(data_file):
	with open(data_file) as f:
		lines = f.readlines()
		dataset = []
		#q = 0
		for line in lines:
			packet_feature_vector = line.split(',')
			row = []
			for attribute in attribute_list:
				feature = packet_feature_vector[attribute_list.index(attribute)]
				if feature.isdigit():
					feature = int(feature)
				elif isfloat(feature):
					feature = float(feature)
				row.append(feature)
			row[len(row) - 1] = row[len(row) - 1][0 : len(row[len(row) - 1]) - 2]

			if row[len(row) - 1] != "normal":
				row[len(row) - 1] = "anomalous"

			dataset.append(row)
			"""
			q += 1
			if q == 100:
				break
			"""
		return np.array(dataset)


def prepare_encoder(dataset_train, dataset_test):
	string_set = set()
	rows_train = dataset_train.shape[0]
	cols_train = dataset_train.shape[1]
	rows_test = dataset_test.shape[0]
	cols_test = dataset_test.shape[1]
	print "preparing encoder..."

	print "---- checking TRAINING dataset ----"
	for i in range(rows_train):
		if i%100000 == 0:
			print "checking row", i, "/", rows_train
		for j in range(cols_train):
			if (not dataset_train[i][j].isdigit()) and (not isfloat(dataset_train[i][j])):
				string_set.add(dataset_train[i][j])

	print "---- checking TEST dataset ----"
	for i in range(rows_test):
		if i%100000 == 0:
			print "checking row", i, "/", rows_test
		for j in range(cols_test):
			if (not dataset_test[i][j].isdigit()) and (not isfloat(dataset_test[i][j])):
				string_set.add(dataset_test[i][j])

#	print string_set
	le = preprocessing.LabelEncoder()
	le.fit(list(string_set))
	#write_set(list(string_set))
	return le

def encode_data(dataset_train, dataset_test):
	le = prepare_encoder(dataset_train, dataset_test)
	rows_train = dataset_train.shape[0]
	cols_train = dataset_train.shape[1]
	rows_test = dataset_test.shape[0]
	cols_test = dataset_test.shape[1]

	print "---- modifying TRAINING dataset ----"
	for i in range(rows_train):
		if i%100000 == 0:
			print "modifying row", i, "/", rows_train
		for j in range(cols_train):
			if (not dataset_train[i][j].isdigit()) and (not isfloat(dataset_train[i][j])):
				dataset_train[i][j] = str(le.transform([dataset_train[i][j]])[0])

	print "---- modifying TEST dataset ----"
	for i in range(rows_test):
		if i%100000 == 0:
			print "modifying row", i, "/", rows_test
		for j in range(cols_test):
			if (not dataset_test[i][j].isdigit()) and (not isfloat(dataset_test[i][j])):
				dataset_test[i][j] = str(le.transform([dataset_test[i][j]])[0])

	return dataset_train, dataset_test, le

def fetch_training_testing_data():
	dataset_train, dataset_test, le = encode_data(import_dataset(training_file), import_dataset(test_file))

	#print dataset.shape
	return dataset_train[:, 0:len(dataset_train[0])-1], dataset_train[:, len(dataset_train[0])-1:len(dataset_train[0])], dataset_test[:, 0:len(dataset_test[0])-1], dataset_test[:, len(dataset_test[0])-1:len(dataset_test[0])], le

#import_data("../data/test.txt")
#train_x, train_y = fetch_training_data()
#train_x, train_y,test_x, test_y = fetch_training_testing_data():()
#print train_x.shape
#print train_y.shape
#print encode_feature_vector("anomalous,normal,3.14.")
#print decode_label(['14'])
