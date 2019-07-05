import csv
import MySQLdb

'''
mydb = MySQLdb.connect(host='az1-ss5.a2hosting.com',
    user='virdishc_12345',
    passwd='12345',
    db='virdishc_Ironhack',
    autocommit=True)
'''

mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='74463IL478obmuJ459',
    db='virdishc_Ironhack',
    autocommit=True)

cursor = mydb.cursor()
count_lines = 0

with open('/home/josep/Downloads/gtfs/trips.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
            count_lines += 1
            row = list(row)
            print("This is row number: %d for %s \r" % (count_lines,row))
            data = (row)
            mysql_query = ('INSERT INTO 00_P2_trips(route_id,service_id,trip_id,trip_headsign,direction_id,shape_id,wheelchair_accessible)' 'VALUES(%s, %s, %s, %s, %s,%s, %s)')
            cursor.execute(mysql_query, data)


#close the connection to the database.

cursor.close()
print("Done")
