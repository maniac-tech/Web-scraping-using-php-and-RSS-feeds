dict = {
	"key1":"value1",
	"key2":"value2",
	"key3":"value3",
	"key4":"value4"
}

#iterating over keys:
# for x in dict.iterkeys():
# 	print (x)

#iteraing over values:
# for x in dict.itervalues():
# 	print(x)

#iterating over values using keys:
for x in dict.iterkeys():
	print(dict[x])	