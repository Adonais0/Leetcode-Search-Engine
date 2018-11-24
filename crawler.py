from splinter import Browser
import json
import time
from bs4 import BeautifulSoup

def save_as_json(dict_name,file_name):
    dict_cache = json.dumps(dict_name,indent=4)
    f = open(file_name,"w")
    f.write(dict_cache)
    f.close()

# try:
#     cache_file = open('leetcode_questions.json', 'r')
#     cache_contents = cache_file.read()
#     leetcode_questions = json.loads(cache_contents)
#     cache_file.close()
# except:
#     print("something bad happens!")
#

#
# leetcode_descriptions={}
# with Browser("chrome") as browser:
#     # Visit URL
#     for each in leetcode_questions:
#         url = leetcode_questions[each]['problem_url']
#         browser.visit(url)
#         time.sleep(5)
#         content_page=browser.html
#         leetcode_descriptions[leetcode_questions[each]['problem_title']]=content_page
#
# save_as_json(leetcode_descriptions,'descriptions.json')

try:
    cache_file = open('descriptions.json', 'r')
    cache_contents = cache_file.read()
    leetcode_questions = json.loads(cache_contents)
    cache_file.close()
except:
    print("something bad happens!")

my_descriptions={}
for each in leetcode_questions:
    if each in leetcode_questions[each]:
        page_soup = BeautifulSoup(leetcode_questions[each], 'html.parser')
        if page_soup.find('div',class_="tab-pane__280T css-18a8uxa-TabContent e5i1odf5")!=None:
            my_description={}
            all_problems = page_soup.find('div',class_="tab-pane__280T css-18a8uxa-TabContent e5i1odf5")
            problem_id,problem_name=page_soup.find('div',class_='css-101rr4k').find('div',class_="css-1ponsav").text.split(". ")
            # problem_difficult=page_soup.find('div',class_='css-101rr4k').find('div',class_="css-ia03ri").text)
            problem_description=all_problems.find('div',class_="content__eAC7").text
            problem_tags=page_soup.find_all('a',class_="topic-tag__Hn49")
            problem_tag_list=[]
            for tag in problem_tags:
                problem_tag_list.append(tag.text)

            my_description['problem_name']=problem_name
            my_description['problem_description']=problem_description
            my_description['problem_tags']=problem_tag_list
            my_descriptions[str(problem_id)]=my_description

save_as_json(my_descriptions,"problem_descriptions.json")
print(len(my_descriptions))
