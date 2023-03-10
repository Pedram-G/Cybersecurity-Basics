# <mark style="background: #FF5582A6;">Prerequisite :</mark> 
[[02-Sql Injection (Basic)]]
[[03-Sql Injection (Errors)]]
# <mark style="background: #FF5582A6;">Description :</mark> 
we use this method when the desired page doesn't show us the column numbers
(even with a - behind the ?id number).

# How To Do :
on the desired page :
1. <mark style="background: #FFB86CA6;">Ctrl + u</mark> 
2. put <mark style="background: #FFB86CA6;">view-source:</mark> before the URL of the site
3. Right Click and View Page Source

for to easily find the column numbers in source :
- union select 1111,2222,3333,4444,5555,6666,7777,8888,9999--
- Ctrl + f ---> search 1111 to 9999 for find the column numbers
- when we find, the continuation of the steps is similar to before :
  [[02-Sql Injection (Basic)]]
  