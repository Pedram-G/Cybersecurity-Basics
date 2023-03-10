# Description :
- it's related to uploaders.
- uploader algorithms :
	1. extention :
	   - whithe list : .jpg .png .jpeg
	   - black list : .php .asp .aspx .exe .msi
	2. MIME type : image/jpeg image/jpg image/*
	3. size limit : 100 kb
	4. file proccess
- anywhere on the target site that has an uploader, this vulnerability may exist.
- shell uploading is possible in a form uploader or a profile photo uploader or an uploader inside the admin panel [[2-Sql Injection (Basic)]].
- in uploader, we upload shell to get high level access from the target site.
- download different shells from : https://r57.gen.tr
- for upload the shell, we try all the paths of the site that have uploaders.
- To run our shells, after it has been successfully uploaded in the target site, We click on edit in the site uploader and open our shell file in a separate browser tab.

# Points :
1. if only image type (jpeg) were allowed to upload or the uploader had format restrictions :
	- changing the browser request that is send to the server (with Burp Suite) :
	   Turn on the Burp Suite ---> Proxy part ---> We change the content-type from application to the image/jpeg and click forward.
	   (Changing the file-name instead of content-type has no effect).
	   
2. If we can't do it with Burp Suite :
   we rename the shell file format as follows :
   - .Php
   - .phP
   - .pHp
   - .php3
   - .php4
   - .php5
   - .php7
   - .phps
   - .phtml
   - .phpt
   - .pgif
   - .phar
   - .php/
   - .php%0a
   - .php%00.jpg
   - .php<mark style="background: #FF5582A6;">\x</mark> 00.jpg
   - (This doesn't work on all servers)

3. The shell may be uploaded correctly in the uploader but not executed : 
	- The server may have antishell and Know some shells Or It may be due to the size of the shell file:
					so we will try several different shell to solve these problems.

