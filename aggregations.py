from pymongo import MongoClient
from pprint import pprint

client = MongoClient("mongodb://localhost:27017")
db = client["PracticeDB"]

departments = db["departments"]
employees = db["employees"]

# a = collection.aggregate([
#     {"$match": {"center_id": {"$eq": 11}}},{"$count": "totalrows"},])

# b = collection.aggregate([
#     {
#         "$match": {"center_id": {"$gt": 20, "$lt": 100}}
#     },
#     {
#         "$group": {
#             "_id": "$center_id", "Number_of_orders": {
#                 "$avg": "$num_orders"
#             }}}
#
# ])
#
# for i in b:
#     pprint(i)

# c = collection.aggregate([{"$group": {"_id": "$center_id", "Number_of_orders": {"$avg": "$num_orders"}}}])
# pprint(list(c))


new_dict = [{"author": "dave", "score": [80, 90, 100], "views": 100},
            {"author": "dave", "score": [85, 40, 80], "views": 521},
            {"author": "ahn", "score": [60, 94, 91], "views": 1000},
            {"author": "li", "score": [55, 49, 100], "views": 5000},
            {"author": "annT", "score": [60, 78, 98], "views": 50},
            {"author": "li", "score": [94, 78, 59], "views": 999},
            {"author": "ty", "score": [95, 80, 65], "views": 1000}]

# a = collection.insert_many(new_dict)
# for i in new_dict:
# print(i)

# b = collection.aggregate([{"$match": {"author": "dave"}}])
# pprint(list(b))


# c = collection.aggregate([{"$match": {"$or": [{"score": {"$gt": 70, "$lt": 90}}, {"views": {"$gte": 1000}}]}},
#                           {"$group": {"_id": "$author", "count": {"$sum": 1}}}])
# pprint(list(c))

# d = collection.aggregate([{"$addFields": {"total_score": {"$sum": "$score"}}},
#                           {"$addFields": {"score_and_views": {"$sum": ["$total_score", "$views"]}}},
#                           {"$addFields": {"quality": "1080p"}},
#                           {"$addFields": {"score": {"$concatArrays": ["$score", [95]]}}}])
# pprint((list(d)))


# print(list(e))
# f = collection.find_one({"quality": "1080p"}, {"_id": 0})


dict1 = [
    {
        "_id": 1,
        "name": "Alice",
        "department": "HR",
        "salary": 50000,
        "age": 30
    },
    {
        "_id": 2,
        "name": "Bob",
        "department": "IT",
        "salary": 60000,
        "age": 28
    },
    {
        "_id": 3,
        "name": "Charlie",
        "department": "IT",
        "salary": 55000,
        "age": 35
    },
    {
        "_id": 4,
        "name": "David",
        "department": "HR",
        "salary": 52000,
        "age": 32
    }
]

# one = collection.insert_many(dict1)
# a = collection.aggregate([{"$group": {"_id": "salary",
#                                       "average_salary": {"$avg": "$salary"}}}])
# pprint(list(a))

# c = collection.aggregate([{"$sort": {"age": -1}},
#                           {"$limit": 1},
#                           {"$project": {"name": 1, "age": 1, "department": 1, "_id": 0}}])
# pprint(list(c))
# d = collection.aggregate([{"$group": {"_id": "$department", "count": {"$sum": 1}}}])
# pprint(list(d))

# e = collection.aggregate([{"$match": {"department": "IT"}},
#                           {"$project": {"name": 1, "_id": 0}}])

# {"case": {"$and": [{"$gte": ["$salary", 50000]}, {"$lt": ["$salary", 60000]}]}, "then": "50k-60k"},

# f = collection.aggregate([{"$group": {"_id":
#     {"$switch":
#         {"branches": [
#             {"case": {"$and": [{"$gte": ["$salary", 50000]}, {"$lt": ["$salary", 60000]}]},
#              "then": "50_to_60"},
#             {"case": {"$and": [{"$gte": ["$salary", 60000]}, {"$lt": ["$salary", 70000]}]},
#              "then": "60_to_70"},
#             {"case": {"$gte": ["$salary", 70000]}, "then": "exceeding_70K"}
#         ],
#             "default": "Below_50k"
#         },
#         "count": {"$sum": 1}}}
# }
# ])
# pprint(list(e))

# pipeline = [
#     {
#         "$group": {
#             "_id": {
#                 "$switch": {
#                     "branches": [
#                         {"case": {"$and": [{"$gte": ["$salary", 50000]}, {"$lt": ["$salary", 60000]}]},
#                          "then": "50_to_60"},
#                         {"case": {"$and": [{"$gte": ["$salary", 60000]}, {"$lt": ["$salary", 70000]}]},
#                          "then": "60_to_70"},
#                         {"case": {"$gte": ["$salary", 70000]}, "then": "exceeding_70K"}
#                     ],
#                     "default": "Below_50k"
#                 }
#             },
#             "count": {"$sum": 1}
#         }
#     }
# ]
#
# result = list(collection.aggregate(pipeline))
# print(result)


