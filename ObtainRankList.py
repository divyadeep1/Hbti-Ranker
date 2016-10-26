import sqlite3
conn = sqlite3.connect('Ranker.sqlite')
cur = conn.cursor()
sqlStr = 'SELECT Name, Branch, Marks FROM RankList ORDER BY Marks DESC LIMIT {}'.format((int(raw_input("How many top rankers do you wish to see?"))))
print type(sqlStr), sqlStr
print "Rank List:-"
print "Rank\t\tName\t\tBranch\t\tPercentage"
rank=1
for i in cur.execute(sqlStr):
	print ("%d\t\t%s\t\t%s\t\t%s"%(rank, i[0], i[1], str(i[2]/20.0)))
	rank=rank+1
	