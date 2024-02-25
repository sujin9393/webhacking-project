from flask import Flask, redirect, request

app = Flask(__name__)

nextId = 4
topics= [
    {'id': 1, 'title': 'html', 'body':'html is...'},
    {'id': 2, 'title': 'css', 'body':'css is...'},
    {'id': 3, 'title': 'javascript', 'body':'javascript is...'},
]
# 항목에 대한 제목, 본문 내용 등등은 딕셔너리에 저장하는게 편함 
# 변수에 있는 데이터를 목록으로 표현

def template(contents, content):
        #반복되는 부분을 템플릿으로 만들기 

    return f'''<!doctype html>
    <html>
        <body>
        <h1><a href="/">WEB</a></h1>
        <ol>
            {contents}
        </ol>
        <ul>
            <li><a href="/create/">create</a></li>
        </ul>
    
        <h2>{content}</h2>
        Hello, web
    </body>
</html>
'''

def getContents():
    liTags = ''
    for topic in topics: 
         liTags = liTags +f'<li><a href="/read/{topic["id"]}/">{topic["title"]}</a></li>'
    return liTags

@app.route('/')
def index():
    return template(getContents(), '<h2>Welcome</h2>Hello, WEB')

@app.route('/create/', methods=['GET', 'POST'])
def create():
    if request.method =='GET':
        content = '''
            <form action="/create/" method="POST">
                <p><input type ="text" name ="title" placeholder="title"></p>
                <p><textarea name ="body" placeholder ="body"></textarea></p> 
                <p><input type ="submit" value="create"></p>
            </form>
    '''
        return template(getContents(), content)
    elif request.method =="POST":
         global nextId 
         #전역변수 
         title = request.form['title']
         body = request.form['body']
         newTopic = {'id': nextId, 'title': title, 'body': body}
         #next id 값에 새로운 아이디에 nextid를 넣기 
         #request form 을 이용해서 데이터 가져오기 
         topics.append(newTopic)
         url = '/read/' + str(nextId)+'/' 
         nextId=nextId + 1
         return redirect(url)

@app.route('/read/<int:id>/')
def read(id):
    title = ''
    body = ''
    for topic in topics: 
        if id == topic['id']:
            title = topic['title']
            body = topic['body']
            break
    return template(getContents(), f'<h2>{title}</h2>{body}')
 #현재 순번의 토픽과 아이디가 같다면 타이틀은 토픽의 타이틀 바디는 토픽 
            #int type id로 바꾸기 
            #조회하고 id와 일치하는 토픽 아이디면 그 토픽의 타이틀과 바디를 합성해서 결과 넣기 

@app.route('/update/<int:id>/', methods=['GET', 'POST'])
def update (id):
    if request.method == 'GET':
        content = '''
        <form action="/update/{id}"method="POST">
            <p><input type ="text" name="title" placeholder="title" value="{title}"></p>
            <p><textarea name = "body" placeholder="body">{body}</textarea></p>
            <p><input type = "submit" value ="update"></p>
        </form>
        '''
        title = ''
        body = ''
        for topic in topics:
            if id == topic['id']:
                title = topic ['title']
                body = topic ['body']
                break

@app.route('/delete/<int:id>/', methods=['POST'])
def delete(id):
    for topic in topics:
        if id == topic['id']:
            topics.remove(topic)
            break
    return redirect('/')
    
app.run(port=5001, debug=True)

