from pymongo import MongoClient

# Test database.
# my_database = "WebData_test"
my_database = "PlayStore"


# main database.
# my_database = "WebData"


# Getting database Client.
def get_db_client():
    return MongoClient("localhost", 27017)


# Getting the database by database name.
# If database not exists then create.
def get_database(database_name: str):
    return get_db_client().get_database(database_name)


# Getting the collection from database.
# If collection not exists then create.
def get_collection(Collection_name: str, database_name: str):
    # print("data" + str(database_name) )
    # print("Collection_name" + str(Collection_name) )
    return get_database(database_name).get_collection(Collection_name)


# Getting the links collection.
def get_crawl_links_collection():
    return get_collection("crawl_links_collection", my_database)


# Getting the Response Logs collection.
def get_response_logs_collection():
    return get_collection("response_logs_collection", my_database)