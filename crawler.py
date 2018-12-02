from splinter import Browser
import json
import time
from bs4 import BeautifulSoup

# useful functions
def save_as_json(dict_name,file_name):
    dict_cache = json.dumps(dict_name,indent=4)
    f = open(file_name,"w")
    f.write(dict_cache)
    f.close()

# crawl leetcode problems
def crawl_leetcode_problems():
    f=open("leetcode.html")
    lines=f.readlines()
    page_content=""
    for l in lines:
        page_content+=l
    f.close()
    page_soup = BeautifulSoup(page_content, 'html.parser')
    all_problems = page_soup.find(class_="reactable-data")
    problem_blocks=all_problems.find_all('tr')
    for i in range(len(problem_blocks)):
        question_content={}
        problem_block_content=problem_blocks[i].find_all('td')
        question_content['problem_id']=int(problem_block_content[1].text)
        question_content['problem_title']=problem_block_content[2]['value']
        question_content['problem_url']=problem_block_content[2].find('a')['href']
        question_content['problem_acceptable']=problem_block_content[4]['value']
        question_content['problem_difficult']=problem_block_content[5].text
        leetcode_questions[str(int(problem_block_content[1].text))]=question_content
    save_as_json(leetcode_questions,'leetcode_questions.json')

# crawl description pages
def crawl_leetcode_description_pages():
    try:
        cache_file = open('leetcode_questions.json', 'r')
        cache_contents = cache_file.read()
        leetcode_questions = json.loads(cache_contents)
        cache_file.close()
    except:
        print("something bad happens!")

    leetcode_descriptions={}
    with Browser("chrome") as browser:
        # Visit URL
        for each in leetcode_questions:
            url = leetcode_questions[each]['problem_url']
            browser.visit(url)
            # wait for 5 mins in order to load all pages
            time.sleep(5)
            content_page=browser.html
            leetcode_descriptions[leetcode_questions[each]['problem_title']]=content_page

    save_as_json(leetcode_descriptions,'descriptions.json')

# crawl descriptions
def crawl_leetcode_descriptions():
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
                problem_related_qs=page_soup.find_all('div',class_="question__3owm")
                problem_tag_list=[]
                for tag in problem_tags:
                    problem_tag_list.append(tag.text)
                problem_related_list=[]
                for rq in problem_related_qs:
                    problem_related_list.append(rq.text)

                my_description['problem_name']=problem_name
                my_description['problem_description']=problem_description
                my_description['problem_tags']=problem_tag_list
                my_description['related_questions']=problem_related_list
                my_descriptions[str(problem_id)]=my_description

    save_as_json(my_descriptions,"problem_descriptions2.json")
    print(len(my_descriptions))

# crawl_leetcode_problems()
# crawl_leetcode_description_pages()
crawl_leetcode_descriptions()

# try:
#     cache_file = open('discussion_list3.json', 'r')
#     cache_contents = cache_file.read()
#     discussion_lists = json.loads(cache_contents)
#     cache_file.close()
# except:
#     print("something bad happens!")
#
# discussion_pages={}
# with Browser("chrome") as browser:
#     # Visit URL
#     for each in discussion_lists:
#         for i in range(len(discussion_lists[each])):
#             if 'discussion_link' in discussion_lists[each][i]:
#                 url = discussion_lists[each][i]['discussion_link']
#                 browser.visit(url)
#                 # wait for 5 mins in order to load all pages
#                 time.sleep(5)
#                 content_page=browser.html
#                 discussion_pages[str(each)+":"+str(i)]=content_page
#
# save_as_json(discussion_pages,'discussion_pages.json')
