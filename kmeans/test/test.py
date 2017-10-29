#!/usr/bin/env python
# encoding: utf-8

from kmeans.kmn_client import KmnMovieLensClient


if __name__ == '__main__':
	kmn_client = KmnMovieLensClient()
	kmn_client.do_kmn('../movielens/data/u.user')
