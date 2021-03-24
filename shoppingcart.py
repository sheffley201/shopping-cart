from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def shop():
   return render_template('main.html')

@app.route('/cart',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("cart.html",result = result)

if __name__ == '__main__':
   app.run(debug = True)