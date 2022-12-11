import hashlib
import json
from time import time
from urllib.parse import urlparse
from uuid import uuid4

import requests
from flask import Flask, jsonify, request


class Blockchain:

	def __init__(self):
		self.current_transaction = []
		self.chain = []
		self.nodes = set()

		# Tworzenie bloku tranzakcyjnego
		self.new_block(previous_hash='1', proof=100)

	def register_node(self, address):
		'''
		Dodawanie nowego wezla do listy wezlow

 		:param address: Adres wezla Eg. 'http://192.168.0.5:5000'
		'''

		parsed_url = urlpare(address)
		if parsed_url.netloc:
			self.nodes.add(parsed_url.netloc)
		elif parsed_url.path:
			# Accepts an URL without scheme
			self.nodes.add(parsed_url.path)
		else:
			raise ValueError('Invalid URL')

	def valid_chain(self, chain):
		'''
		
		'''
