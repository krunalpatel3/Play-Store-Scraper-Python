import threading
from datetime import datetime
from http.client import InvalidURL
from requests.utils import requote_uri


# get all links from html.
def get_links_html(getHtml, tabName, dictionary):
    try:
        if getHtml is not None:
            get_links = getHtml.findAll(tabName, dictionary)
            if get_links is not None and len(get_links) > 0:
                return list(set(get_attribute_value(get_links, "a", "href", "url")))
            else:
                return ""

    except Exception as e:
        print("get_attribute_value " + str(e))


def get_attribute_value(selected_html, find_all_tabs, attribute, mode):
    try:
        values_list = []
        if len(selected_html) > 0:
            for link in selected_html:
                all_tabs = link.find_all(find_all_tabs)  # For ex:- a ,input
                for a in all_tabs:
                    if mode == "url":
                        values_list.append(requote_uri(a.get(attribute)))
                    else:
                        values_list.append(a.get(attribute))

            return values_list

    except Exception as e:
        print("get_attribute_value " + str(e))


def current_date_time():
    """ Get Current date and time."""
    return datetime.now()


# Create Thread.
# Return thread object.
def create_thread(task):
    """ Create Thread. :param task: :return: thread object. """
    print(task.__hash__())
    return threading.Thread(target=task)



