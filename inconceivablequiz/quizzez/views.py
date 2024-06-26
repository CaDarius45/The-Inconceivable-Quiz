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
from .forms import UserUpdateForm

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

def user_profile(req):
    return render(req, 'profile.html')

@login_required
def profile_update(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('user-profile')  # Replace 'profile' with your actual profile view name or URL
    else:
        form = UserUpdateForm(instance=request.user)
    
    return render(request, 'profile_update.html', {'form': form})

def instructions(req):
    return HttpResponse("instructions page")

@login_required
def comunity(req):
    quizs = Quiz.objects.all()
    return render(req, 'comunity.html', {'quizs': quizs})

#==========================quiz creation=============================
@login_required
def quiz_index(req):
    quizs = Quiz.objects.filter(user=req.user) 
    return render(req, 'quizs/index.html', {'quizs': quizs})

@login_required
def quiz_detail(request, quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
    not_question = Question.objects.exclude(id__in = quiz.questions.all().values_list('id'))
    return render(request, 'quizs/detail.html', {
        'quiz': quiz, 
        'questions':not_question
    })

@login_required
def play_quiz(request, quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
    total_questions = quiz.questions.count()
    return render(request, 'play_quiz.html', {
        'quiz': quiz, 
        'total': total_questions,
    })

class QuizCreate(LoginRequiredMixin, CreateView):
    model = Quiz
    fields = ['name','description']
    success_url = '/quizzes'
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
    success_url = '/quizzes'

#==========================question creations=============================
# def add_question(req, quiz_id):
#     # create a ModelForm instance using the data in request.POST
#     form = QuestionForm(req.POST)
#     # validate the form
#     if form.is_valid():
#         # don't save the form to the db until it
#         # has the cat_id assigned
#         new_question = form.save(commit=False)
#         new_question.quiz_id = quiz_id
#         new_question.save()
#     return redirect('quiz-detail', quiz_id=quiz_id)

def add_question(req, quiz_id, question_id):
    Quiz.objects.get(id=quiz_id).questions.add(question_id)
    return redirect('quiz-detail', quiz_id=quiz_id)

def remove_question(req, quiz_id, question_id):
    Quiz.objects.get(id=quiz_id).questions.remove(question_id)
    return redirect('quiz-detail', quiz_id=quiz_id)

class QuestionList(LoginRequiredMixin, ListView):
    model = Question

class QuestionDetail(LoginRequiredMixin, DetailView):
    model = Question

class QuestionCreate(LoginRequiredMixin, CreateView):
    model = Question
    fields = '__all__'

class QuestionUpdate(LoginRequiredMixin, UpdateView):
    model = Question
    fields = ['name', 'opt_1', 'opt_2', 'opt_3', 'opt_4']

class QuestionDelete(LoginRequiredMixin, DeleteView):
    model = Question
    success_url = '/questions'