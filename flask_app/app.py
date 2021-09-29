# python -m textblob.download_corpora
from flask import Flask, render_template,request,url_for
from flask_bootstrap import Bootstrap
from textblob import TextBlob
from textblob import Word
from textblob.blob import WordList


app = Flask(__name__)
Bootstrap(app)

@app.route('/',methods=['GET','POST'])
def definitions():
    df=['Word definition']
    if request.method == 'POST':
        data= request.form.get('word')
        if len(Word(data).definitions)>=1:
            df=Word(data).definitions
        else:
            df=['word is not in dictionary']


    return render_template('definitions.html',definitions=df)


if __name__ == '__main__':
	app.run(debug=True)


