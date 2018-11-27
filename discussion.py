import sys
import json
from bs4 import BeautifulSoup
from selenium import webdriver
import selenium as se
from splinter import Browser
import time

def save_as_json(dict_name,file_name):
    dict_cache = json.dumps(dict_name,indent=4)
    f = open(file_name,"w")
    f.write(dict_cache)
    f.close()

# try:
#     cache_file = open('leetcode_questions.json', 'r')
#     cache_contents = cache_file.read()
#     data = json.loads(cache_contents)
#     cache_file.close()
# except:
#     print("something bad happens!")
#
#
# with Browser("chrome") as browser:
#     for key in data.keys():
#         prob_url = data[key]['problem_url'] + '/discuss/?orderBy=most_votes'
#         print(prob_url)
#         browser.visit(prob_url)
#         time.sleep(5)
#         my_html = browser.html
#         result[key]=my_html
#
#
# save_as_json(result, 'discussion_lists2.json')

result = {}
try:
    cache_file = open('discussion_lists2.json', 'r')
    cache_contents = cache_file.read()
    discussion_list = json.loads(cache_contents)
    cache_file.close()
except:
    print("something bad happens!")

for key in discussion_list:
    discussions = []
    urls = []
    votes = []
    views = []

    discussion_title = ""
    m_soup = BeautifulSoup(discussion_list[key], features="html.parser")
    discussion_blocks = m_soup.find_all('div', class_='topic-item__2RLo')
    if len(discussion_blocks)!=0:
        for db in discussion_blocks:
            content=db.find('div')
            discussions.append(content.find('div',class_='topic-title__2w2q').text)
            urls.append(content.find('a')['href'])
            odd = True
            nums = db.find_all('div', class_='no__1L9S')
            for num in nums:
                if odd:
                    try:
                        votes.append(num.text)
                    except:
                        votes.append('')
                else:
                    try:
                        views.append(num.text)
                    except:
                        views.append('')
                odd = not odd
    else:
        print(key)

    if len(votes)!=0:
        result[key] = []
        for i in range(5):
            result[key].append({})
            result[key][i]['discussion_title'] = discussions[i]
            result[key][i]['discussion_vote'] = votes[i]
            result[key][i]['discussion_views'] = views[i]
            result[key][i]['discussion_link'] = 'https://leetcode.com' + urls[i]


print(len(result))
save_as_json(result,'discussion_list3.json')
