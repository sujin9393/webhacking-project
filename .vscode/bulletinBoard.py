from flask import Flask, redirect, request

app = Flask(__name__)

nextId = 4
posts = [
    {'id': 1, 'title': 'First Post', 'content': 'This is the content of the first post.'},
    {'id': 2, 'title': 'Second Post', 'content': 'This is the content of the second post.'},
    {'id': 3, 'title': 'Third Post', 'content': 'This is the content of the third post.'}
]


def get_contents():
    li_tags = ''
    for post in posts:
        li_tags += f'<li><a href="/read/{post["id"]}">{post["title"]}</a></li>'
    return li_tags


def template(contents, content):
    return f'''<!doctype html>
<html>
    <body>
        <h1><a href="/">Bulletin Board</a></h1>
        <ol>
            {contents}
        </ol>
        <ul>
            <li><a href="/create/">Create Post</a></li>
        </ul>
        <h2>{content}</h2>
        Board  
    </body>
</html>
'''


@app.route('/')
def index():
    return template(get_contents(), '<h2>Menu</h2>')


@app.route('/create/', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        content = '''
            <form action="/create/" method="POST">
                <p><input type="text" name="title" placeholder="Title"></p>
                <p><textarea name="content" placeholder="Content"></textarea></p> 
                <p><input type="submit" value="Create"></p>
            </form>
        '''
        return template(get_contents(), content)
    elif request.method == 'POST':
        global nextId
        title = request.form['title']
        content = request.form['content']
        new_post = {'id': nextId, 'title': title, 'content': content}
        posts.append(new_post)
        nextId += 1
        return redirect('/')


@app.route('/read/<int:id>/')
def read(id):
    for post in posts:
        if id == post['id']:
            title = post['title']
            content = post['content']
            return template(get_contents(), f'<h2>{title}</h2>{content}')
    return 'Post not found', 404


@app.route('/update/<int:id>/', methods=['GET', 'POST'])
def update(id):
    if request.method == 'GET':
        for post in posts:
            if id == post['id']:
                title = post['title']
                content = post['content']
                form = f'''
                <form action="/update/{id}/" method="POST">
                    <p><input type="text" name="title" placeholder="Title" value="{title}"></p>
                    <p><textarea name="content" placeholder="Content">{content}</textarea></p>
                    <p><input type="submit" value="Update"></p>
                </form>
                '''
                return template(get_contents(), form)
        return 'Post not found', 404
    elif request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        for post in posts:
            if id == post['id']:
                post['title'] = title
                post['content'] = content
                return redirect('/')
        return 'Post not found', 404


@app.route('/delete/<int:id>/')
def delete(id):
    for i, post in enumerate(posts):
        if id == post['id']:
            del posts[i]
            return redirect('/')
    return 'Post not found', 404


if __name__ == '__main__':
    app.run(port=5001, debug=True)