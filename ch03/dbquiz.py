from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.saoh

movie_star = db.movies.find_one({'title':'매트릭스'})
print(movie_star['star'])

movie_title = list(db.movies.find({'star':movie_star['star']}))

for m in movie_title:
    print(m['title'])

db.movies.update_one({'title':'매트릭스'},{'$set':{'star':'0'}})
