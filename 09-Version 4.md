# <mark style="background: #FF5582A6;">Prerequisite :</mark> 
[[02-Sql Injection (Basic)]]
[[03-Sql Injection (Errors)]]
Knowing How To Work With Burp Suite 

# <mark style="background: #FF5582A6;">Description :
</mark> 
This method used when :
1. for sites that have database vesion 4
2. for sites that don't have database version 4 but in the late steps, the target site it's sensitive to the <mark style="background: #FF5582A6;">table_name</mark> or <mark style="background: #FF5582A6;">information_schema</mark> 

# How To Do :
1. instead of one of the columns we write : <mark style="background: #FF5582A6;">version ()</mark> 
   and after the number of columns we wirte one of the expressions below :
    - from admin
    - from Admin
    - from admins
    - from Admins
    - from user
    - from users
if it doesn't have these tables, it will not show us anything, but if it has these tables and the programmer has blocked it's path, it will show us <mark style="background: #FF5582A6;">forbidden</mark> .
(in version 4 sites, it's better to take <mark style="background: #FF5582A6;">version()</mark> instead of <mark style="background: #FF5582A6;">group_concat</mark> .

2. in the previous step, if it showed us the <mark style="background: #FF5582A6;">version()</mark> 
   then instead of <mark style="background: #FF5582A6;">version()</mark> we put <mark style="background: #FF5582A6;">user</mark> or <mark style="background: #FF5582A6;">username</mark> or guess other important columns to finally find the important column.
   (in the method of version 4, if we use bypass in previous step, we clear the bypass of the <mark style="background: #FF5582A6;">from</mark> )

3. if we were able to find the important column including : <mark style="background: #FF5582A6;">user or email and password</mark> in the previous step then our work is done but if we couldn't guess the important table or important column in the previous step, we get help from Burp Suite :

4. we use Burp Suite for to guess the important table as follows :

	1. in the first step, we put <mark style="background: #FF5582A6;">aaaa</mark> instead of <mark style="background: #FF5582A6;">admin</mark> and run it in Burp Suite.
	2. from the proxy section, right-click and click : <mark style="background: #FF5582A6;">send to intruder</mark> .
	3. first of all, click <mark style="background: #FF5582A6;">clear</mark> and <mark style="background: #FF5582A6;">select aaaa</mark> and click <mark style="background: #FF5582A6;">add</mark> .
	4. <mark style="background: #FF5582A6;">payload</mark> section ---> the <mark style="background: #FF5582A6;">set</mark> part should be on <mark style="background: #FF5582A6;">1</mark> and the <mark style="background: #FF5582A6;">type</mark> part should be on <mark style="background: #FF5582A6;">runtime file</mark> .
	4. we give it <mark style="background: #FF5582A6;">the list of tables</mark> we have.
	   (E: \ PEDRAM \ Web Pentest \ Tables (Burp Suite).txt) or [[17-Tables (Burp Suite)]]
	6. click <mark style="background: #FF5582A6;">START</mark> .
	7. our answer is the word that the <mark style="background: #FF5582A6;">length has more than other</mark> .
	   (7000s are errors)

 5. the method of finding the important column with the help of Burp Suite is similar to finding the important table that we said above.
    (we find the important table, we don't change it anymore)
    the step of this work are :
    
    1. in the first step, we put aaaa instead of user (for exaple for the important column) and run it in Burp Suite.
    2. from the proxy section, right-click and click : send to intruder.
    3. first of all, click clear and select aaaa and click add.
    4. payload section ---> the set part should be on 1 and the type part should be on runtime file.
    5. we give it the list of columns we have.
       (E: \ PEDRAM \ Web Pentest \ Columns (Burp Suite).txt) or [[18-Columns (Burp Suite)]]
    6. click START.
    7. our answer is the word that the length has more than other.
	   (7000s are errors)

