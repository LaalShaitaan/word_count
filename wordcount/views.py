from django.http import HttpResponse
from django.shortcuts import render


def first(request):
    return HttpResponse("<h1>This is my first page.</h1>")

def second(request):
    return render(request,'first.html')

def count(request):
    return render(request,'count.html')

def aftercount(request):
    FULLTEXT= request.GET['fulltext']
    print(FULLTEXT)

    countword=FULLTEXT.split()

    worddict={}

    for word in countword:
        if word in worddict:
            worddict[word]+=1
        else:
            worddict[word]=1


    return render(request,'aftercount.html',{'fulltext':FULLTEXT,'countw':len(countword), 'worddict':worddict.items()})
