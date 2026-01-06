from django.shortcuts import render, redirect
from .models import Users, Transactions, Transactionstatus, Ledgerentries, Auditlog, Accounts
from django.contrib.auth.models import User
from django.utils import timezone # for storing time related fields
from django.db import transaction, IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import random

# initialisation views : Login, Logout and Register
from django.db import IntegrityError

def register_user(request):
    if request.method == 'POST':
        details = request.POST
        name = details.get('name')
        email = details.get('email')
        password = details.get('password')
        cpassword = details.get('cpassword')
        phone = details.get('phone')

        # 1. Validation Logic (Catching errors before they hit the DB)
        if password != cpassword:
            return render(request, 'base/register.html', {'error': "Access Keys do not match."})
        
        if len(phone) != 10:
            return render(request, 'base/register.html', {'error': "Invalid Phone Format. 10 digits required."})

        try:
            with transaction.atomic():
                # 1. Create Digital Profile
                auth_user = User.objects.create_user(
                    username=email,
                    email=email,
                    password=password
                )

                # 2. Create Banking Profile (Using your custom 'Users' model)
                Users.objects.create(
                    auth_user=auth_user,
                    name=name,
                    email=email,
                    phone=phone,
                    status='ACTIVE',
                    createdate=timezone.now(),
                )

            messages.success(request, "Account created successfully!")
            return redirect('login')

        except IntegrityError:
            # Catch duplicate email/phone specifically
            return render(request, 'base/register.html', {'error': "Identity Conflict: Email or Phone already registered."})
        except Exception as e:
            # Catch-all for unexpected system issues
            return render(request, 'base/register.html', {'error': f"Engine Fault: {str(e)}"})
        
    return render(request, 'base/register.html')


def login_user(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')

        user = authenticate(request, username=u, password=p)

        if user is not None:
            login(request, user)
            messages.success(request, "Loggedin Successfully!")
            return redirect('home')
        else:
            return render(request, 'base/login.html', {'error': "Invalid AUTH_KEY or AUTH_ID."})
        
    return render(request, 'base/login.html')


def logout_user(request):
    logout(request)
    messages.success(request, 'Loggedout Successfully!')
    return redirect('login')


# base/home page view :
def home(request):
    accounts = Accounts.objects.filter(userid = request.user.users)
    context = {
        'accounts' : accounts
    }
    return render(request, 'base/home.html', context)

# view for opening new account ->
def new_account(request):
    if request.method == 'POST':
        accType = request.POST.get('account_type')
        initial_balance = request.POST.get('initial_balance')

        while True :
            generated_acc_no = str(random.randint(1000000000, 9999999999))
            if not Accounts.objects.filter(accountnumber=generated_acc_no).exists():
                break
        
        try:
            with transaction.atomic(): # start transaction to insert into the 'accounts' table
                new_account = Accounts.objects.create(
                    userid = request.user.users,
                    accountnumber = generated_acc_no,
                    accounttype = accType,
                    balance = initial_balance,
                    status = 'ACTIVE',
                    createdate = timezone.now(),
                )

                messages.success(request, 'account created successfully!')
                messages.success(request, f"Account {generated_acc_no} is now ACTIVE.")
                return redirect('home')
        except Exception as e:
            messages.error(request, f"Provising error : {str(e)}")

    return render(request, 'base/new_account.html')

# view for performing a transaction ->
def transfer(request):
    return render(request, 'base/transfer.html')

# view for retrieving bank statements ->
def statements(request):
    return render(request, 'base/statements.html')

def deactivate_account(request, pk):
    return render(request, 'base/deactivate_account.html')
