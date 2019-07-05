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

with open('/home/josep/Downloads/gtfs/stop_times.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
            count_lines += 1
            row = list(row)
            print("This is row number: %d for %s \r" % (count_lines,row))
            data = (row)
            mysql_query = ('INSERT INTO 00_P2_stop_times(trip_id,arrival_time,departure_time,stop_id,stop_sequence)' 'VALUES(%s, %s, %s, %s, %s)')
            cursor.execute(mysql_query, data)


#close the connection to the database.

cursor.close()
print("Done")
