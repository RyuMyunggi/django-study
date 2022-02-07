from django.http import HttpResponse
from django.shortcuts import render, redirect
import random
from django.views.decorators.csrf import csrf_exempt

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

nextId = 4


def index(request):
    article = '''
            <h2>Hello Django</h2>
            welcome
    '''
    return HttpResponse(HTMLTemplate(article))


def HTMLTemplate(articleTag, id=None):
    global topics
    contextUI = ''
    if id != None:
        contextUI = f'''
            <li>
                <form action="/delete/", method="post"> 
                    <input type="hidden" name="id" value="{id}">   
                    <input type="submit" value="delete">
                </form>
            </li>
            <li><a href="/update/{id}">update</a></li>
        '''

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
                <li>
                    <a href="/create">create</a>
                </li>
                {contextUI}
            </ul>
        </body>
        </html>
    '''


@csrf_exempt
def create(request):
    global nextId

    # 사용자 http method 확인
    if request.method == 'GET':
        # http method 변경
        article = '''
            <form action="/create/" method="post">
                <p><input type="text" name="title" placeholder="title"></p>
                <p><textarea name="body" placeholder="body"></textarea></p>
                <p><input type="submit"></p>
            </form>
        '''
        return HttpResponse(HTMLTemplate(article))

    elif request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        newTopic = {"id": nextId, "title": title, "body": body}
        url = '/read/' + str(nextId)
        nextId += 1
        topics.append(newTopic)
        return redirect(url)


# 가변적인 값을 받을 때는 두번 째 인자로 가변값의 이름을 받음
def read(request, id):
    global topics
    article = ''
    for topic in topics:
        if topic['id'] == int(id):
            article = f'<h2>{topic["title"]}</h2>{topic["body"]}'
    return HttpResponse(HTMLTemplate(article, id))


@csrf_exempt
def delete(request):
    global topics
    if request.method == 'POST':
        id = request.POST['id']
        newTopics = []
        for topic in topics:
            if topic['id'] != int(id):
                newTopics.append(topic)
        topics = newTopics
        return redirect('/')


@csrf_exempt
def update(request, id):
    global topics
    if request.method == 'GET':
        for topic in topics:
            if topic['id'] == int(id):
                selectedTopic = {
                    'title': topic['title'],
                    'body': topic['body']
                }

        article = f'''
            <form action="/update/{id}/" method="post">
                <p><input type="text" name="title" placeholder="title" value={selectedTopic['title']}></p>
                <p><textarea name="body" placeholder="body">{selectedTopic['body']}</textarea></p>
                <p><input type="submit"></p>
            </form>
        '''
        return HttpResponse(HTMLTemplate(article, id))
    elif request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        for topic in topics:
            if topic['id'] == int(id):
                topic['title'] = title
                topic['body'] = body
        return redirect(f'/read/{id}')