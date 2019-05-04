import numpy as np

attribute_list = ['duration', 'protocol_type', 'service', 'flag', 'src_bytes', 'dst_bytes', 'land', 'wrong_fragment', 'urgent', 'hot', 'num_failed_logins', 'logged_in', 'num_compromised', 'root_shell', 'su_attempted', 'num_root', 'num_file_creations', 'num_shells', 'num_access_files', 'num_outbound_cmds', 'is_host_login', 'is_guest_login', 'count', 'srv_count', 'serror_rate', 'srv_serror_rate', 'rerror_rate', 'srv_rerror_rate', 'same_srv_rate', 'diff_srv_rate', 'srv_diff_host_rate', 'dst_host_count', 'dst_host_srv_count', 'dst_host_same_srv_rate', 'dst_host_diff_srv_rate','dst_host_same_src_port_rate', 'dst_host_srv_diff_host_rate', 'dst_host_serror_rate', 'dst_host_srv_serror_rate', 'dst_host_rerror_rate', 'dst_host_srv_rerror_rate', 'type']

training_file = "../data/training.txt"
test_file = "../data/test.txt"

def isfloat(value):
        try:
            float(value)
            return True
        except ValueError:
            return False

def import_dataset(data_file):
	with open(data_file) as f:
		lines = f.readlines()
		dataset = []
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
		return dataset
		
						
#import_data("../data/test.txt")
