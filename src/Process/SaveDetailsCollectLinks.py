# Save link from front page.
from requests.utils import requote_uri

from Main.UrlConstraints import PLAY_STORE_MAIN_URL
from Process.DatabaseOperation import insert_links, insert_details
from Utility.Utility import get_links_html


def save_links_front_page(getHtml):
    try:

        # get Links from list.
        dic = {"class": "T4LgNb"}
        list_of_app_links = get_links_html(getHtml, "div", dic)

        # If we get url then insert.
        if list_of_app_links is not None and len(list_of_app_links) > 0:

            for url in list_of_app_links:
                # concat Base Url.
                if 'https://' not in url:
                    list_of_app_links[list_of_app_links.index(url)] = requote_uri(PLAY_STORE_MAIN_URL + url)

            # print(list_of_app_links)
            insert_links(list_of_app_links)

    except Exception as e:
        print("except save_links_front_page " + str(e))


def save_details(html_str):
    try:

        details_dic = {}

        get_developer_details = html_str.findAll("div", {"class": "hAyfc"})

        if get_developer_details is not None and get_developer_details.__len__() > 0:
            if get_developer_details[-1] is not None:
                developer_details = get_developer_details[-1].findAll("a", {"class": "hrTbp"})
                for details in developer_details:
                    if details is not None:
                        if 'Visit website' in details.get_text():
                            details_dic['WebSite'] = details.get('href')
                        elif 'Privacy Policy' in details.get_text():
                            details_dic['Privacy Policy'] = details.get('href')
                        else:
                            details_dic['Email'] = details.get_text()

            # Get Address
            developer_details = get_developer_details[-1].findAll("span", {"class": "htlgb"})

            if developer_details is not None and developer_details.__len__() > 0:
                get_div_tags = developer_details[0].findAll("div")
                if get_div_tags is not None and get_div_tags.__len__() > 0:
                    if 'Privacy Policy' not in get_div_tags[-1].get_text().replace("\n", " "):
                        details_dic['Address'] = get_div_tags[-1].get_text().replace("\n", " ")

            # company_name
            company_name = html_str.findAll("span", {"class": "T32cc UAO9ie"})

            if company_name is not None and company_name.__len__() > 0:
                get_company_name = company_name[0].findAll("a", {"class": "hrTbp R8zArc"})
                if get_company_name is not None and get_company_name.__len__() > 0:
                    details_dic['Company Name'] = get_company_name[0].get_text()

            # Check if details_dic is empty
            # if not empty then only insert details.
            if details_dic:
                print(details_dic)
                insert_details(details_dic)

            # Get Similar Links.
            dic = {"class": "tlG8q"}
            list_of_app_links = get_links_html(html_str, "aside", dic)
            if list_of_app_links is not None and list_of_app_links.__len__() > 0:
                # concat Base Url.
                for url in list_of_app_links:
                    if 'https://' not in url:
                        list_of_app_links[list_of_app_links.index(url)] = requote_uri(PLAY_STORE_MAIN_URL + url)

                insert_links(list_of_app_links)

    except Exception as e:
        print("Exception " + str(e))
