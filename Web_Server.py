from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Ensure you create 'index.html' in a 'templates' folder

if __name__ == '__main__':
    app.run(debug=True)

git config --global user.email "you@example.com"
  git config --global user.name "Your Name"