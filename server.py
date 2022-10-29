from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = 'secrets secrets are no fun...'

@app.route('/')
def hello_world():
    return render_template('form.html')

@app.route('/result', methods=['POST'])
def result():
    print(request.form)
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['fav_language'] = request.form['fav_language']
    session['comments'] = request.form['comments']
    print(session['name'])
    return render_template('result.html')

if __name__=="__main__":
    app.run(debug=True)