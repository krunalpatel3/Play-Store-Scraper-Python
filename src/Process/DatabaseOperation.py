import pymongo

from Utility.Mongodb import get_collection, my_database, get_crawl_links_collection
from Utility.Utility import current_date_time

Play_store_coll = get_collection("Play_store_collection", my_database)
crawl_links_coll = get_crawl_links_collection()


def insert_links(links_list):
    try:
        print("insert_links")
        for item in links_list:
            if crawl_links_coll.count_documents({'Url': item}) == 0:
                crawl_links_coll.insert_one({'Url': item, 'Crawl_Status': False,
                                             'Web_Site': "Play Store", 'DateTime': current_date_time()})

    except Exception as e:
        print("Exception " + str(e))


def insert_details(details):
    try:
        # Check if details of company already exists.
        # if not exists then insert in database.
        if Play_store_coll.count_documents({'WebSite': details.get('WebSite'),
                                            'Email' : details.get('Email')}) == 0:
            Play_store_coll.insert_one(details)

    except Exception as e:
        print("Exception " + str(e))


def get_links(status, web_site, page_size, page_number):
    """ Get urls 50 by website Name which are not Crawl. """

    try:
        # Calculate number of documents to skip
        skips = page_size * (page_number - 1)  # page_size will always be 50.And page_number will change like
        # Ex 1,2,3.

        for links in crawl_links_coll.find({'Crawl_Status': status, 'Web_Site': web_site}) \
                .skip(skips).limit(page_size):
            print(links)
            yield links
    except Exception as e:
        print("Exception " + str(e))


def update_link_status(link):
    """ Update Crawl_Status to True to insure that the url is Crawl. """
    try:
        crawl_links_coll.update_one({"Url": link}, {"$set": {"Crawl_Status": True}})
    except Exception as e:
        print("Exception " + str(e))


def create_index():
    """ create index from crawl_links_coll."""
    # create an index in descending order
    resp = crawl_links_coll.create_index([("Url", pymongo.DESCENDING)])
    print("index response:", resp)
    resp = Play_store_coll.create_index([("WebSite", pymongo.ASCENDING),("Email", pymongo.ASCENDING)])
    print("index response:", resp)
