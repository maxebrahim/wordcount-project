from django.http import HttpResponse
from django.shortcuts import render


def getHome(request):
    return render(request, 'home.html', {'name': 'Wolf'})


def getAbout(request):
    return render(request, 'about.html')


def getCount(request):
    fulltext = request.GET['counttext']

    wordlist = fulltext.split()

    wordCounter = {}

    for word in wordlist:
        wordCounter[word] = wordlist.count(word)

    return render(request, "count.html",
                  {'fulltext': fulltext, 'count': len(wordlist), 'wordCounter': wordCounter})








