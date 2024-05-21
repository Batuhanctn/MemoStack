
from flask import Flask,render_template,request,redirect,url_for
from db import Firebase
from user import User
from note import Note


if __name__ == "__main__":
    app = Flask(__name__) 
    f=Firebase()
           
    @app.route('/')
    def main():
            return render_template("anasayfa.html")

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
        # Form verilerini işleyin
            mail = request.form['mail']
            password = request.form['password']
            try:
                f.login(mail, password)
                user = User(f.get_user_id(), f)
                user.save()
                return redirect(url_for('userpage',user_id=f.get_user_id()))
                
            except Exception as e:
                return render_template("login.html", error="Invalid User Information!")
        return render_template("login.html")
    
    @app.route('/signup', methods=['GET', 'POST'])
    def signup():
        if request.method == 'POST':
            password = request.form['password']
            mail = request.form['mail']
            username= request.form['username']
            f.register(mail,password)
            f.login(mail, password)
            user = User(f.get_user_id(), f)
            user.save()
            user.update(
        {
            "username": username,
        }
    )
            return redirect(url_for('userpage',user_id=f.get_user_id()))
                
        return render_template("signup.html")
    
    @app.route('/information/<user_id>', methods=['GET', 'POST'])
    def information(user_id):
        user = User(user_id, f)
        user_data = user.get()
        if request.method == 'POST':
            fullname = request.form['fullname']
            university = request.form['university']
            department= request.form['department']
            user = User(f.get_user_id(), f)
            user.update(
        {
            "fullname": fullname,
            "university": university,
            "department": department,
            
        }
    )
            return render_template("userpage.html",user_data=user_data)
        return render_template("information.html",user_data=user_data)
    
    @app.route('/userpage/<user_id>', methods=['GET', 'POST'])
    def userpage(user_id):
        user = User(user_id, f)
        user_data = user.get()
        return render_template("userpage.html", user_data=user_data)
    
    
    app.run(debug=True,port=5500)