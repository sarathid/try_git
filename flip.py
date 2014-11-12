import urllib2
import json
MyApi= "0c9cab886b7d40fe98dc2146cc93d6ab"
flip = urllib2.urlopen("https://affiliate-api.flipkart.net/affiliate/api/"+MyApi+'.json').read()
Response = json.loads(flip)
print "flipkart Response Keys"
print Response.keys()
print "flipkart Response Title:"
print Response['title']
print "flipkart Description"
print Response["description"]
print "flipkart's API Groups"
for x in Response["apiGroups"]["affiliate"]["apiListings"].keys():
	print x
	url_id=Response["apiGroups"]["affiliate"]["apiListings"][x]["availableVariants"]["v0.1.0"]["get"]
	print url_id
	data = urllib2.urlopen(url_id).read()
	new_flip=open(r"F:\\Codes\\Flipkart\\"+x+".json")
	new_flip.write(data)
	new_flip.close()
