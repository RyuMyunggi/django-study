from django.http import HttpResponse
from django.shortcuts import render
import random

# Create your views here.

# 첫 번째 인자는 요청과 관련한 객체를 받음. 관습적으로 request
# def index(request):
#     # http를 이용하여 응답
#     return HttpResponse('<h1>Welcome</h1>'+str(random.random()))

topics = [
    {'id': 1, 'title': 'routing', 'body': 'Routing is..'},
    {'id': 2, 'title': 'view', 'body': 'View is..'},
    {'id': 3, 'title': 'model', 'body': 'Model is..'}
]


def index(request):
    article = '''
            <h2>Hello Django</h2>
            welcome
    '''
    return HttpResponse(HTMLTemplate(article))


def HTMLTemplate(articleTag):
    global topics
    ol = ''
    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
    return f'''
        <html>
        <body>
            <h1><a href="/">Django<a></h1>
            <ol>
                {ol}
            </ol>
            {articleTag}
            <ul>
                <a href="/create">create</a>
            </ul>
        </body>
        </html>
    '''


def create(request):
    article = '''
        <form action="/create/">
            <p><input type="text" name="title" placeholder="title"></p>
            <p><textarea name="body" placeholder="body"></textarea></p>
            <p><input type="submit"></p>
        </form>
    '''
    return HttpResponse(HTMLTemplate(article))

# 가변적인 값을 받을 때는 두번 째 인자로 가변값의 이름을 받음
def read(request, id):
    global topics
    article = ''
    for topic in topics:
        if topic['id'] == int(id):
            article = f'<h2>{topic["title"]}</h2>{topic["body"]}'
    return HttpResponse(HTMLTemplate(article))
