#this is how to define dictionary in python
pythonDic = {}

#this is how add values for dictionary

pythonDic = {'janidu' : 'most kind person i ever met' , 'yoshini' : 'most angryful girl i ever met'}

print(pythonDic.items())
print(pythonDic.keys())
print(pythonDic.values())

pythonDic['hansika'] = 'she is pretty but high class,cant reach from in my level'
print(pythonDic.items())

#delete items from the dictionary
del(pythonDic['hansika'])
print(pythonDic.items())

pythonDic.clear()
print(pythonDic.items())
