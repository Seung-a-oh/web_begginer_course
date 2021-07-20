from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# 코딩 시작
#insert/find/update/delete

#insert
# doc = {'name':'seunga','age':22}
# db.users.insert_one(doc)

#find
# same_ages = list(db.users.find({'age':21},{'_id':False}))
# for person in same_ages:
#     print(same_ages)

#find one
# user = db.users.find_one({'name': 'bobby'}, {'_id:False'})
# print(user)

#update_one
# db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

#update_one
db.users.delete_one({'name':'bobby'})