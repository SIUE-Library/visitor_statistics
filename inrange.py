import sys
import ipaddress
input = open(sys.argv[1], "r")

outC = []
outM = []
for line in open("close", "r"):
	arr = line.split(",")
	outC.append(  (ipaddress.IPv4Address(arr[0]), ipaddress.IPv4Address(arr[1]), arr[2], arr[3], arr[4][:-1])   )


for line in open("medium", "r"):
	arr = line.split(",")
	outM.append(  (ipaddress.IPv4Address(arr[0]), ipaddress.IPv4Address(arr[1]), arr[2], arr[3], arr[4][:-1]) )


flag = False
for line in input:
	flag = False

	toint = int(ipaddress.IPv4Address(line[:-1]))
	for range in outC:
		if toint >= int(range[0]) and toint <= int(range[1]):
			print(line[:-1]+","+str(toint)+","+range[2]+","+range[3]+","+range[4]+","+range[4]+",Commuter")
			flag = True

	for range in outM:
		if toint >= int(range[0]) and toint <= int(range[1]):
			print(line[:-1]+","+range[2]+","+range[3]+","+range[4]+",Remote")
			flag = True

	if flag == False:
		print(line[:-1]+",Distant")
		continue
