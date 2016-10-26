import urllib
import re
import sqlite3

#base url
baseUrl = "http://hbti.ac.in/coe/results/odd_2016/reg16btall.asp?rollno=15045"
branchIDs = ['10', '13', '51', '00', '20', '30', '40', '84', '85', '87', '82', '55', '86']
marks=00
html=''
marks=00
branch = name = ''
conn = sqlite3.connect('Ranker.sqlite')
cur = conn.cursor()
cur.execute("""CREATE TABLE RankList(Name TEXT, Branch TEXT, Marks INTEGER)""")
for id in branchIDs:
	for roll in range(1, 60):
		if ctr==4:
			break
		else:
			if roll<10:
				html = urllib.open(baseUrl+id+'00'+roll).read()
			else:
				html = urllib.urlopen(baseUrl+id+'0'+roll).read()
			if('Roll Number not found in database.' not in html):
				marks = int(re.findall('Marks:&nbsp;</strong>(.*)/2000', html)[0].strip())
				name = re.findall('<td width="50%">(.*)</td>', html)[1]
				branch = re.findall('<td><b>Course/Branch:</b></td>\n<td>(.*)</td>', html)
				ctr = 0
			else:
				ctr = ctr+1
				continue
		cur.execute('''SELECT Marks FROM RankList WHERE Name = ?''', (name, ))
		if(cur.fetchone() is None):
			cur.execute('''INSERT INTO RankList(Name, Branch, Marks) VALUES (?, ?, ?)''', (name, branch, marks))
		else:
			continue
	cur.commit()
cur.close()