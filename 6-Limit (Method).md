# <mark style="background: #FF5582A6;">Prerequisite :</mark> 
[[2-Sql Injection (Basic)]]
[[3-Sql Injection (Errors)]]
# <mark style="background: #FF5582A6;">Description :</mark> 
limit is used in two cases : 
1. the target site is sensitive to the group_concat.
2. a site that is limited in printing characters.

Limit is an important method and it's also used in :
- [[12-Xpath Injection]]
- [[13-Double Query]]
- [[15-Blind Sql Injection]]
# How To Do :

When we delete the <mark style="background: #FF5582A6;">group_concat()</mark> , after the <mark style="background: #FF5582A6;">database()</mark> with a space, we write :
<mark style="background: #FFB86CA6;">limit 0,1--</mark> 

for example :
- <mark style="background: #FFB86CA6;">union select 1,2,3,4,5,table_name,7,8,9 from information_schema.tables where table_schema=database() limit 0,1--</mark> 
in this way, this code it show us the first table.
to see the rest of the tables :
we add the first number of the limit :
- limit 1,1
- limit 2,1
- limit 3,1
- limit 4,1
 until the display of the last table.
 the rest of the steps are the same as before, but we keep the limit at the end of our code.

## <mark style="background: #FF5582A6;">Make this method easier :</mark> 
- HackBar Quantum ---> Load ---> each time, we increase the limit number ---> Ok