from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('indexnew.html')

@app.route('/boardnew.html')
def recommend():
   return render_template('boardnew.html')

@app.route('/indexnew.html')
def indexnew():
   return render_template('indexnew.html')

@app.route('/introduce_member.html')
def introduce():
   return render_template('introduce_member.html')

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)
