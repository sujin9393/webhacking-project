import pymysql



con = pymysql.connect(
    user = 'uroot',
    passwd = '',
    host = '127.0.0.1',
    db = 'opentutorials',
    charset = 'utf8'
)

# cur = con.cursor()
# sql_query = "SELECT * FROM topic"
# cursor.execute(sql_query)

# result = cursur.fetchall()

# for row in result:
#     print(row)


# cursor.close()
# conn.close()
