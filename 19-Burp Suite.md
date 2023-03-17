# <mark style="background: #FF5582A6;">Description :</mark> 
- خزنده ای قدرتمند برای شناسایی تمام صفحات سایت
- اسکنری قدرتمند برای شناسایی ضعف های سایت
- پیاده سازی حملات بروت فورس (حملاتی که یوزر را بدست آورده ایم و حالا میخواهیم پسورد های مختلف را امتحان کنیم تا به جواب برسیم)

# Software Preparation :
1. install <mark style="background: #FF5582A6;">FoxyProxy extension</mark> ---> options ---> add proxy --->
	proxy type : HTTP
	Proxy IP address or DNS name : 127.0.0.1
	port : 8080
	and save it
2. when working with Burp Suite, FoxyProxy should be on (127.0.0.1) and during daily use, FoxyProxy should be off.
3. turn on the FoxyProxy and search in the browser :
	- <mark style="background: #FF5582A6;">http://burp</mark> 
   click on the <mark style="background: #FF5582A6;">CA certificate</mark> and a file will be downloaded.
   then we go to the browser sitting :
   - setting ---> certificates ---> view certificates (certificate manager) --->
      authorities tab --- > import ---> select the file we downloaded ---> trust this
      CA . . . websites ---> OK
4. we do this so that Burp Suite isn't limited to <mark style="background: #FF5582A6;">http</mark> and accept : <mark style="background: #FF5582A6;">https</mark> 
# Introduction of different parts of the software :
1. proxy :
اطلاعاتی که از طریق مرورگر ثبت میشود در اینجا ثبت میشود (واسط بین من و سرور)

2. target : 
 درخواست هایی که ارسال کردیم را به صورت ریکوئست و ریسپانس میبینیم

3. action :
کلیک راست روی صفحه در قسمت پروکسی همان بخش های اکشن را نشان میدهد
 - send to repeater :
توی این بخش تغییراتی که بخواهیم توی درخواستمون ایجاد میکنیم

4. scope :
یک آدرس را میدهیم و میگوییم میخواهیم ریکوئست و ریسپانس های مربوط به این مسیر را ببینیم

5. scan :
   - crawl : خزش
   - crawl and audit :
   هم خزش انجام میدهد و هم بعد از این که دایرکتوری ها را مشخص کرد کار اسکن هم انجام بده
   - URLs to scan :
   سایت یا مسیرهای خاص یک سایت را برای اسکن میدهیم

6. live task :
   - live audit : اسکن کامل
   - live passive crawl : برسی دایرکتوری ها بدون انجام اسکن

7. comparer : مقایسه کننده بر اساس کلمه یا بایت

8. intruder : برای تست روی پارامترهای یک وبسایت

9. sequencer :
میتونیم روی پارامترهایی که به صورت رندوم تعریف میشه آنالیز داشته باشیم مثل توکنها و سیشنها

10. extender :
برپ سویت را مجهزتر میکنیم و امکانات بیشتری را اضافه میکنیم با نصب اکستنشن های مختلف
- CMS Scanner : اسکنی روی سیستم مدیریت محتوا انجام میدهد
- WAF Detect : نوع واف را شناسایی میکند

# Different methods in Burp Suite :
1. GET :
		different requests to view a page.
2. POST :
		we enter information in a form and send it to the server.
3. HEAD :
		request for page header.
4. TRACE :
		it allows the user to see the process of changing requests step by step.
5. PUT :
		it helps to send a data and save it at the same time.
6. DELETE :
		it's used to delete a page.
7. OPTION :
		we can see all the request methods of the page.

- Point :
	for the security of the website, the following request method must be closed :
	1. OPTION
	2. DELETE
	3. PUT