import random
from time import sleep

from Process.DatabaseOperation import get_links, update_link_status
from Process.SaveDetailsCollectLinks import save_links_front_page, save_details
from Utility.NetworkRequest import getHtml_Str_From_Url

# url = 'https://play.google.com/store/apps?hl=en_IN&gl=IN'
# url = 'https://play.google.com/store/apps/collection/cluster?clp=ogooCAEaHAoWcmVjc190b3BpY19OeTFXWFM3VGhMZxA7GAMqAggBUgIIAg%3D%3D:S:ANO1ljIID9g&gsr=CiuiCigIARocChZyZWNzX3RvcGljX055MVdYUzdUaExnEDsYAyoCCAFSAggC:S:ANO1ljKrItI&hl=en_IN&gl=IN'
# url = 'https://play.google.com/store/apps/details?id=com.axis.mobile&hl=en_IN&gl=IN'
url = 'https://play.google.com/store/apps'
# url = 'https://play.google.com/store/apps/details?id=com.coinbase.android'


def run_play_store(page_size,page_num):
    # (getHtml, session, response_code) = getHtml_Str_From_Url(url, True)
    # save_links_front_page(getHtml)
    # save_details(getHtml)

    links_list = list(get_links(False, 'Play Store', page_size, page_num))
    i = len(links_list)

    while i > 0:
        # 10 seconds sleep the thread.
        sleep(10)

        (getHtml, session, response_code) = getHtml_Str_From_Url(links_list[i - 1]['Url'], True)

        save_links_front_page(getHtml)
        save_details(getHtml)

        update_link_status(links_list[i - 1]['Url'])

        i -= 1
        # remove crawled url from links_list.
        links_list.pop(i)

        # shuffle items from links_list.
        random.shuffle(links_list)

        # if links_list less than equal to 3 then get more crawling links from database.
        if i <= 3:
            links_list.extend(list(get_links(False, 'Play Store', page_size, page_num)))
            i = len(links_list)