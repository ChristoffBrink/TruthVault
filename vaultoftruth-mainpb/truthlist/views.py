from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
import pandas as pd
from django.contrib import messages
import random
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import json
from .models import *
from reportlab.pdfgen import canvas
import datetime





# Create your views here.

def home(request):
    return render(request,'truthlist/home.html')

@login_required(login_url='login')
def upload(request):
    if request.method == 'POST':
        file = request.FILES['file']
        # read the excel file
        df = pd.read_excel(file)
        # check the second column name is question
        if df.columns[1].lower() != 'question':
            messages.error(request, "The second column name should be Question")
            return redirect('upload')
        # check the third column name is category
        if df.columns[2].lower() != 'category':
            messages.error(request, "The third column name should be Category")
            return redirect('upload')
        # check the fourth column name is fundamentals
        if df.columns[3].lower() != 'fundamentals':
            messages.error(request, "The fourth column name should be Fundamentals")
            return redirect('upload')
        # convert the dataframe into list
        df = df.values.tolist()
        for row in df:
            q = Question.objects.get_or_create(question=row[1])[0]
            q.category = Category.objects.get_or_create(name=row[2])[0] if row[2] else None
            q.is_fundamental = True if row[3] and row[3].lower() == 'yes' else False
            q.active = True
            q.save()

        messages.success(request, "Questions uploaded successfully")

    return render(request, 'truthlist/upload.html')


@login_required(login_url='login')
def profile(request):
    questions = UserAnswer.objects.filter(user=request.user)
    return render(request, 'truthlist/profile.html', {'questions': questions})


@login_required(login_url='login')
def assessment(request):
    questions = Question.objects.filter(active=True)
    if request.method == 'POST':
        for q in questions:
            answer = request.POST.get(str(q.id))
            if answer:
                ua = UserAnswer.objects.get_or_create(user=request.user, question=q)[0]
                ua.answer = answer
                ua.save()
        
        return redirect('profile')
    return render(request, 'truthlist/assessment.html', {'questions': questions})


@login_required(login_url='login')
def add_to_certificate(request, id, value):
    ua = UserAnswer.objects.get(id=id)
    if value == 'true':
        ua.add_to_certificate = True
    else:
        ua.add_to_certificate = False
    ua.save()
    return redirect('profile')


@login_required(login_url='login')
def add_new_question(request):
    if request.method == 'POST':
        question = request.POST.get('question')
        category = request.POST.get('category')
        is_fundamental = True if request.POST.get('is_fundamental') == 'on' else False
        if question:
            q = Question.objects.get_or_create(question=question)[0]
            q.category = Category.objects.get(id=category) if category else None
            q.is_fundamental = is_fundamental
            q.save()
            messages.success(request, "Question added successfully")
            return redirect('add_new_question')
        else:
            messages.error(request, "Question is required")
            return redirect('add_new_question')
    
    categories = Category.objects.all()
    return render(request, 'truthlist/add_new_question.html', {'categories': categories})


@login_required(login_url='login')
def pending_questions(request):
    questions = Question.objects.filter(active=False)
    return render(request, 'truthlist/pending_questions.html', {'questions': questions})


@login_required(login_url='login')
def approve_question(request, id):
    q = Question.objects.get(id=id)
    q.active = True
    q.save()
    return redirect('pending_questions')


@login_required(login_url='login')
def reject_question(request, id):
    q = Question.objects.get(id=id)
    q.delete()
    return redirect('pending_questions')


def public_believes(request):
    ua = UserAnswer.objects.all()
    return render(request, 'truthlist/public_believes.html', {'user_answer': ua})


def reasons(request, id):
    if request.method == 'POST':
        reason = request.POST.get('reason')
        file = request.FILES.get('file')
        if reason:
            r = Reason.objects.create(
                user=request.user,
                question=Question.objects.get(id=id),
                reason=reason,
                file=file if file else None
            )
            r.save()
            messages.success(request, "Reason added successfully")
    question = Question.objects.get(id=id)
    all_reasons = Reason.objects.filter(question=question)
    all_comments = Comment.objects.filter(question=question)
    return render(request, 'truthlist/reasons.html', {'question': question, 'reasons': all_reasons, 'comments': all_comments})


