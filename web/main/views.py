from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import loginForm, SendValentineForm, SendAnswerForm
from .models import User, ValentineMessage

def index(request):
    login = request.session.get('login')
    if login:
        return redirect('home')
    else:
        return redirect('login')
    
    
def home(request):
    login = request.session.get('login')
    received = ValentineMessage.objects.all().filter(recipient_name=login)
    
    if not login:
        return redirect('login')
    
    if request.method == 'POST':
        form = SendValentineForm(request.POST)
 
        if form.is_valid():
            recipient = form.cleaned_data['recipient']
            
            if User.objects.all().filter(login=recipient):
                message = ValentineMessage()
                
                message.sender = User.objects.get(login=login)
                message.question = form.cleaned_data['message']
                message.recipient_name = recipient
                
                message.save()
                
                return redirect('home')
            else:
                form.add_error('recipient', 'User does not exist')
    else:
        form = SendValentineForm()
        
    return render(request, 'home.html', {'user': login, 'form': form, 'received': received})


def login(request):
    login = request.session.get('login')
    
    if request.method == 'POST':
        form = loginForm(request.POST)
        
        if form.is_valid():
            try:
                user = User()
                user.login = form.cleaned_data['login']
                
                user.save()
                username = user.login
            except Exception:
                username = form.cleaned_data['login']
                
            request.session['login'] = username
            return redirect('home')
    else:
        form = loginForm()
    return render(request, 'login.html', {'form': form, 'user':login})


def logout_session(request):
    logout(request)
    return redirect('home')


def messages(request):
    login = request.session.get('login')
    if not login:
        return redirect('login')
    
    received = ValentineMessage.objects.all().filter(recipient_name=login)
    sended = ValentineMessage.objects.all().filter(sender__login=login)
    
    return render(request, 'messages.html', {'messages': received, 'sended':sended, 'user': login})


def answer(request, mess_id):
    login = request.session.get('login')
    message = ValentineMessage.objects.get(id=mess_id)
    
    if request.method == 'POST':
        form = SendAnswerForm(request.POST)
        if form.is_valid(): 
            message.answer = form.cleaned_data['answer']
            
            message.save()
            return redirect('messages')
    else:
        form = SendAnswerForm()    
        
    return render(request, 'answer.html', {'user': login, 'form': form, 'message': message})
    