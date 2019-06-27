import sys
import ipaddress
input = open(sys.argv[1], "r")

outC = []
outM = []
for line in open("close", "r"):
	arr = line.split(",")
	outC.append(  (ipaddress.IPv4Address(arr[0]), ipaddress.IPv4Address(arr[1][:-1]))  )

print(outC)

for o in outC:
	print(str(int(o[0]))+","+str(int(o[1])))


for line in open("medium", "r"):
	arr = line.split(",")
	outM.append(  (ipaddress.IPv4Address(arr[0]), ipaddress.IPv4Address(arr[1][:-1])) )


flag = False
for line in input:
	flag = False

	toint = int(ipaddress.IPv4Address(line[:-1]))
	for range in outC:
		if toint >= int(range[0]) and toint <= int(range[1]):
#			print(line[:-1]+"("+str(toint)+") is very close to campus")
			flag = True

	for range in outM:
		if toint >= int(range[0]) and toint <= int(range[1]):
#			print(line[:-1]+" is kind closeish to campus")
			flag = True

	if flag == False:
		print(line[:-1]+" is very far from campus")
		continue
