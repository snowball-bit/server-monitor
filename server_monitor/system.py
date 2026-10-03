import psutil
import socket


def get_cpu_usage():
	return psutil.cpu_percent()

def get_memory_usage():

	memory = psutil.virtual_memory()
	return memory.percent

def get_disk_usage():
	disk = psutil.disk_usage("/")
	return disk.percent

def get_system_status():
	return {'cpu' : get_cpu_usage() , 'memory' : get_memory_usage() , 'disk':get_disk_usage(), "hostname": socket.gethostname()}