# dict2 = [
#     {
#         "_id": 1,
#         "title": "The Great Gatsby",
#         "author": "F. Scott Fitzgerald",
#         "rating": 4.5,
#         "num_reviews": 100
#     },
#     {
#         "_id": 2,
#         "title": "To Kill a Mockingbird",
#         "author": "Harper Lee",
#         "rating": 4.8,
#         "num_reviews": 80
#     },
#     {
#         "_id": 3,
#         "title": "Pride and Prejudice",
#         "author": "Jane Austen",
#         "rating": 4.7,
#         "num_reviews": 120
#     },
#     {
#         "_id": 4,
#         "title": "1984",
#         "author": "George Orwell",
#         "rating": 4.3,
#         "num_reviews": 60
#     }
# ]

# collection.insert_many(dict2)

# ba = collection.aggregate([{"$group": {
#     "_id": {
#         "$cond": {
#             "if": {"$gte": ["$rating", 4.7]},
#             "then": "HighlyRated",
#             "else": {
#                 "$cond": {"if": {"gte": ["$rating", 4.0]},
#                           "then": "ModeratelyRated",
#                           "else": "Lowly Rated"
#                           }}}}, "count": {"$sum": 1}}}])
#
# pprint(list(ba))

# collection.insert_many([
#   {
#     "_id": 1,
#     "title": "Inception",
#     "genre": "Action",
#     "year": 2010,
#     "ratings": [8.8, 9.2, 8.9]
#   },
#   {
#     "_id": 2,
#     "title": "The Shawshank Redemption",
#     "genre": "Drama",
#     "year": 1994,
#     "ratings": [9.3, 9.5, 9.1]
#   },
#   {
#     "_id": 3,
#     "title": "The Dark Knight",
#     "genre": "Action",
#     "year": 2008,
#     "ratings": [9.0, 8.7, 8.9]
#   },
#   {
#     "_id": 4,
#     "title": "Pulp Fiction",
#     "genre": "Crime",
#     "year": 1994,
#     "ratings": [8.9, 9.1, 8.8]
#   }
# ])

# nq = collection.aggregate([{"$addFields": {"average_ratings": {"$avg": "$ratings"}}},
#                            {"$project": {"title": 1, "year": 1, "average_ratings": 1, "_id": 0}},
#                            {"$out": "Average_ratings"}])
# print(list(nq))

#
# dict3 = {
#     "_id": 1,
#     "order_id": "ORD-001",
#     "customer_id": 101,
#     "total_amount": 150.99
# }
#
# # collection.insert_one(dict3)
#
# dict4 = {
#     "_id": 101,
#     "name": "John Doe",
#     "email": "john.doe@example.com",
#     "address": "123 Main St, City"
# }
#
# # collection2.insert_one(dict4)
#
# ab = orders.aggregate([{
#     "$lookup": {
#         "from": "customers",
#         "localField": "customer_id",
#         "foreignField": "_id",
#         "as": "info"
#
#     }},
#     {
#         "$unwind": "$info"
#     },
#     {
#         "$project": {
#             "_id": 1,
#             "order_id": 1,
#             "customer_id": 1,
#             "info.name": 1,
#             "info.email": 1,
#             "info.address": 1,
#             "total_amount": 1
#         }
#     }
#
# ])
#
# print(list(ab))

# dict5 = [{
#     "_id": 101,
#     "department_name": "Human Resources"
# },
#     {
#         "_id": 102,
#         "department_name": "Marketing"
#     }]
#
# dict6 = [{
#     "_id": 201,
#     "name": "John Doe",
#     "email": "john.doe@example.com",
#     "department_id": 101
# },
#     {
#         "_id": 202,
#         "name": "Jane Smith",
#         "email": "jane.smith@example.com",
#         "department_id": 102
#     }]
#
# # dc = departments.insert_many(dict5)
# # ec = employees.insert_many(dict6)
#
# lookup1 = departments.aggregate([{
#     "$lookup": {
#         "from": "employees",
#         "localField": "_id",
#         "foreignField": "department_id",
#         "as": "employee_info"
#     }},
#     {
#         "$unwind": "$employee_info"
#     },
#     {
#         "$project": {
#             "_id": 1,
#             "department_name": 1,
#             "employee_info.name": 1,
#             "employee_info.email": 1,
#
#
#
#         }
#     }
# ])
#
# print(list(lookup1))


students = db["students"]
courses = db["courses"]

