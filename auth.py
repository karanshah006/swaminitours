from flask import Blueprint, render_template, flash, request, redirect, url_for 
from .models import User, Bookingdetails
from . import db
from flask_login import login_user, login_required ,logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

auth=Blueprint('auth',__name__)

@auth.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged In Successfully!',category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist',category='error')

    return render_template("login.html",user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/About_Us')
def About_Us():
    return render_template("about_us.html",user=current_user)

@auth.route('/Home' )
def home():
   return render_template("home.html",user=current_user)

@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
    if request.method=='POST':
        email=request.form.get('email')
        firstname=request.form.get('firstname')
        password1=request.form.get('password1')
        password2=request.form.get('password2')

        user = User.query.filter_by(email=email).first()

        if user:
            flash('Email already exists',category='error')
        elif len(email)<4:
         flash("Email must be greater than 4 characters.",category='error')
        elif len(firstname)<2:
            flash("First name must be greater than 2 characters.",category='error')
        elif password1!=password2:
             flash("Password don\'t match.",category='error')
        elif len(password1)<7:
             flash("Password must be at least 6 characters.",category='Error')
        else:
            new_user = User(email=email, firstname=firstname, password=generate_password_hash(
                password1, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            flash("Account Created!",category='Success')    
            return redirect(url_for('views.home',user=current_user))    
    
    return render_template("sign_up.html",user=current_user)

@auth.route('/info1')
def info1():
    return render_template("/info1.html",user=current_user)

@auth.route('/info2')
def info2():
    return render_template("/info2.html",user=current_user)

@auth.route('/info3')
def info3():
    return render_template("/info3.html",user=current_user)

@auth.route('/info4')
def info4():
    return render_template("/info4.html",user=current_user)

@auth.route('/info5')
def info5():
    return render_template("/info5.html",user=current_user)

@auth.route('/info6')
def info6():
    return render_template("/info6.html",user=current_user)

@auth.route('/info7')
def info7():
    return render_template("/info7.html",user=current_user)

@auth.route('/info8')
def info8():
    return render_template("/info8.html",user=current_user)

@auth.route('/info9')
def info9():
    return render_template("/info9.html",user=current_user)

@auth.route('/info10')
def info10():
    return render_template("/info10.html",user=current_user)

@auth.route('/info11')
def info11():
    return render_template("/info11.html",user=current_user)

# Accepting Data from Form here
@auth.route('/booking_form',methods=['GET','POST'])
def form():
    if request.method=='POST':
        bookingdate=request.form.get('bookingdate')
        bookingtime=request.form.get('bookingtime')
        destination=request.form.get('destination')
        phoneno=request.form.get('phoneno')

        
        new_booking = Bookingdetails(bookingdate=bookingdate, bookingtime=bookingtime, destination=destination, phoneno=phoneno, user=current_user)
        db.session.add(new_booking)
        db.session.commit()
        flash("Booking Reserved!",category='Success')    
        return redirect(url_for('auth.booking_details'))  

    return render_template("booking_form.html",user=current_user)

# Showing Database here
@auth.route('/booking_details',methods=['GET', 'POST'])
def booking_details():
    return render_template("/booking_details.html",user=current_user)

# @auth.route('/index',methods=['GET', 'POST'])
# def index():
#     data=request.form
#     print(data)
#     return render_template("/index.html")