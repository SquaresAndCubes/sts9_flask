from flask import Flask, render_template
app = Flask(__name__,)

@app.route('/')
@app.route('/<name>')
def hello_name(name=None):
    return render_template('hello.html', name=name)

@app.route('/layout')
def layout_page():
    return render_template('layout.html')

@app.route('/child')
def child():
    return render_template('child.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run()
