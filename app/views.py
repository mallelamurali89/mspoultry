from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db.models import ObjectDoesNotExist
from app.models import Expenses
from django.contrib import messages
import babel.numbers

from datetime import datetime,timedelta
from django.utils import timezone

import gspread # for google sheet access



def index(request):
    if request.user.is_anonymous:
        return redirect("/login.html")
    usr_profile = request.session.get('profile', [])
    if request.user.is_authenticated:
        request.session['usr_profile'] = {'name': request.user.username.capitalize()}

    some_day_plus_21 = timezone.now().date() + timedelta(days=21)
    print(timezone.now().date())
    print(some_day_plus_21)

    items = Expenses.objects.all()
    total_expenses = sum(items.values_list('exp_amount', flat=True))
    total_amt_murali = sum(items.filter(author=1).values_list('exp_amount', flat=True))
    total_amt_sri = sum(items.filter(author=2).values_list('exp_amount', flat=True))

    total_amt_pro = "%.2f" % ( sum(items.filter(exp_type='products').values_list('exp_amount', flat=True))/total_expenses*100)
    total_amt_hat = "%.2f" % ( sum(items.filter(exp_type='hatching').values_list('exp_amount', flat=True))/total_expenses*100)
    total_amt_tra = "%.2f" % ( sum(items.filter(exp_type='traveling').values_list('exp_amount', flat=True))/total_expenses*100)
    total_amt_chf = "%.2f" % ( sum(items.filter(exp_type='chick_feed').values_list('exp_amount', flat=True))/total_expenses*100)
    total_amt_gwf = "%.2f" % ( sum(items.filter(exp_type='grower_feed').values_list('exp_amount', flat=True))/total_expenses*100)
    total_amt_lyf = "%.2f" % ( sum(items.filter(exp_type='layer_feed').values_list('exp_amount', flat=True))/total_expenses*100)
    total_amt_med = "%.2f" % ( sum(items.filter(exp_type='medicines').values_list('exp_amount', flat=True))/total_expenses*100)
    total_amt_wrk = "%.2f" % ( sum(items.filter(exp_type='workers').values_list('exp_amount', flat=True))/total_expenses*100)
    total_amt_rnt = "%.2f" % ( sum(items.filter(exp_type='rent').values_list('exp_amount', flat=True))/total_expenses*100)
    total_amt_oth = "%.2f" % ( sum(items.filter(exp_type='others').values_list('exp_amount', flat=True))/total_expenses*100)

    total_exp = babel.numbers.format_currency(total_expenses, 'INR', locale='en_IN')
    # return html(request, "index")
    return render(request,'index.html',{'tot_exp':total_exp,'tot_murali_exp':total_amt_murali/total_expenses*100,'tot_sri_exp':total_amt_sri/total_expenses*100,'pro':total_amt_pro,'hat':total_amt_hat,'tra':total_amt_tra,'chf':total_amt_chf,'gwf':total_amt_gwf,'lyf':total_amt_lyf,'med':total_amt_med,'wrk':total_amt_wrk,'rnt':total_amt_rnt,'oth':total_amt_oth})

def expense(request):
    listofExpenses = Expenses.objects.all()
    # gc = gspread.service_account(filename='./gsheet_credentials.json')
    # sh = gc.open_by_key('1yZYtgxAuSN72Eqz0RXL0Km0VmFXqzbRiUXPljsb1Lsc')
    # sheet_name = request.user.username.capitalize()+" Expenses"
    # worksheet = sh.worksheet(sheet_name)
    # insertRow = ["24/3/23","traveling charges for vijayawada (400 petrol + Tea and Tiffen (30))",430]
    # worksheet.append_row(insertRow)
    if request.user.is_anonymous:
        return redirect("/login.html")
    elif request.method == "POST":
        # if request.POST.get("expType") == 'hatching':
        #     res = [int(i) for i in request.POST.get("expDesc").split() if i.isdigit()]
        #     tot_eggs = res[0]
        #     if tot_eggs > 0:
        #         eggs_sheet = "Eggs Production"
        #         ws = sh.worksheet(eggs_sheet)
        #         eggs_hatching_date = request.POST.get("expDate")
        #         Begindate = datetime.strptime(eggs_hatching_date, "%Y-%m-%d")
        #         eggs_deliver_date = Begindate + timedelta(days=22)
        #         insertRow = [request.POST.get("expDate"),tot_eggs,"",str(eggs_deliver_date.date())]
        #         ws.append_row(insertRow)
        try:
            exp = Expenses()
            exp.author  = request.user
            if request.POST.get("expDate"):
                exp.exp_date = request.POST.get("expDate")
            exp.exp_type  = request.POST.get("expType")
            exp.exp_description  = request.POST.get("expDesc")
            exp.exp_amount  = request.POST.get("expAmount")
            exp.save()

            #update expenses into google sheet - start
            gc = gspread.service_account(filename='./gsheet_credentials.json')
            sh = gc.open_by_key('1yZYtgxAuSN72Eqz0RXL0Km0VmFXqzbRiUXPljsb1Lsc')
            sheet_name = request.user.username.capitalize()+" Expenses"
            worksheet = sh.worksheet(sheet_name)
            insertRow = [request.POST.get("expDate"),request.POST.get("expDesc"),request.POST.get("expAmount")]
            worksheet.append_row(insertRow)
            #update expenses into google sheet - end
            if request.POST.get("expType") == 'hatching':
                res = [int(i) for i in request.POST.get("expDesc").split() if i.isdigit()]
                tot_eggs = res[0]
                if tot_eggs > 0:
                    eggs_sheet = "Eggs Production"
                    ws = sh.worksheet(eggs_sheet)
                    eggs_hatching_date = request.POST.get("expDate")
                    Begindate = datetime.strptime(eggs_hatching_date, "%Y-%m-%d")
                    eggs_deliver_date = Begindate + timedelta(days=22)
                    insertRow = [request.POST.get("expDate"),tot_eggs,"",str(eggs_deliver_date.date())]
                    ws.append_row(insertRow)
            messages.success(request,"Added successfully")
        except Exception:
            messages.error(request,"Getting error")

    return render(request,'expense.html',{'listofexp':listofExpenses})


def html(request, filename):
    context = {"filename": filename,
               "collapse": ""}
    if request.user.is_anonymous and filename != "login":
        return redirect("/login.html")
    if filename == "logout":
        logout(request)
        return redirect("/")
    if filename == "login" and request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            if "@" in username:
                user = User.objects.get(email=username)
            else:
                user = User.objects.get(username=username)
            user = authenticate(request, username=user.username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                context["error"] = "Wrong password"
        except ObjectDoesNotExist:
            context["error"] = "User not found"

        print("login")
        print(username, password)
    print(filename, request.method)
    if filename in ["buttons", "cards"]:
        context["collapse"] = "components"
    if filename in ["utilities-color", "utilities-border", "utilities-animation", "utilities-other"]:
        context["collapse"] = "utilities"
    if filename in ["404", "blank"]:
        context["collapse"] = "pages"

    return render(request, f"{filename}.html", context=context)
