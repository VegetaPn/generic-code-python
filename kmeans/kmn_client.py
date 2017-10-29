#!/usr/bin/env python
# encoding: utf-8

from kmeans.kmn import Kmn


class KmnMovieLensClient(object):
	def __init__(self):
		self.train_filepath = './movielens/data/u.user'
		self.kmn = None

	def do_kmn(self, train_filepath=None):
		self.kmn = Kmn()
		self.kmn.load_data(self.load_data_from_file(train_filepath))
		self.kmn.go(5, 100)

	def load_data_from_file(self, file_path=None):
		if not file_path:
			file_path = self.train_filepath
		data_raw = []
		for line in open(file_path, 'r'):
			user_raw = line.split('|')
			data_raw.append(user_raw)
		return self.convert_data(data_raw)

	def convert_data(self, data_raw):
		job_name_list = []
		sex_name_list = []
		job_dict = dict()
		sex_dict = dict()
		data_metric = []
		for data in data_raw:
			metric = [int(data[0]), float(data[1])]
			sex_name = data[2]
			job_name = data[3]
			if sex_name not in sex_name_list:
				sex_name_list.append(sex_name)
				sex_dict[sex_name] = len(sex_name_list)
			if job_name not in job_name_list:
				job_name_list.append(job_name)
				job_dict[job_name] = len(job_name_list)
			metric.append(sex_dict.get(sex_name))
			metric.append(job_dict.get(job_name))
			data_metric.append(metric)
		return data_metric


if __name__ == '__main__':
	kmn_client = KmnMovieLensClient()
	kmn_client.do_kmn()
