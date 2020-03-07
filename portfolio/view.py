from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(request):
    # return HttpResponse('Hello World')
    return render(request,'home.html')

# def about(request):
#     # return HttpResponse('Hello World')
#     # test commit from Git and try to see how it update back to VScode
#     return render(request,'about.html')

# def eggs(request):
#     return HttpResponse('<h1>This is eggs page test</h1>')


# def count(request):
#     # return HttpResponse('Hello World')
#     fulltext = request.GET['fulltext']
#     length = len(fulltext)
#     wordlist = fulltext.split()
#     print(fulltext)
#     print(wordlist)

#     worddictionary = {}

#     for word in wordlist:
#         if word in worddictionary:
#             #increse
#             worddictionary[word] += 1
#         else:
#             #add in Dic
#             worddictionary[word] = 1

#     sortedoutput = sorted(worddictionary.items(), key=operator.itemgetter(1),reverse =True)
#     return render(request,'count.html',{'fulltext':fulltext, 'count' : length , 'words': len(wordlist), 'worddictionary':sortedoutput})

