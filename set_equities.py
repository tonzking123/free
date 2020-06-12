import requests
from bs4 import BeautifulSoup
import mysql.connector



url = "https://marketdata.set.or.th/mkt/investortype.do?language=en&country=US"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
mydivs = soup.find("table", {"class": "table table-info"})
tds = soup.findAll("td")

#print(len(tds))
"""0 = Local Institutions 1=buy 2=buy% 3=sell 4=sell% 5=net 6=empty
   7 = Proprietary Trading 8=buy 9=buy% 10=sell 11=sell% 12=net 13=empty
   14 = Foreign Investors 15=buy 16=buy% 17=sell 18=sell% 19=net 20=empty
   21 = Local Individuals 22=buy 23=buy% 24=sell 25=sell% 26=net 27=empty
"""

tds_list = []
for td in tds:
    tds_list.append(td.text)
    
var_list = []
for var in tds_list:
    var = var.strip()
    var = var.replace(',',"")
    var_list.append(var)

#print(var_list)

#print(var_list)

#print(type(int(tds[1].text)))

mydb = mysql.connector.connect(
  host="t-mysql-01.torch-ex.com",
  user=".....",
  password=".....",
  database='.....'
)
mycursor = mydb.cursor()
sql = "INSERT INTO local_institutions (buy, buy_perc,sell,sell_perc,net) VALUES (%s, %s, %s, %s, %s)"
val = (float(var_list[1]),float(var_list[2]),float(var_list[3]),float(var_list[4]),float(var_list[5]))
mycursor.execute(sql, val)

sql = "INSERT INTO Proprietary_trading (buy, buy_perc,sell,sell_perc,net) VALUES (%s, %s, %s, %s, %s)"
val = (float(var_list[8]),float(var_list[9]),float(var_list[10]),float(var_list[11]),float(var_list[12]))
mycursor.execute(sql,val)
mydb.commit()

sql = "INSERT INTO Foreign_Investors (buy, buy_perc,sell,sell_perc,net) VALUES (%s, %s, %s, %s, %s)"
val = (float(var_list[15]),float(var_list[16]),float(var_list[17]),float(var_list[18]),float(var_list[19]))
mycursor.execute(sql,val)
mydb.commit()

sql = "INSERT INTO Local_Individuals (buy, buy_perc,sell,sell_perc,net) VALUES (%s, %s, %s, %s, %s)"
val = (float(var_list[22]),float(var_list[23]),float(var_list[24]),float(var_list[25]),float(var_list[26]))
mycursor.execute(sql,val)

mydb.commit()

#
#for div in mydivs:
    
    
