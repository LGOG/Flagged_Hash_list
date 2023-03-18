import requests
import numpy as np
import csv  
import re

#Add URL here#
url=["https://raw.githubusercontent.com/Neo23x0/signature-base/master/iocs/hash-iocs.txt"]
hash_List=[]

#for loop for all the URLs#
for i_url in url:
#Curl the list from the web#
	read = requests.get(i_url)
#Format it to a list format#
	text_read=(read.text)
	Sort_list=text_read.split("\n")
	for item in Sort_list:
		if "#" in item:
			pass
		else:
#Split the hash from the other infromation#
			x = item.split(';')
#Add only hashes, not new lines#
			if len(x[0]) > 3:
				hash_List.append((x[0]))
				hash_List.append("\n")
			else:
				pass			

# from the numpy module to created a cvs file
rows = [hash_List]
# from the numpy module to created a cvs file
with open("Bad_Hash.csv", "w") as f:
	np.savetxt(f, 
           rows,
   	      delimiter ="", 
       	   fmt ='% s')
