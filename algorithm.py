import json
# get discussion_list
try:
    cache_file = open('discussion_list3.json', 'r')
    cache_contents = cache_file.read()
    discussion_lists = json.loads(cache_contents)
    cache_file.close()
except:
    print("something bad happens!")

try:
    cache_file = open('leetcode_questions.json', 'r')
    cache_contents = cache_file.read()
    leetcode_questions = json.loads(cache_contents)
    cache_file.close()
except:
    print("something bad happens!")

try:
    cache_file = open('problem_descriptions.json', 'r')
    cache_contents = cache_file.read()
    problem_descriptions = json.loads(cache_contents)
    cache_file.close()
except:
    print("something bad happens!")


import pickle
def savePickle(dictfile,filename):
	print("saving....")
	f=open(filename+".pickle",'wb')
	pickle.dump(dictfile,f)
	f.close()

def loadPickle(filename):
	print("loading....")
	f=open(filename+".pickle",'rb')
	dictfile=pickle.load(f)
	f.close()
	return dictfile

meta=loadPickle('meta_stop')
weighted_scores=loadPickle('weighted_scores')
f=open('documents_id.txt')
lines=f.readlines()
f.close()
document_map={}
for each in lines:
    my_data=each.split("\t")
    document_map[my_data[0]]=my_data[1][:-1]

import math

class bm25_ctf():

    def __init__(self, k1 = 1.25, b = 0.9, k3 = 500):
        self.k1 = k1
        self.b = b
        self.k3 = k3

    def score_one(self, w,query_meta,meta,document_id):
        k1 = self.k1
        b = self.b
        k3 = self.k3
        #Fill your answer here
        ictf=math.log(meta['total_terms']/meta['corpus_term_count'][w])
        pidf=math.log(-(1-2**(-meta['corpus_term_count'][w]/meta['num_docs']))/(math.log(1-meta['doc_count'][w]/meta['num_docs']))+1)
        idf=math.log((meta['num_docs']-meta['doc_count'][w]+0.5)/(meta['doc_count'][w]+0.5))
        bidf=ictf*pidf*idf
        tf=((k1+1)*meta['btf'][w][document_id])/(k1*(1-b+b*meta['doc_size'][document_id]/meta['avg_dl'])+meta['btf'][w][document_id])
        qtf=((k3+1)*query_meta['query_term_weight'][w])/(k3+query_meta['query_term_weight'][w])

        res=bidf*tf*qtf

        return res

    def score(self,query_meta,document_id,meta):
        words=set(query_meta['query_words']) & meta['doc_unique_terms'][document_id]
        score=0
        for w in words:
            score+=self.score_one(w,query_meta,meta,document_id)
        return score

def get_weighted_score(query_meta,i,weighted_scores):
    score=0
    prog_lan_score=weighted_scores['prog_lan_score']
    tag_score=weighted_scores['tag_score']
    difficulty_score=weighted_scores['difficulty_score']
    title_score=weighted_scores['title_score']
    keywords_in_discussion=weighted_scores['keywords_in_discussion']
    for t in tag_score:
        if t in query_meta['query']:
            if str(i) in tag_score[t]:
                score+=tag_score[t][str(i)]*0.3
        if t in query_meta['query']:
            if str(i) in keywords_in_discussion[t]:
                score+=keywords_in_discussion[t][str(i)]
    for t in title_score:
        if t in query_meta['query']:
            if str(i) in title_score[t]:
                score+=title_score[t][str(i)]

    for w in query_meta['query'].split():
        if w in weighted_scores['prog_lan_score']:
            if i in weighted_scores['prog_lan_score'][w]:
                score+=weighted_scores['prog_lan_score'][w][i]*0.3
        if w in weighted_scores['difficulty_score']:
            if str(i) in weighted_scores['difficulty_score'][w]:
                score+=weighted_scores['difficulty_score'][w][str(i)]*0.1
        elif w=='difficult':
            if str(i) in weighted_scores['difficulty_score']['hard']:
                score+=weighted_scores['difficulty_score']['hard'][str(i)]*0.1

    vote_score=weighted_scores['vote_score']
    view_score=weighted_scores['view_score']
    if str(i) in vote_score:
        score+=vote_score[str(i)]*0.01+view_score[str(i)]*0.0001

    return score

def get_query_meta(query):
    if 'dynamic programming' in query:
        query+=' dp'
    elif 'dp' in query:
        query+=' dynamic programming'

    if query in query_logs:
        return query_logs[query]
    else:
        query_words=query.lower().split()

        query_length=len(query_words)
        query_term_weight={}
        for qw in query_words:
            if qw not in query_term_weight:
                query_term_weight[qw]=1
            else:
                query_term_weight[qw]+=1


        query_meta={}
        query_meta['query_length']=query_length
        query_meta['query_term_weight']=query_term_weight
        query_meta['query_words']=query_words
        query_meta['query']=query
        query_meta['related_query']=[]
        query_logs[query]=query_meta
        return query_meta

import pandas as pd
def do_search(query,meta,weighted_scores):
    d_scores={}
    query_meta=get_query_meta(query)
    print("query:",query_meta['query'])
    # print("result:")
    for i in range(1,meta['num_docs']):
        d_scores[i]=[ranker.score(query_meta,i,meta)+get_weighted_score(query_meta,i,weighted_scores)]
    my_frame=pd.DataFrame.from_dict(d_scores).T
    my_frame.columns=['scores']
    my_frame=my_frame.sort_values(by='scores',ascending=False)
    # print(my_frame.head(10))
#     print("related query:")
#     RQ_len=5
#     if len(query_meta['related_query'])<5:
#         RQ_len=len(query_meta['related_query'])
#     for i in range(RQ_len):
#         print(query_meta['related_query'][i], end=" ")
    return d_scores,my_frame

ranker=bm25_ctf()
query_logs={}
query=input("What do you want to search?")
while query:
    d_scores,my_frame=do_search(query,meta,weighted_scores)
    id_=list(my_frame.head(10).index.values)

    for each in id_:
        qid,did=document_map[str(each)].split("-")
        print(discussion_lists[str(qid)][int(did)]['discussion_title'])
        print(discussion_lists[str(qid)][int(did)]['discussion_link'])
    #     print(leetcode_questions[str(qid)]['problem_title'])
    #     print(leetcode_questions[str(qid)]['problem_url'])

    #     print(leetcode_questions[str(qid)])
    #     print(discussion_lists[str(qid)][int(did)])
    query=input("What do you want to search?")
