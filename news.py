import urllib2
import smtplib
import json
import HTMLParser
def search():
	query='Delhi'
	final_url = ('https://ajax.googleapis.com/ajax/services/search/news?v=1.0&q='+query+'&userip=INSERT-USER-IP')
	json_obj=urllib2.urlopen(final_url)
	data=json.load(json_obj)
	send_email(data)
def send_email(data):
	FROM = "sender@example.com"
	TO = ["prakash.kumar94@live.com"] 
	SUBJECT = "Delhi Headlines"
	TEXT=""
	for news3 in data['responseData']['results']:
		TEXT=TEXT+"\n\n\n "
		atitle="Headline:"+str(news3['titleNoFormatting'])
		alink= "link:"+str(news3['unescapedUrl'])
		apublisher="published by-"+str(news3['publisher'])
        	TEXT=TEXT+atitle+"\n"+alink+"\n"+apublisher+"\n"
        	if  'relatedStories' in locals():
       			for news4 in news3['relatedStories']:
				a1title= "Headline:"+str(news4['titleNoFormatting'])
				a1link="link:"+str(news2['unescapedUrl'])
				a1publisher="published by-"+str(news4['publisher'])+"<p>"
				TEXT=TEXT+a1title+"\n"+a1link+"\n"+a1publisher+"\n"
		
	message = """\
	From: %s
	To: %s
	Subject: %s
	%s
	""" % (FROM, ", ".join(TO), SUBJECT, TEXT)
	# Send the mail
	server = smtplib.SMTP(host='smtp.gmail.com', port=587)
	server.starttls()
	server.login('gmail id', 'password')
	server.sendmail(FROM,TO,message)
	server.close()
				   
if __name__=="__main__":
   search()
