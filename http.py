import urllib2
page = urllib2.urlopen("http://www.google.com").read()
print page