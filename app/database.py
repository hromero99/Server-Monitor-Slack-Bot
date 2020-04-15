import json


class Database(object):

	def __init__(self, json_path: str):
		self.database_path = json_path
		with open(json_path, 'r') as disk:
			self.data = json.load(disk)

	def save(self):
		with open(self.database_path, 'w') as diskfile:
			json.dump(self.data, diskfile)

	def add_new_server(self, server_url: str):
		if "servers" not in self.data.keys():
			self.data['servers'] = [server_url]
		self.data['servers'].append(server_url)
		self.save()

	def get_urls(self) -> list:
		return self.data["servers"]

