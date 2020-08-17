from itertools import count
import matplotlib.pyplot as plt
from pandas import read_csv
from matplotlib.animation import FuncAnimation
import csv
import random
import time
import os
def LIVECSV():
	path = 'E:\\My Projects\\2019 Works\\Python\\Sublime\\Matplotlib'
	os.chdir(path)
	if 'CSVDataGenerator' not in os.listdir():
		os.mkdir('CSVDataGenerator')
	os.chdir('CSVDataGenerator')

	x_vals = 0
	total_1 = 1000
	total_2 = 1000
	# Headers
	fieldnames = ['xvals','total_1','total_2']
	# mode 'r' means reading, 'w' writing and 'a' appending
	# Writing headers
	with open('data.csv' , 'w') as f:
		csv_writer = csv.DictWriter(f , fieldnames = fieldnames)
		csv_writer.writeheader()
	# Now, writing data
	while True:
		with open('data.csv' , 'a') as f:
			csv_writer = csv.DictWriter(f , fieldnames = fieldnames)
			info = {'xvals':x_vals,
			'total_1':total_1,'total_2':total_2}
			csv_writer.writerow(info)
			print(x_vals,total_1,total_2)
			x_vals += 1
			total_1 = total_1 + random.randint(-6 , 8)
			total_2 = total_2 + random.randint(-5 , 6)
		# a simple pause in between writing data in secs
		# you can do it for milisecs with a dot behind digits
		time.sleep(1)
