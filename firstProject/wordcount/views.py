from django.shortcuts import render
from .models import Words
from konlpy.tag import Mecab
def home(request):
    return render(request, 'wordcount/home.html')

def about(request):
    
    return render(request, 'wordcount/about.html')


def count(request):
    full_text = request.GET['fulltext']

    tagger = Mecab() #형태소 분석기

    word_list = tagger.nouns (full_text)#명사만 추출하기 return은 dict형태

    #word_list = full_text.split()

    word_dictionary = {}

    for word in word_list:
        if Words.objects.filter(text=word):
            word =  Words.objects.get(text=word)
            word.frequency_total += 1
            word.save() 
        else:
            word = Words(text=word, frequency_total=1) 
            word.save()
        if word in word_dictionary:
            word_dictionary[word] += 1
        else :
            word_dictionary[word] = 1

    return render(request, 'wordcount/count.html',{'fulltext' : full_text, 'total': len(word_list), 'word_dictionary':word_dictionary.items() })
# Create your views here.
