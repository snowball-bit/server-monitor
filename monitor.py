from server_monitor.system import get_system_status
import time
import os
import argparse
from datetime import datetime
import socket


CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 90
def positive_int(value):
	value = int(value)
	if value > 0:
		return value

	raise ValueError("interval must be greater than 0")

def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument("--interval", type=positive_int, default=5)
	parser.add_argument("--once", action="store_true")
	return parser.parse_args()

def main():
	args = parse_args()
	
	try:
		while True:
			status = get_system_status()
			os.system("cls" if os.name == "nt" else "clear")	
			print_status(status)
			if args.once :
				return
			time.sleep(args.interval)
	except KeyboardInterrupt:
		print("Stopping Server Monitor...")

def get_status_label(v , threshold):
	return '[HIGH]' if v >= threshold else '[OK]'

def format_status(status):
	return (
	f"Server Monitor\n"
	f"Host: {status['hostname']}\n"
	f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        f"CPU Usage: {status['cpu']}% {get_status_label(status['cpu'],CPU_THRESHOLD)}\n"
        f"Memory Usage: {status['memory']}% {get_status_label(status['memory'],MEMORY_THRESHOLD)}\n"
        f"Disk Usage: {status['disk']}% {get_status_label(status['disk'],DISK_THRESHOLD)}"
    )
def print_status(status):
	print(format_status(status))

if __name__ == "__main__":
    main()
