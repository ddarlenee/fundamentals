from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
  if request.method == "POST":
    msg = request.form['message']
    with open('messages.txt', 'a') as file:
      file.write(msg + "\n")
    render_template('index.html', message=msg)
  # this is for get
  with open('messages.txt', 'r') as file:
    posts = file.readlines()
  return render_template('index.html', posts=posts)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)
