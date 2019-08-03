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
   
    from elasticsearch import Elasticsearch
    es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    
    dd = es.search(index="product", body={"query": {"match":


    {"title": djtext}},"highlight":{"fields":{"title":{}}

     
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
       
    parms = {'search_result': comp_data}
    return render(request, 'out.html',parms)
    
