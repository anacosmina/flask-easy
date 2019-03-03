from flask import Flask, render_template, request
from graph import build_graph
from werkzeug import secure_filename
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static'

def factors(num):
  return [x for x in range(1, num+1) if num%x==0]

@app.route("/")
def main():
    return "Welcome!"

@app.route('/test')
def testing():
    return 'test'

@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello '+ name + '!'

@app.route('/square/<int:num>')
def f(num):
    # No conversion of x needed.
    return str(num**2)

@app.route('/factors/<int:n>')
def factors_display(n):
    return render_template("factors.html", number=n, factors=factors(n))

def factors_route(n):
    return "The factors of {} are {}".format(num, factors(num))

@app.route('/graphs')
def graphs():
    x1 = [0, 1, 2, 3, 4]
    y1 = [10, 30, 40, 5, 50]
    x2 = [0, 1, 2, 3, 4]
    y2 = [50, 30, 20, 10, 50]
 
    graph1_url = build_graph(x1,y1)
    graph2_url = build_graph(x2,y2)
 
    return render_template('graphs.html', graph1=graph1_url, graph2=graph2_url)

@app.route('/upload')
def upload_file():
    return render_template('upload.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def uploader_file():
    if request.method == 'POST':
        f = request.files['file']
        full_filename = os.path.join('static', secure_filename(f.filename))
        f.save(full_filename)
        return render_template("picture.html", user_image = full_filename)


if __name__ == "__main__":
    app.run()
