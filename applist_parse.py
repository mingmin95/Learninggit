import pymysql


if __name__ == '__main__':

    db = pymysql.Connect(host="127.0.0.1",port=3306,user='root',passwd='root123',db='fingerprinting',charset='utf8')
    cur = db.cursor()
    sql = "select deviceudid,app_list from device_applysubmit where breakflag='是'"
    cur.execute(sql)
    data = cur.fetchall()
    print
    insertlist = []
    for applist in data:
        print(applist[0])
        device= eval(applist[1])
        deviceudid =  applist[0]
        for app in device:
            timestamp = app['timestamp']
            version = app['version']
            app_name = app['app_name']
            package_name = app['package_name']
            insertlist.append((deviceudid, timestamp, version, app_name, package_name))

    sql = "insert into applist(deviceudid,timestamp,version,app_name,package_name) values(%s,%s,%s,%s,%s)"
    cur.executemany(sql, insertlist)
    db.commit()
    cur.close()
    db.close()