#Difference between dump() and dumps()
'''The json.dump() method converts a Python object into a JSON and writes it to a file
The json.dumps() method encodes a Python object into JSON and returns a string. '''

# *
def myfun(**kwargs):
    for key,value in kwargs.items():
        print("%s == %s" % (key,value))

myfun(first='ankita', mid='s', last='sharma')        