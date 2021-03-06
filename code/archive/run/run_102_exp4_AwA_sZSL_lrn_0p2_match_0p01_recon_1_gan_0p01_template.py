from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import tensorflow as tf
import aaeexp4


"""
Please try:

coef_match = [0.001, 0.01, 0.1, 1, 10, 100, 1000]
coef_recon = 1
coef_gan = [0.01, 0.0001]

"""


def main(_):
	input_dim = 1024
	hid_dim = 85

	d1 = 100

	lrn_rate = 0.2
	train_batch_size = 64
	epoch_max = 100

	#momentum = 0.9

	gaus_mean = 0.21
	gaus_stddev = 0.25

	coef_match = 0.01
	coef_recon = 1
	coef_gan = 0.01

	#train_size = 24295
	#test_size = 6180
	#reg_lambda = 1.0 / train_size

	save_model_period = 1

	generalizedZSL = False

	unseen_class_file_name = "../AwA_standardZSL/unseen_class.npy"

	train_file_name = "../AwA_standardZSL/xTrain_scaled.npy"
	test_file_name = "../AwA_standardZSL/xTest_scaled.npy"

	train_label_file_name = "../AwA_standardZSL/yTrain.npy"
	test_label_file_name = "../AwA_standardZSL/yTest.npy"

	test_attr_file_name = "../AwA_standardZSL/sTest_scaled.npy"

	log_directory = "./log/log_102_exp4_AwA_sZSL_lrn_0p2_match_0p01_recon_1_gan_0p01_template"
	log_file_name_head = log_directory + "/log"
	if not os.path.exists(log_directory):
		os.makedirs(log_directory)

	#load_model_directory = "./log/log_27_lrn_0p02_data_AwA_match_1_adagrad_2"
	load_model_directory = None

	machine = aaeexp4.aaeexp4(
		input_dim, hid_dim, d1,
		lrn_rate, train_batch_size, epoch_max,
		gaus_mean = gaus_mean, gaus_stddev = gaus_stddev,
		coef_match = coef_match, coef_recon = coef_recon, coef_gan = coef_gan,
		unseen_class_file_name = unseen_class_file_name,
		train_file_name = train_file_name,
		test_file_name = test_file_name,
		train_label_file_name = train_label_file_name,
		test_label_file_name = test_label_file_name,
		test_attr_file_name = test_attr_file_name,
		log_file_name_head = log_file_name_head,
		save_model_period = save_model_period,
		load_model_directory = load_model_directory,
		generalizedZSL = generalizedZSL)

	machine.train()


if __name__ == "__main__":
	tf.app.run(main = main, argv = None)
