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
    return render_template('dashboard_student.html')

@app.route('/lecturer_dashboard')
def lecturer_dashboard():
    return render_template('dashboard_lecturer.html')

@app.route('/admin_dashboard')
def admin_dashboard():
    return render_template('dashboard_admin.html')

#Admin sidebar
@app.route('/admin_students')
def admin_students():
    return render_template('student.html')

@app.route('/admin_lecturers')
def admin_lecturers():
    return render_template('lecturer.html')

@app.route('/admin_courses')
def admin_courses():
    return render_template('course.html')

@app.route('/admin_programs')
def admin_programs():
    return render_template('program.html')

@app.route('/admin_results')
def admin_results():
    return render_template('result.html')

@app.route('/admin_assessments')
def admin_assessments():
    return render_template('assessment.html')

@app.route('/admin_payments')
def admin_payments():
    return render_template('payment.html')

@app.route('/admin_accommodations')
def admin_accommodations():
    return render_template('accommodation.html')

@app.route('/admin_settings')
def admin_settings():
    return render_template('setting.html')

#Profiles routes
@app.route('/admin_profile')
def admin_profile():
    return render_template('profile_admin.html')

@app.route('/lecturer_profile')
def lecturer_profile():
    return render_template('profile_lecturer.html')

@app.route('/student_profile')
def student_profile():
    return render_template('profile_student.html')

@app.route('/user_profile')
def user_profile():
    return render_template('profile.html')

#Registering pages
@app.route('/register_lecturer')
def register_lecturer():
    return render_template('lecturer_registration.html')

@app.route('/register_student')
def register_student():
    return render_template('student_registration.html')

if __name__ == '__main__':
    app.run(debug=True)