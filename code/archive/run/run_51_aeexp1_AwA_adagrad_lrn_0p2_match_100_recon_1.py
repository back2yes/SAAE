from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import math
import time
import os
import tensorflow as tf
import dataset
import aeexp1


def main(_):
	input_dim = 1024
	attr_dim = 85
	disp_dim = 85

	lrn_rate = 0.2
	train_batch_size = 16
	epoch_max = 100

	momentum = 0.9

	coef_match = 100
	coef_recon = 1

	train_size = 24295
	test_size = 6180
	#reg_lambda = 1.0 / train_size

	save_model_period = 10

	train_file_name = "../AwA/xTrain_scaled.npy"
	test_file_name = "../AwA/xTest_scaled.npy"

	train_label_file_name = "../AwA/yTrain.npy"
	test_label_file_name = "../AwA/yTest_relabeled.npy"

	train_attr_file_name = "../AwA/sTrain_scaled.npy"
	test_attr_file_name = "../AwA/sTest_scaled.npy"

	log_directory = "./log/log_51_aeexp1_AwA_adagrad_lrn_0p2_match_100_recon_1"
	log_file_name_head = log_directory + "/log"
	if not os.path.exists(log_directory):
		os.makedirs(log_directory)

	#load_model_directory = "./log/log_27_lrn_0p02_data_AwA_match_1_adagrad_2"
	load_model_directory = None

	machine = aeexp1.aeexp1(
		input_dim, attr_dim, disp_dim,
		lrn_rate, train_batch_size, epoch_max, momentum = momentum,
		coef_match = coef_match, coef_recon = coef_recon,
		train_file_name = train_file_name,
		test_file_name = test_file_name,
		train_label_file_name = train_label_file_name,
		test_label_file_name = test_label_file_name,
		train_attr_file_name = train_attr_file_name,
		test_attr_file_name = test_attr_file_name,
		log_file_name_head = log_file_name_head,
		save_model_period = save_model_period,
		load_model_directory = load_model_directory)

	machine.train()


if __name__ == "__main__":
	tf.app.run(main = main, argv = None)
