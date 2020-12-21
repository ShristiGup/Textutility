#I have created this file.
from django.http import HttpResponse
from django.shortcuts import render

# def site1(request):
#     return HttpResponse('''<a href="https://www.facebook.com/">Go to facebook </a>
#     <a href="https://www.youtube.com/">Go to youtube</a>
#     <a href="https://twitter.com/">Go to twitter</a>
#     <a href="https://www.google.com/">Go to google</a>
#     <a href="https://www.instagram.com/">Go to instagram</a>
#     ''')

# def about(request):
#     return HttpResponse("About world")

def index(request):
    return render(request,'index.html')
    # return HttpResponse('''<h1>Home</h1>
    # <button><a href="/removepunc">Go to remove punc</a></button>
    # <button><a href="/capitalizefirst">Go to capitalize first</a></button>
    # <button><a href="/newlineremove">Go to newline remover</a></button>
    # <button><a href="/spaceremove">Go to space remover</a></button>
    # <button><a href="/charcount">Go to charcount</a></button>''')

def analyze(request):
    djtext = request.POST.get('mytext','default')
    rmpunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    charcount = request.POST.get('charcount','off')
    flag = 0
    purpose=""
    if rmpunc=="on" and len(djtext)!=0:
        punc = """\\~`!@#$}%^&*()_-{[]:;"'|/?>.<,"""
        ana_text=""
        for i in djtext:
            if i not in punc:
                ana_text+=i
        params={"purpose":"Remove Punctuation","analyzed_text":ana_text}
        purpose+="Remove Punctuation/"
        djtext = ana_text
        flag=1
    if fullcaps=="on" and len(djtext)!=0:
        ana_text = djtext.upper()
        purpose+="Changed To Uppercase/"
        params={"purpose":purpose,"analyzed_text":ana_text}
        djtext = ana_text
        flag=1
    if newlineremover=="on" and len(djtext)!=0:
        ana_text = ""
        for i in djtext:
            if i!="\n" and i!="\r":
                ana_text+=i
        purpose+="Newlines Removed/"
        params={"purpose":purpose,"analyzed_text":ana_text}
        djtext = ana_text
        flag=1
    if extraspaceremover=="on" and len(djtext)!=0:
        ana_text = ""
        for i in range(len(djtext)):
            if not(djtext[i]==" " and djtext[i+1]==" "):
                ana_text+=djtext[i]
        purpose+="Extra Spaces Removed/"
        params={"purpose":purpose,"analyzed_text":ana_text}
        djtext = ana_text
        flag=1
    if charcount=="on" and len(djtext)!=0:
        ana_text = len(djtext)
        purpose+="The total characters present are:"
        params={"purpose":purpose,"analyzed_text":ana_text}
        flag=1
    if flag==1:
        return render(request,'analyze.html',params)
    else:
        return HttpResponse("Error")
# def analyze(request):
#     djtext = request.GET.get('mytext','default')
#     rmpunc = request.GET.get('removepunc','off')
#     print(djtext)
#     if rmpunc=="on" and len(djtext)!=0:
#         # punc = """\\~`!@#$}%^&*()_-{[]:;"'|/?>.<,"""
#         s = djtext
#         # ana_text=""
#         for i in djtext:
#             if not('a'<=i<='z' or 'A'<=i<='Z' or '0'<=i<='9' or i==" "):
#                 s = s.replace(i,"")
#         params={"purpose":"Remove Punctuation","analyzed_text":s}
#         return render(request,'analyze.html',params)
#     else:
#         return HttpResponse("Error")
# def removepunc(request):
#     djtext = request.GET.get('mytext','default')
#     print(djtext)
#     return HttpResponse('''remove punc
#     <button><a href="/">Back</a></button>''')

# def capitalizefirst(request):
#     return HttpResponse('''capitalize first
#     <button><a href="/">Back</a></button>''')

# def newlineremove(request):
#     return HttpResponse('''remove new line
#     <button><a href="/">Back</a></button>''')

# def spaceremove(request):
#     return HttpResponse('''remove spaces
#     <button><a href="/">Back</a></button>''')

# def charcount(request):
#     return HttpResponse('''counts char
#     <button><a href="/">Back</a></button>''')