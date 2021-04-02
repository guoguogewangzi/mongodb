import pymongo

mongo = pymongo.MongoClient(host='192.168.111.133', port=27017, tz_aware=True)

'''
    必须是连接通过方法获取数据库
    数据库通过方法获取集合
    敲代码就会有提示功能
'''

# 获取集合
db = mongo.get_database('test')
emp = db.get_collection('emp')
user = db.get_collection('user')


def show(r):
    "展示所有文档"
    for i in r:
        print(i)


def test_and():  # 不需要改
    """and操作"""
    r = db.user.find({
        "$and": [
            {"_id": {"$gte": 3, "$lte": 4}},
            {"age": {"$gte": 10}}

        ]
    })
    show(r)


def test_or():  # 不需要改

    r = db.user.find({
        '$or': [
            {"_id": {'$gte': 0, '$lte': 1}},
            {"_id": {'$lte': 4}},
            {"name": "xuyihang"}
        ]
    })
    show(r)


def test_regex():  # 需要改
    """正则操作"""
    r = db.user.find({
        "name": {"$regex": "^z.*?(n|i)$"}
    })
    show(r)


def test_project():  # 不需要改
    """投影"""
    r = db.user.find(
        {"name": "lihua"},
        {"_id": 0, "name": 1, "age": 1}
    )
    show(r)


def test_array():  # 不需要改
    """数组操作"""

    r = db.user.find({},
                     {
                         "_id": 0,
                         "name": 0,
                         "age": 0,
                         "addr": 0,
                         "hobbies": {'$slice': [0, 2]}
                     })
    show(r)


def test_sort():  # 需要改
    """排序操作"""
    '''
        2）查询结果name倒序排序
        db.user.find().sort({"name":-1})
        
        3）查询结果按年龄倒序排序，然后再按id倒序排序（相同年龄的）
        db.user.find().sort({"age":-1,"_id":-1})
    '''
    r = db.user.find({}, {"name": -1}).sort("name", pymongo.DESCENDING)
    show(r)
    r = user.find({}, {"age": -1, "_id": 1}).sort([("age", pymongo.DESCENDING), ("_id", pymongo.ASCENDING)])
    show(r)


def test_page(pageNum, pageSize):  # 不需要改
    """分页"""
    '''
        1）显示前两个
        db.user.find().limit(2)
        2）跳过前2个显示后续的2个
        db.user.find().limit(2).skip(2) 或 db.user.find().skip(2).limit(2)
        3）分页公式：
        db.user.find().skip((pageNum-1)*pageSize).limit(pageSize)
    '''
    r = db.user.find().limit(2)
    show(r)
    r = db.user.find().limit(2).skip(2)
    show(r)
    r = db.user.find().skip((pageNum - 1) * pageSize).limit(pageSize)
    show(r)


def test_group():  # 不需要改
    """分组查询"""
    r = db.emp.aggregate([{
        "$match": {"post": "公务员"}
    }])
    show(r)

    r = db.emp.aggregate([
        {'$match': {"_id": {'$gt': 3}}},
        {'$group': {"_id": "$post", "avg_sal": {"$avg": "$salary"}}}
    ])
    show(r)

def test_project02():  #不需要改
    """投影"""
    r = db.emp.aggregate([
        {
    '$project': {
        "name": 1,
        "post": 1,
        "new_age": {"$add": ["$age", 1]}
    }
    }
    ])
    show(r)

def test_sort_limit_skip():    #不需要改
        """排序限制过滤"""
        r = db.emp.aggregate([
            {'$group': {"_id": "$post", "avg_salary": {"$avg": "$salary"}}},
        {'$sort': {"avg_salary": 1}},
        {'$limit': 2}
        ])
        show(r)

        r = db.emp.aggregate([
        {'$group': {"_id": "$post", "avg_salary": {"$avg": "$salary"}}},
        {'$sort': {"avg_salary": 1}},
        {'$skip': 1}
        ])
        show(r)

def test_sample():   #不需要改
        """随机获取"""
        #14）$sample：随机取3个
        r = db.emp.aggregate([
            {'$sample': {'size': 3}}
        ])
        show(r)


def test_str():   #不需要改
    """操作字符串"""
    #15）$substr: 截取sex[0:2]字符串
    r = db.emp.aggregate([
        {
    '$project': {
        "_id": 0,
        "str": {"$substr": ["$sex", 0, 2]}
    }
    }
    ])
    show(r)

   # 16）$concat: 拼接字符串
    r = db.emp.aggregate([
        {'$project': {
        "_id": 0,
        "str": {"$concat": ["$name", "测试", "$sex"]}
    }}
    ])
    show(r)

   # 17）$toUpper: 转成大写
    r = db.emp.aggregate([
        {
    '$project': {
        "sex": {'$toUpper': "$sex"}
    }
    }
    ])
    show(r)

   # 18）$toLower: 转成小写
    r = db.emp.aggregate([
        {
    '$project': {
        "sex": {'$toLower': "$sex"}
    }
    }
    ])
    show(r)


if __name__ == '__main__':
    test_str()