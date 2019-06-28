import sys
import csv
import ipaddress
input = open(sys.argv[1], "r")


reader = csv.reader(input)
for arr in reader:
	lat = float(arr[6])
	lon = float(arr[7])
	v = len(arr[1])
	if lat < 40.09 and lat > 37.49 and lon > -91.29 and lon < -88.69 and ":" not in arr[1]:
		print(str(int(ipaddress.IPv4Address(arr[0])))+","+str(int(ipaddress.IPv4Address(arr[1])))+","+arr[3]+","+arr[4]+","+arr[5]+",C")
	elif lat < 48.79 and lat > 28.79 and lon > -99.99 and lon < -79.99 and ":" not in arr[1]:
                print(str(int(ipaddress.IPv4Address(arr[0])))+","+str(int(ipaddress.IPv4Address(arr[1])))+","+arr[3]+","+arr[4]+","+arr[5]+",M")
	elif ":" not in arr[1]:
		print(str(int(ipaddress.IPv4Address(arr[0])))+","+str(int(ipaddress.IPv4Address(arr[1])))+","+arr[3]+","+arr[4]+",F")

