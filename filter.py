import sys
import csv

input = open(sys.argv[1], "r")


reader = csv.reader(input)
for arr in reader:
	lat = float(arr[6])
	lon = float(arr[7])
	v = len(arr[1])
	if lat < 54.79 and lat > 24.79 and lon > -104.99 and lon < -74.49 and ":" not in arr[1]:
		print(arr[0]+","+arr[1])
