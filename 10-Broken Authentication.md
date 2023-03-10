# The Different Method Are :

## 1. Bypass OTP:
### Description :
A one-time password for logging in or forgetting the password of various sites.
The number we use in this method can have an account on the site or not, in which case we can create an account on the target site with that number without the permission of the owner of the number.

### How To Do :
enter the phone number and click ok---> a 4 to 6 digit code is sent to the phone number ---> turn on the foxy proxy and 9-Burp Suite ---> in the field related to the sent code, enter a random number, such as : 000000 ---> in Burp Suite, we right-click on the proxy section ---> do intercept ---> response to this request (In this section, we first see the request and send it to the browser if we want) ---> If the status was <mark style="background: #FF5582A6;">false</mark> , we will change it to : <mark style="background: #FF5582A6;">true</mark> , and delete the error massage ---> forward ---> turn off the foxy proxy and Burp Suite ---> We enter another person's user account or create an account with that phone number or change the password of that account.

Point 1 :
On different sites, it may be 0 and 1 instead of true and false words. Or it's better to do the correct way once to the end and pay attention to this response, and replace that answer instead of the wrong response that the browser wants to send to the server.

Point 2 :
In terms of performing steps with Burp Suite, this method is similar to the
DOR (Broken Access Control)

## 2. Rate Limit :
### Description :
In this method, the steps are similar to the previous vulnerability, that is OTP, with the difference that if the previous method didn't work, we use this method.
To find out, we can use this vulnerability or not.
We enter some random numbers to confirm the code that site send to the phone number, if the site blocks us, this method can not be used, but if the target site doesn't block our requests, we will continue this method.

### How To Do :
enter the phone number and click ok---> a 4 to 6 digit code is sent to the phone number ---> turn on the foxy proxy and Burp Suite ---> in the field related to the sent code, enter a random number, such as : 000000 ---> in Burp Suite, we right-click on the proxy section ---> send to intruder ---> click on clear ---> select 000000 and click on add ---> payload section ---> set : 1 & type : numbers & from : 000000 & to : 999999 & step : 1
---> our answer is the word that the <mark style="background: #FF5582A6;">length has more than other</mark> .
(If the site was not sensitive to consecutive tests : in option ---> request engine ---> number of threads : 50)

Point 1 :
In sites that have a time limit for entering the code, this method may not work.

Point 2 :
If our requests are blocked in this method, we have a bypass :
in proxy section in burp suite ---> We add a part named : X-Forwarded-For : 127.0.0.1
---> We select part 127.0.0.1 and try the list of different IPs so as not to be blocked by the site.
(we can use fake ip, it's doesn't matter)
(409 = It means blocking & 401 = The tested number isn't correct)

## 3. Master Password (Bypass Admin Page) : 
	
### Description :

in the login page (admin or member) ---> in the user and password box --->
typing :
- <mark style="background: #FFB86CA6;">'=''or'</mark> 
	
with these, we enter the last admin or member who entered the site.
sometimes it's necessary to observe the structure of gmail for the user :
- <mark style="background: #FFB86CA6;">'=''or'@gmail.com</mark> 
### How To Find Admin page :

1. Dork (10% to 15% Chance) :
	- site:(the name of site) inurl:admin
	- site:(the name of site) password or login

2. Pictures (5% to 10% Chance) :
	we open different photo of the site with open link in new tab and looking for unreasonable path in url that came from the admin page.

3. <mark style="background: #FF5582A6;">Dirbuster</mark> (50% Chance) :
	java must be installed before installing this tool(Dirbuster).
	with this tool, we can find the admin page, backup site and etc.
	
	example site for work with dirbuster :
	https://exam.sedayezendegi.com/
	result :
	https://exam.sedayezendegi.com/edit.php
	
4. Enumeration Directory :
	
	example 1 :
	www.ntwinvestigations.com/adminc/admin_login.php
	we ask ourselves if we delete this part of the address : admin_login.php
	will it enter the admin page or not ?!

	another way of this vulnerability is to search on google :
	site:https://www.ntwinvestigations.com/adminc
	we ask google to suggest us what words to put after adminc
	for example :
		welcome
	and with :
		www.ntwinvestigations.com/adminc/welcome.php
	we enter the admin page.

	example 2 :
	http://www.ghodsgasht.ir/portal/admin/hotel/admin.php

### Other Examples For Mater Password:

1. http://www.nlcrt.ca/login.php?type=1&id=9

2. https://www.starfishindia.com/admin/production/

3. http://www.gspodisha.org/gadmin/login

4. http://www.rhgoc.in/goc/admin.php

5. http://themes.propeller.in/bootstrap3/html/propeller-admin/login.html