student_dict = [{
    "_id": 101,
    "name": "John Doe",
    "age": 20,
    "course_id": 301
},
    {
        "_id": 102,
        "name": "Jane Smith",
        "age": 22,
        "course_id": 302
    }]

courses_dict = [{
    "_id": 301,
    "course_name": "Mathematics",
    "instructor": "Professor Johnson",
    "credits": 4
},
    {
        "_id": 302,
        "course_name": "History",
        "instructor": "Professor Williams",
        "credits": 3
    }]

# students.insert_many(student_dict)
# courses.insert_many(courses_dict)
#
# student_info = students.aggregate([
#     {
#         '$lookup': {
#             'from': 'courses',
#             'localField': 'course_id',
#             'foreignField': '_id',
#             'as': 'student_info'
#         }
#     },
#     {
#         '$unwind': "$student_info"
#     },
#     {
#         '$project': {
#             '_id': 1,
#             'name': 1,
#             'age': 1,
#             'course_info': 'student_info.course_name',
#             'course_instructor': 'student_info.instructor',
#             'course_credits': 'student_info.credits'
#         }
#     }
#
# ])
#
# pprint(list(student_info))

products = db["products"]
reviews = db["reviews"]

products_list = [{
    "_id": 301,
    "product_name": "Smartphone",
    "category": "Electronics",
    "price": 499.99
},
    {
        "_id": 302,
        "product_name": "Laptop",
        "category": "Electronics",
        "price": 1099.99
    }]

reviews_list = [{
    "_id": 401,
    "product_id": 301,
    "rating": 4.5,
    "comment": "Great phone, highly recommended!"
},
    {
        "_id": 402,
        "product_id": 301,
        "rating": 5.0,
        "comment": "Excellent value for money."
    },
    {
        "_id": 403,
        "product_id": 302,
        "rating": 4.0,
        "comment": "Powerful laptop, but a bit expensive."
    }]

# reviews.insert_many(reviews_list)
# products.insert_many(products_list)

aggregation = reviews.aggregate([{
    "$group": {
        "_id": "$product_id",
        "Average_ratings": {"$avg": "$rating"}
    }},
    # {
    # "$lookup": {
    #     "from": "products",
    #     "localField": "_id",
    #     "foreignField": "product_id",
    #     "as": "full_info"
    # }},
    # {
    #     "$unwind": "$full_info"
    # },
    # {
    #     "$project": {
    #         "id": "product_id",
    #         "product_name": "full_info.name",
    #         "category": "full_info.category",
    #         "price": "full_info.price",
    #         "Average_ratings": 1
    #     }
    #
    # }
])

# print(list(aggregation))


books = db["books"]
authors = db["authors"]
books_list = [{
    "_id": 101,
    "title": "The Great Gatsby",
    "genre": "Fiction",
    "author_id": 201
},
    {
        "_id": 102,
        "title": "To Kill a Mockingbird",
        "genre": "Fiction",
        "author_id": 202
    }]

authors_list = [{
    "_id": 201,
    "author_name": "F. Scott Fitzgerald",
    "birth_year": 1896
},
    {
        "_id": 202,
        "author_name": "Harper Lee",
        "birth_year": 1926
    }
]

# books.insert_many(books_list)
# authors.insert_many(authors_list)

# books_info = books.aggregate([
#     {
#         '$lookup': {
#             'from': 'authors',
#             'localField': 'author_id',
#             'foreignField': '_id',
#             'as': 'full_info'
#         }
#     },
#     {
#         '$unwind': {
#             'path': '$full_info'
#         }
#     },
#     {
#         "$project": {
#             "_id": 1,
#             "title": 1,
#             "genre": 1,
#             "author_name": "$full_info.author_name",
#             "birth_year": "$full_info.birth_year"
#         }
#     }
# ])
#
#
# pprint(list(books_info))


orders_list = [{
    "_id": 301,
    "order_id": "ORD-001",
    "customer_id": 401,
    "total_amount": 50.99
},
    {
        "_id": 302,
        "order_id": "ORD-002",
        "customer_id": 402,
        "total_amount": 99.99
    }]

customers_list = [{
  "_id": 401,
  "customer_name": "John Doe",
  "email": "john.doe@example.com",
  "address": "123 Main St, City"
},
    {
  "_id": 402,
  "customer_name": "Jane Smith",
  "email": "jane.smith@example.com",
  "address": "456 Park Ave, Town"
}
]

orders = db["orders"]
customers = db["customers"]

# orders.insert_many(orders_list)
# customers.insert_many(customers_list)

customer_info = customers.aggregate([{
    "$lookup": {
        "from": "orders",
        "localField": "_id",
        "foreignField": "customer_id",
        "as": "orders_information"
    }
}])