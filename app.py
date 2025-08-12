from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        # Process data 
        flash('Thank you for your message! I will contact you soon.', 'success')
        return redirect(url_for('home'))
    
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)