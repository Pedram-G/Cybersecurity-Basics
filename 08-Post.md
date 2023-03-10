# <mark style="background: #FF5582A6;">Prerequisite :</mark>
[[02-Sql Injection (Basic)]]
[[03-Sql Injection (Errors)]]
Knowing How To Work With Burp Suite 

# Description :
- This method is used for sites that don't have numerical parameters such as (?id=1), or don't have a parameter equal to a thing in the URL.

# How To Do :
1. We are looking for forms on the Target siteو Search form or new member registration form (join us) or any other form in the site.

2. Turn on Burp Suite and look for the parameter in the proxy section of Burp Suite, we go to the repeater section and we use those parameters to find out the target site has [[02-Sql Injection (Basic)]] vulnerability or not.

3. The steps are exactly the same as the [[02-Sql Injection (Basic)]] steps and it starts with the quotation <mark style="background: #FF5582A6;">( ' )</mark> .

4. By entering each step of the command code, we look for errors and changes in the site in the response section, This section displays the codes of the site.
    Of course, to see better, that is the appearance of the site, we pay attention to the render part (for example, to see the column numbers on the target site in union select step).

# Example :

https://www.shivsenapunjab.com/join-us

(phone)

https://exam.sedayezendegi.com/login.php

(username)