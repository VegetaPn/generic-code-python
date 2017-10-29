#!/usr/bin/env python
# encoding: utf-8
import sys
import random


# data_metric数据格式: [id, x, y, z, ...]
class Kmn(object):
	def __init__(self):
		self.k = 10
		self.data = []
		self.clusters = dict()
		self.centers = []
		self.center_clusterindex = dict()
		self.dim = 0

	def go(self, k=5, max_round=100):
		self.init_data(k)
		for i in range(max_round):
			print(u'进行第' + str(i + 1) + u'轮聚类...')
			self.do_cluster_round()
			# self.recal_center()
			print(u'第' + str(i + 1) + u'轮聚类完成...')
		print(u'------------ Done !!! ----------------')
		print(self.clusters)

	def init_data(self, k):
		self.k = k
		self.init_centers()
		# self.init_cluster()

	def load_data(self, data_metric):
		if not data_metric or len(data_metric) == 0 or not data_metric[0] or len(data_metric) <= 1:
			raise Exception(u'load data error: 数据格式不符合要求')
		self.data = data_metric
		self.dim = len(self.data[0]) - 1
		print(u'data加载完成')

	def init_cluster(self):
		if len(self.centers) < self.k:
			raise Exception(u'中心点初始化错误')
		for i in range(self.k):
			self.clusters[i] = []
			self.center_clusterindex[self.centers[i][0]] = i
		print(u'初始化cluster完成')

	# 初始化中心点
	def init_centers(self):
		if self.k > len(self.data):
			raise Exception(u'error: k > 数据量')
		random_index_list = random.sample(range(1, len(self.data)), self.k)
		for index in random_index_list:
			self.centers.append(self.data[index])
		print(u'初始化中心点完成, 中心点: ' + str(self.centers))

	def do_cluster_round(self):
		self.init_cluster()
		for item in self.data:
			least_distance = sys.maxint
			cluster_index = None
			for center in self.centers:
				distance = self.cal_distance(item[1:], center[1:], self.dim)
				if least_distance > distance:
					least_distance = distance
					cluster_index = self.center_clusterindex[center[0]]
			self.clusters[cluster_index].append(item)
		self.recal_center()
		print(u'当前分类完成...')

	def recal_center(self):
		self.centers = []
		for i in range(self.k):
			cluster = self.clusters.get(i)
			if not cluster:
				print(u'\n-------随机数产生不理想, 导致某一个聚类中心点集合为空, 请重新运行-------\n')
				raise Exception(u'随机数产生不理想, 导致某一个聚类中心点集合为空, 请重新运行')
			center_i = [0] * (1 + self.dim)
			for item in cluster:
				center_i = [sum(zip_item) for zip_item in zip(center_i, item)]
			center_i = [x / len(cluster) for x in center_i]
			self.centers.append(center_i)
		print(u'重新计算中心点完成, 中心点: ' + str(self.centers))

	def cal_distance(self, p1, p2, dim):
		distance = 0
		for i in range(dim):
			distance += (float(p1[i]) - float(p2[i])) ** 2
		return distance

