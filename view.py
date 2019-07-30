from django.conf.locale import es
from django.http import HttpResponse
from django.shortcuts import render
import json
def index(request):
    return render(request, 'index.html')

def removepunc(request):
    djtext = request.GET.get('text','default')

    import requests
    res = requests.get('http://localhost:9200')
    #print(res.content)
    from elasticsearch import Elasticsearch
    es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    #print(es.get(index='test-index', doc_type='test', id=1))
   #print(es.search(index="product", body={"query": {"match": {"title": djtext}}}))
#d =(es.search(index="product", body={"query": {"match": {"title": djtext}}}))
    dd = es.search(index="product", body={"query": {"match":


    {"title": djtext}},"highlight":{"fields":{"title":{}}

        #{"pre_tags":"<marks>","post_tags":"</marks>"{"fields":{"title":{}}}
                                    }})
    #de = json.dumps(dd)
    comp_data = []
    comp_doc = {}
    for doc in dd['hits']['hits']:
        for key, value in doc['highlight'].items():
            for i in value:
                try:
                    comp_doc = {
                'comp_name': doc['_source']['title']

                            }
                    comp_data.append(comp_doc)
                except:
                    pass
        #print( doc["_source.title"])
    #print(dd)
    #print("%d documents found" % dd['hits']['total'])
    #for doc in dd['hits']['hits']:
        #print("%s) %s" % (doc['_id'], doc['_source']['content']))

    #for p in dd['title']:
        #print('title: ' + p['title'])
    #3for hit in  dd['hits']['hits']:
        #dj = dd['hits']['hits']
        #de = hit['_source']['title']
        #de = de + de

        #df = hit ['_source'] ['description']
        #df = df + "/n" + df
        #print(dj)
    #comp_data.append(comp_doc)
    parms = {'search_result': comp_data}
    return render(request, 'out.html',parms)
    #return render("testing")
    #return HttpResponse("remove punc")
#print(request.GET.get('text','default)
#return HttpResponse ("REMOVE PUNCS")
