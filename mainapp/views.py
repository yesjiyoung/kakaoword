from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def result(request):
    return render(request, 'result.html')

def result(request):
    text = request.GET['fulltext']
    words = text.split()
    splitwords = len(words)
    
    word_dic = {}
    for word in words:
        if word in word_dic:
            #increase
            word_dic[word] += 1          
        else:
            word_dic[word] = 1  
    import operator
    sorteddic = sorted(word_dic.items(), key = operator.itemgetter(1), reverse = True )
    return render(request, 'result.html',{'full': text , 'total':splitwords, 'dictonary':sorteddic})