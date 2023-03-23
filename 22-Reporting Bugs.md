# Hacking Steps :
1. Recon
2. Exploit
3. Reports

# The Main Sections Of Each Report :
1. <mark style="background: #FFB86CA6;">Title :</mark> 
	- in-scope :
		the name of the bug + vulnerable function + impact
		
	- out-of-scope :
		the name of the bug {out-of-scope} + second bug + vulnerable function + impact
	
	- <mark style="background: #FF5582A6;">Point :</mark> 
	    in-scope and out-of-scope :
	    the dos and don'ts of acceptable bugs we have found.
		
2. <mark style="background: #FFB86CA6;">Summary :</mark> 
	- explanation about our work and what important information, i have gained with the bug i found (in a paragraph)

	- Example :
			site.com is vulnerable to reflected XSS via the q parameter

3. <mark style="background: #FFB86CA6;">POC (Proof of concept) :</mark> 
	- we explain all the exploiting steps in order
	- env + <mark style="background: #FF5582A6;">steps</mark> + screenshot or video
	- env : if there are any prerequisites before exploiting or special conditions (env isn't necessary to write it in the report)

4. <mark style="background: #FFB86CA6;">Impact :</mark> 
	- what can a hacker do with this vulnerability?
	- what information does the hacker get access to with this vulnerability?
	- what effect does this vulnerability have on other site users?

	- <mark style="background: #FF5582A6;">Point 1 :</mark> 
	    Known vulnerabilities such as [[2-Sql Injection (Basic)]], don't need impact.

	- <mark style="background: #FF5582A6;">Point 2 :</mark> 
		in this section, we should not write the definition of the bug.

# Examples for title :
- Account Takeover with IDOR vulnerability on site.com
- sql injection in the 'article.php' on the site.com
- User Enumeration + Authentication Flaws on site.com
- Self-XSS chained IDOR in login page on the site.com

# Real Examples for title:
- [site.com] SQL Injection Time Based On /js/commentAction/
- Bypass Password Authentication to Update the Password
- Server-Side Request Forgery using Javascript allows to exfill data from Google Metadata
- Being able to change account contents even after password change
- Login Page vulnerable to bruteforce via rate limiting bypass

# Answers after sending a bug report :
1. Triaged :
	- the report is flawless and accepted ---> Resolved ---> Bounty

2. Need more info :
	- more information needs to be sent ---> Triaged

3. informative :
	- a good impact isn't written or the vulnerability doesn't grant high-level access and the level of vulnerability is considered low or the steps taken are complexly written and the security team couldn't complete the process ---> more information needs to be sent ---> Triaged

4. Not Applicable :
	- a higher level of access should be found or the domain being worked is out-of-scope or the vulnerability is low level and needs to be combined with another vulnerability ---> another vulnerability needs to be found.

5. Duplicate :
	- The vulnerability we sent is accepted but someone reported it earlier ---> another vulnerability needs to be found.