from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User, Token, Expense, Incom
from datetime import datetime
from json import JSONEncoder

# Create your views here.



@csrf_exempt
def submit_incom(request):
    """ user submits an incom """

    # TODO; validate data. user might be fake. token be fake, amount might be ...

    this_token = request.POST['token']
    this_user = User.objects.filter(token__token=this_token).get()
    if 'date' not in request.POST:
        date = datetime.now()  # TODO: user might want to submit the date herself
    Incom.objects.create(user=this_user, amount=request.POST['amount'],
                           title=request.POST['tittle'], date=date)

    return JsonResponse({
        "Status": "OK"
    }, encoder=JSONEncoder)





@csrf_exempt
def submit_expense(request):
    """ user submits an expense """
    # TODO; validate data. user might be fake. token be fake, amount might be ...

    this_token = request.POST['token']
    this_user = User.objects.filter(token__token=this_token).get()
    if 'date' not in request.POST:
        date = datetime.now()  # TODO: user might want to submit the date herself
    Expense.objects.create(user=this_user, amount=request.POST['amount'],
                           title=request.POST['tittle'], date=date)

    return JsonResponse({
        "Status": "OK"
    }, encoder=JSONEncoder)
