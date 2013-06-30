import urllib2
def summary(c):
	d=c.split("<plot_simple>")
	c=d[1]
	e=c.split("</plot_simple>")
	return e[0]
def rat(c):
	d=c.split("<rating>")
	c=d[1]
	e=c.split("</rating>")
	return e[0]
def parser(url):
	a=urllib2.urlopen("http://imdbapi.org?type=xml&q="+url)
	b=a.read()
	c="Summary:"+summary(b)
	d="Rating:"+rat(b)+" out of ten"
	e=(c,d)
	return e
#print(parser("The matrix"))
