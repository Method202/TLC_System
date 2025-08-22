from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('admindash.html')  # Change to the template you want

if __name__ == '__main__':
    app.run(debug=True)