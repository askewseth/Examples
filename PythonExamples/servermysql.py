import mysql.connector


cnx = mysql.connector.connect(user='root',
                              password='Bluesun7',
                              host='159.203.129.213',
                              database='astro'
                              )

print 'DONE!'

cnx.close()
