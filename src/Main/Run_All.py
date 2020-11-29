import multiprocessing

from Process.DatabaseOperation import insert_links, create_index
from Process.MainProcess import run_play_store
from Utility.NetworkRequest import getHtml_Str_From_Url
from Utility.Utility import get_links_html, create_thread

if __name__ == '__main__':

    ''' In order to run you need to do
        1) Install mongodb 
        2) Install tor and run tor.exe
        3) Create index uncomment create_index() to create index.
        4) Need to insert url https://play.google.com/store/apps in crawl_links_coll.
        
        after you complete the following steps you can run the project.
    '''

    # Create index in crawl_links_coll of field Url.
    # Create index in Play_store_coll of field WebSite,Email.
    # create_index()

    # insert_links(['https://play.google.com/store/apps'])

    thread1 = create_thread(run_play_store(50,1))
    thread1.start()

    thread1.join()


