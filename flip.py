import urllib2
MyApi= "0c9cab886b7d40fe98dc2146cc93d6ab"
flip = urllib2.urlopen("https://affiliate-api.flipkart.net/affiliate/api/"+MyApi)
Dict1=dict(flip.read())
print Dict1 
