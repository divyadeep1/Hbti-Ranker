import urllib
import re
import sqlite3

#base url
baseUrl = "http://hbti.ac.in/coe/results/odd_2016/reg16btall.asp?rollno=15045"
branchIDs = ['10', '13', '51', '00', '20', '30', '40', '84', '85', '87', '82', '55', '86']
marks = ctr = 00
branch = name = html = ''
conn = sqlite3.connect('Ranker.sqlite')
cur = conn.cursor()
#cur.execute('''DROP TABLE IF EXISTS RankList''')
cur.execute("""CREATE TABLE IF NOT EXISTS RankList(Name TEXT, Branch TEXT, Marks INTEGER)""")
for id in branchIDs:
	print ("Calculating for branch with ID %s"%id)
	ctr = 0
	for roll in range(1, 60):
		if ctr==4:
			break
		else:
			if roll<10:
				html = urllib.urlopen(baseUrl+id+'00'+str(roll)).read()
			else:
				html = urllib.urlopen(baseUrl+id+'0'+str(roll)).read()
			if('Roll Number not found in database.' not in html):
				marks = int(re.findall('Marks:&nbsp;</strong>(.*)/2000', html)[0].strip())
				print marks
				name = re.findall('<td width="50%">(.*)</td>', html)[1]
				print name
				branch = re.findall('<td>B. Tech. (.*)</td>', html)[0]
				print branch
				ctr = 0
			else:
				ctr = ctr+1
				continue
		cur.execute('''SELECT Marks FROM RankList WHERE Name = ?''', (name, ))
		if(cur.fetchone() is None):
			cur.execute('''INSERT INTO RankList(Name, Branch, Marks) VALUES (?, ?, ?)''', (name, branch, marks))
		else:
			continue
	conn.commit()
cur.close()