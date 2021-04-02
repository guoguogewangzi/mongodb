import pymongo


def mongodb_init01():                 #方法一
    """连接数据库"""
    mongo = pymongo.MongoClient(host='192.168.111.133', port=27017, tz_aware=True)
    rows=mongo.test.user.find()
    for r in rows:
        print(r)


def mongodb_init02():                #方法二
    """连接数据库"""
    uri = "mongodb://{}:{}".format('192.168.111.133',27017)
    mongo = pymongo.MongoClient(uri,tz_aware=True)
    rows = mongo.test.user.find()
    for r in rows:
        print(r)


if __name__ == '__main__':
    mongodb_init02()
