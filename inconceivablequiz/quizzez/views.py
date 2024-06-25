from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.http import HttpResponse
from .models import Quiz, Question

#==========================start screen=============================
class Home(LoginView):
    template_name = 'home.html'

class Login(LoginView):
    template_name = 'login.html'

def signup(req):
    error_message = ''
    if req.method == 'POST':
        form = UserCreationForm(req.POST)
        if form.is_valid():
            user = form.save()
            login(req, user)
            return redirect('login')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(req, 'signup.html', context)

def menu(req):
    return render(req, 'menu.html')

def instructions(req):
    return HttpResponse("instructions page")

#==========================quiz creation=============================
@login_required
def quiz_index(req):
    quizs = Quiz.objects.filter(user=req.user) 
    return render(req, 'quizs/index.html', {'quizs': quizs})

@login_required
def quiz_detail(request, quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
    return render(request, 'quizs/detail.html', {
        'quiz': quiz, 
    })

class QuizCreate(LoginRequiredMixin, CreateView):
    model = Quiz
    fields = ['name','description']
    success_url = '/quizzes/'
    def form_valid(self, form):
        # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user  # form.instance is the quiz
        # Let the CreateView do its job as usual
        return super().form_valid(form)

class quizUpdate(LoginRequiredMixin, UpdateView):
    model = Quiz
    fields = ['name','description']

class quizDelete(LoginRequiredMixin, DeleteView):
    model = Quiz
    success_url = '/quizzes/'

#==========================question creations=============================

class QuestionList(LoginRequiredMixin, ListView):
    model = Question

class QuestionDetail(LoginRequiredMixin, DetailView):
    model = Question

class QuestionCreate(LoginRequiredMixin, CreateView):
    model = Question
    fields = '__all__'

class QuestionUpdate(LoginRequiredMixin, UpdateView):
    model = Question
    fields = ['name']

class QuestionDelete(LoginRequiredMixin, DeleteView):
    model = Question
    success_url = '/toys/'