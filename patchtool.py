import json, sys

## initial
f = open("evasion-rules.nools","r")
f_json = open("evasion.json","r")
f_new = open("new.nools","w")
ret = 0
## read json file
data = f.read()
data_json = json.load(f_json)

## show data in json
for i in data_json['v9']:
	print(i),
	for x in data_json['v9'][i]:
		print(x),
	print("")

## replace rule
r_str = "\"T1099.11\""
for i in data_json['v9']:
	ret = data.find(i,0,len(data))
        y = data.find("d.withMitreInfo", ret, len(data))
	print("index of y is", y)
	z = data.find("]", y, len(data))
	print("index of z is ", z)
	data = data[0: y+17:] + r_str + data[z + 1::]
	print(data)
f_new.write(data)	

#variable
index = 0
x = 0
value = True

while True:
	#search rule
	x = data.find("evasion", index, len(data))
	if x == -1:
		#print("Reach EOF")
		sys.exit()
	#print("[DEBUG]index is", x)
	#print(data[x:x+14]),
	
	#search Mitre rule 
	y = data.find("d.withMitreInfo", x, len(data))
	if y == -1 :
		index = x 
		index += 13
		#print("This rule doesn't have mitre technique")
		continue
	
	#search end of technique
	z = data.find("]", y, len(data))
	#print(data[y+17:z]),	
	#print("")
	index = x
	index += 13

f.close()
f_json.close()	
