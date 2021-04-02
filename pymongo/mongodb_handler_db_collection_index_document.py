import pymongo
from pymongo import IndexModel

mongo = pymongo.MongoClient(host='192.168.111.133', port=27017, tz_aware=True)

def handler_db():
    """操作数据库"""
    #创建或选择数据库
    db=mongo.get_database('sxt')
    #或
    #db = mongo.sxt
    print(db)
    db.user.insert_one({"name":"zhangsan"})

    #删除数据库
    mongo.drop_database(db)   #或mongo.drop_database('sxt')

    #获取数据库名称
    print(mongo.list_database_names())

def handler_collection():
    """操作集合"""
    #获取数据库
    db=mongo.sxt

    #创建集合或选择集合
    col=db.create_collection("col")
    #或
    #col = db.col
    print('创建的集合：',col)

    #获取一个集合
    col= db.get_collection("col")
    #或
    #col=db.col
    print("获取的集合：",col)

    #获取所有集合名称
    print("获取所有集合名称：",mongo.test.list_collection_names())

    #获取所有集合对象
    print("获取所有集合对象：",mongo.test.list_collections())

    #删除集合
    print(db.drop_collection("col"))

def handler_index():
    """索引操作"""
    #获取集合
    emp = mongo.test.emp
    user = mongo.test.user
    #创建索引,默认正序 名字默认是属性
    #print(emp.create_index('name'))

    #创建索引，添加排序规则
    #print(emp.create_index([('salary',pymongo.DESCENDING)]))

    #创建多个索引
    # age_index=IndexModel([('age',pymongo.ASCENDING)],unique=True)
    # name_index=IndexModel([('name',pymongo.DESCENDING)])
    # r=user.create_indexes([age_index,name_index])
    # print(r)

    #创建混合索引
    #r= user.create_index([('age',pymongo.ASCENDING),('name',pymongo.DESCENDING)])
    #print(r)


    #删除索引
    #user.drop_indexes()

def handler_document():
    """操作文档"""
    #创建数据库及集合
    col= mongo.sxt.col
    #添加数据
    #插入单条
    user={"_id": 1, "name": "list", "age": 20}
    r=col.insert_one(user)
    print(r.acknowledged,r.inserted_id)

    #插入多条
    user1={"_id":2,"name":"wangwu","age":18}
    user2={"_id":3,"name":"zhaoliu","age":18}
    rs=col.insert_many([user1,user2])
    print(rs.acknowledged,rs.inserted_ids)

    #修改数据
    #修改单条
    # user={"name":"tianqi","age":23}
    # upt = col.update_one(filter={"name":"zhaoliu"},update={"$set":user})
    # print(upt.acknowledged,upt.matched_count,upt.modified_count,upt.raw_result,upt.upserted_id)

    #修改多条
    # user={"name":"zhaoliu","age":"20"}
    # upt=col.update_many(filter={"name":"zhaoliu666"},update={"$set":user})
    # print(upt.acknowledged,upt.matched_count,upt.modified_count,upt.raw_result,upt.upserted_id)

    #删除数据
    #删除单条
    # d=col.delete_one({"name":"wangwu"})
    # print(d)

    #删除多条
    # d=col.delete_many({"name":"zhaoliu"})
    # print(d.acknowledged,d.deleted_count)



if __name__ == '__main__':
    handler_document()
