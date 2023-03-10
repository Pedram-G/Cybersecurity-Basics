# Types and Descriptions :
1. Directory Traversal (file traversal, path traversal) :
	- when we have a parameter that doesn't have correct validation, it's possible to use it and call and read different files.
	- when we click on one of the photos on the target site, and in the URL, on the file port, a path be called like : <mark style="background: #FF5582A6;">?file=./pictures/1.jpg</mark> 
	   because the calling operation has happened, the target site may have this vulnerability.
	- take the address of the photo to Burp Suite and run it.
	- we will send it to the repeater
	- do we have access to files that we shouldn't be able to read or not ?!
		for example : <mark style="background: #FF5582A6;">?file=/etc/passwd</mark> 
	- if nothing comes for show us, we go one way back with (<mark style="background: #FF5582A6;">..</mark> ) :
		<mark style="background: #FF5582A6;">file=../etc/passwd</mark> 
	- if it still doesn't show us anything again, we go one way back with (..) :
		<mark style="background: #FF5582A6;">file=../../etc/passwd</mark> 
	- so by reversing the path, we can access the password file(maybe).

	## Point 1 :
	the above work hass different modes that may take a long time, but with the following tool called : <mark style="background: #FF5582A6;">dotdotpwn</mark> 
	our work becomes much easier for this vulnerability.

	## point 2 :
	work with dotdotpwn :
	- before install <mark style="background: #FF5582A6;">dotdotpwn</mark> , <mark style="background: #FF5582A6;">perl</mark> must be installed on the system.
	- the target site :
		http://testphp.vulnweb.com
	- vulnerability path :
		http://testphp.vulnweb.com/showimage.php?file=./pictures/1.jpg
	- command code :
		<mark style="background: #FFB86CA6;">dotdotpwn.pl -m http-url -h site address -u vulnerability path -k "root" -q</mark> 
		
		for example :
		dotdotpwn.pl -m http-url -h http://testphp.vulnweb.com -u http://testphp.vulnweb.com/showimage.php?file=TRAVERSAL -k "root" -q

		this tool performs various test in a part of the following path :
		<mark style="background: #FF5582A6;">./pictures/1.jpg</mark> 
		so in the command code instead of this section, we write :
		<mark style="background: #FF5582A6;">TRAVERSAL</mark> 

		if in front of -m, we write only http, then it's necessary in front of -h we write IP of the site but if in front of -m, we write http-url, in front of -h we write only the site address.

		-q at the end causes only the result to be shown not the whole process.

		this vulnerability isn't specific to PHP and all sites may have it.

2. Lfi (local file inclusion)
	- it's exactly the same as the Directory Traversal, with the difference that, it's specific to PHP, and the other difference is that we can also read the PHP file.
	- the steps of this vulnerability are exactly similar to the Directory Traversal, with the difference that, in front of the ?file we write login.php, which will call the content of the PHP file.

3. Rfi (remote file inclusion) :
	- the difference between this vulnerability and the two previous vulnerability is that  instead of calling a file, we instruct it to read and exexute a file (online) from somewhere.
	  for example :
	  if we click on the news section on a site and the site address is displayed in the url, and at the end, that part is called : page=news.php
	  
	  for <mark style="background: #FF5582A6;">Lfi</mark> we do this, at the end of the URL :
	  <mark style="background: #FF5582A6;">?page=config.php</mark> 
	  if we encounter an error, we will go one way back with (..) and if we still don't get the result, we will repeat this work until if the site has this vulnerability, we reach the user and password :
	  <mark style="background: #FF5582A6;">?page=../config.php</mark> 
	  <mark style="background: #FF5582A6;">?page=../../config.php</mark> 

	  for <mark style="background: #FF5582A6;">Rfi</mark> we do this :
	  ?page=D:/1234.txt
	  (D:/1234.txt is a shell to eg)
	  (a shell gives us access to the entire ost of that site, this access is higher than the admin panel)

	  this shell file must be on another online site (our own site where we put the shell in the form of text or the site we hacked and put the shell there) so that we can upload it to the target site.

	  in this method, we don't upload the shell to the target site (Rfu), but we call the shell from somewhere else (online).

4. IDOR (insecure direct object refrence) 

5. Parameter Tampering 