@login_required(login_url='login')
def add_comment(request, id):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        file = request.FILES.get('file')
        if comment:
            c = Comment.objects.create(
                user=request.user,
                question=Question.objects.get(id=id),
                comment=comment
            )
            if file:
                c.file = file
            c.save()
            messages.success(request, "Comment added successfully")
            return redirect('reasons', id=id)

@login_required(login_url='login')
def delete_comment(request, id):
    c = Comment.objects.get(id=id)
    c.delete()
    return redirect('reasons', id=c.question.id)


@login_required(login_url='login')
def update_believes(request, id):
    if request.method == 'POST':
        question = Question.objects.get(id=id)
        update_believe = request.POST.get('update_believe')
        if update_believe:
            ub = UpdateBelieve.objects.get_or_create(
                user=request.user,
                question=question,
                believe=update_believe
            )[0]
            ub.save()
            return render(request, 'truthlist/assessment.html', {'questions': [question]})
        



@login_required(login_url='login')
def download_certificate(request):
    questions = UserAnswer.objects.filter(user=request.user, add_to_certificate=True)
    if request.method == 'POST':
        if questions:
            # make a PDF certificate. keep user full name, email, date, questions and answers
            user = request.user
            full_name = user.first_name + ' ' + user.last_name
            email = user.email
            date = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="certificate.pdf"'
            p = canvas.Canvas(response)
            # text center with large font size
            p.setFont('Helvetica-Bold', 20)
            p.drawCentredString(300, 800, 'Certificate of Truth')
            p.setFont('Helvetica', 12)
            p.drawString(100, 770, 'Name: ' + full_name)
            p.drawString(100, 750, 'Email: ' + email)
            y = 700
            for q in questions:
                p.drawString(100, y, 'Question: ' + q.question.question)
                answer = q.answer
                if answer == 'agree':
                    answer = 'Agree'
                elif answer == 'disagree':
                    answer = 'Disagree'
                else:
                    answer = 'No comment'
                p.drawString(100, y-20, 'Answer: ' + answer)
                y -= 50
                if y < 100:
                    p.showPage()
                    y = 700
            p.showPage()
            p.save()
            return response
        else:
            messages.error(request, "No questions found")
            return redirect('download_certificate')
    return render(request, 'truthlist/download_certificate.html', {'questions': questions})


@login_required(login_url='login')
def reasons_opinion(request, id):
    if request.method == 'POST':
        reason_opinion = request.POST.get(str(id))
        reason = Reason.objects.get(id=id)
        print(reason_opinion, reason)
        if reason:
            ra = ReasonAnswer.objects.get_or_create(
                user=request.user,
                reason=reason,
                answer=reason_opinion
            )[0]
            ra.save()
            messages.success(request, "Reason opinion added successfully")
    
    return redirect(request.META['HTTP_REFERER'])


@login_required(login_url='login')
def category(request):
    categories = Category.objects.all()
    return render(request, 'truthlist/category.html', {'categories': categories})

@login_required(login_url='login')
def category_question(request, id):
    questions = Question.objects.filter(active=True, category=Category.objects.get(id=id))
    return render(request, 'truthlist/assessment.html', {'questions': questions})



def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            messages.success(request, "Logged in successfully")
            return redirect("home")
        else:
            # No backend authenticated the credentials
            messages.error(request, "Invalid Credentials")
            return render(request, "truthlist/login.html")
    return render(request, "truthlist/login.html")

def logout_view(request):
    logout(request)
    return render(request, "truthlist/login.html")

def register(request):
    if request.method == "POST":
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirmpassword = request.POST.get("confirmpassword")
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return render(request, "truthlist/register.html")
        if len(password) < 8:
            messages.error(request, "Password must be atleast 8 characters long")
            return render(request, "truthlist/register.html")
        if password != confirmpassword:
            messages.error(request, "Passwords do not match")
            return render(request, "truthlist/register.html")
        
        user = User.objects.create_user(email, email, password)
        user.first_name = firstname
        user.last_name = lastname
        user.save()
        messages.success(request, "Account created successfully")
        return render(request, "truthlist/login.html")
        
    return render(request, "truthlist/register.html")