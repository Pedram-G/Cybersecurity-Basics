# <mark style="background: #FF5582A6;">Prerequisite :</mark> 
[[2-Sql Injection (Basic)]]
[[3-Sql Injection (Errors)]]
# <mark style="background: #FF5582A6;">Description :</mark> 
This method used when :
1. for sites that don't find the important table
2. for sites that have many important tables and we don't know which one to choose
3. for a site that has many databases

# How To Do :
we make changes in the sql [[2-Sql Injection (Basic)]] codes and our new code will be as follow :
1. previous command :
	- <mark style="background: #FFB86CA6;">from information_schema.tables where table_schema=database()--</mark> 
2. new command :
	- <mark style="background: #FFB86CA6;">from information_schema.<mark style="background: #FF5582A6;">columns</mark> where <mark style="background: #FF5582A6;">column_name like</mark> <mark style="background: #FF5582A6;">'%pas%'</mark> --</mark> 

## Point :
1. %pas% means find everything before and after pas, like :
   - pass
   - paswd
   - passwd
   - password

2. the command we typed, searches all the databases and show us the tables that have similar to pas.

3. when we found the important table, we follow the same step as in the past in
   [[2-Sql Injection (Basic)]], with the difference that <mark style="background: #FF5582A6;">like</mark> remain instead of <mark style="background: #FF5582A6;">=</mark> .

4. if we type in the last step :
	- from the important table
   and it didn't show us anything, we write the name of database before the important table :
		 the name of database<mark style="background: #FF5582A6;">.</mark> the important table

5. %pas% must be hexed because the target site is likely to be sensitive to it.
it's hex is :
- <mark style="background: #FFB86CA6;">0x2570617325</mark> 

6. if we use : %user% instead of : %pas% and if it show us these two tables :
	- PROFILING
	- USER_STATISTICS
   we consider them among the default tables.

## <mark style="background: #FF5582A6;">Point :</mark> 
the [[6-Limit (Method)]] and like method can be combined together.
in this way, the <mark style="background: #FF5582A6;">limit 0,1</mark> comes after <mark style="background: #FF5582A6;">like %pas%</mark> (<mark style="background: #FF5582A6;">limit 0,1</mark> comes instead of <mark style="background: #FF5582A6;">group_concat</mark> )
so this combined method is suitable for a site that is sensitive to <mark style="background: #FF5582A6;">group_concat</mark> and has many tables.