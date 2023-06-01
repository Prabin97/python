from flask import Flask,render_template
new=Flask(__name__)
@new.route('/')
def home():
    return render_template('welcom.html')
@new.route('/regform')
def resign():
    return render_template('regform.html')
if __name__ == '__main__':
    
    new.run()