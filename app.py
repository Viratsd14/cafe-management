from flask import Flask, render_template

app = Flask(__name__)

# Home page route
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index.html')
def ind():
    return render_template('index.html')


# About Us page route
@app.route('/aboutus.html')
def aboutus():
    return render_template('aboutus.html')

# Location page route (your existing location.html)
@app.route('/location.html')
def location():
    return render_template('location.html')

# Cookbook page route (your existing cookbook.html)
@app.route('/cookbook.html')
def cookbook():
    return render_template('cookbook.html')

# Cart page route (your existing cart.html)
@app.route('/cart.html')
def cart():
    return render_template('cart.html')


@app.route('/feedback.html')
def feedback():
    return render_template('feedback.html')

@app.route('/offer.html')
def offer():
    return render_template('offer.html')

@app.route('/thanks.html')
def thanks():
    return render_template('thanks.html')

if __name__ == '__main__':
    app.run(debug=True)
