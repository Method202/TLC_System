from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# This is the change you need to make
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # You would handle the login logic here
        # For now, let's just get the role
        role = request.form.get('role')
        
        # Redirect based on the role
        if role == 'student':
            return redirect(url_for('student_dashboard'))
        elif role == 'lecturer':
            return redirect(url_for('lecturer_dashboard'))
        elif role == 'admin':
            return redirect(url_for('admin_dashboard'))
    
    return render_template('login.html')

# Other dashboard routes
@app.route('/student_dashboard')
def student_dashboard():
    return render_template('studentdash.html')

@app.route('/lecturer_dashboard')
def lecturer_dashboard():
    return render_template('lecturerdash.html')

@app.route('/admin_dashboard')
def admin_dashboard():
    return render_template('admindash.html')

@app.route('/user_profile')
def user_profile():
    return render_template('profile.html')

@app.route('/admin_students')
def admin_students():
    return render_template('admstd.html')

@app.route('/admin_lecturers')
def admin_lecturers():
    return render_template('admlec.html')

@app.route('/admin_courses')
def admin_courses():
    return render_template('admcourse.html')

if __name__ == '__main__':
    app.run(debug=True)