from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template("main.html")

@app.route('/one')
def page_one():
    return render_template("one.html")

@app.route('/two')
def page_two():
    return render_template("two.html")

@app.route('/three')
def page_three():
    return render_template("three.html")

if __name__ == "__main__":
    app.run(debug=True)
