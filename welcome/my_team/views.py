from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def result(request):
    team = request.GET['team']
    sentence = request.GET['sentence']
    wordList = sentence.split(",")
    return render(request, 'result.html', 
    {'fulltext':sentence, 'count':len(wordList), 'wordList':wordList, 'teamname':team})
# Create your views here.
