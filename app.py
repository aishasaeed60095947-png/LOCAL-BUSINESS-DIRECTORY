import os
from flask import Flask, render_template, request, redirect, url_for
from models import Business, BusinessStack

app = Flask(__name__)

# Mock database
businesses = []
recent_businesses = BusinessStack()

@app.route('/')
def index():
    # Pass all businesses and the stack history (top 5) to the template
    recent_list = recent_businesses.get_recent(5)
    return render_template('index.html', businesses=businesses, recent=recent_list)

@app.route('/add', methods=['GET', 'POST'])
def add_business():
    if request.method == 'POST':
        name = request.form.get('name')
        category = request.form.get('category')
        description = request.form.get('description', '')
        
        if name and category:
            new_biz = Business(name, category, description)
            businesses.append(new_biz)
            recent_businesses.push(new_biz)
            return redirect(url_for('index'))
            
    return render_template('add_business.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
