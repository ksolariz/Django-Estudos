from turtle import forward
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

monthly_challenges = {
    "january": "This works",
    "february": "meczada",
    "march": "pogger"
}

def index(request):

    list_items = ""
    months = list(monthly_challenges.keys())
    month_path = reverse("month-challenge", args=[months])
    return render(request,"challenges/index.html",{
        "months": months,
        "month_path": month_path
    })

def monthly_challenge_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    
    redirect_month = months[month - 1]
    #com o reverse ele redireciona de forma dinamica invés de ser o caminho hard-coded
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request,"challenges/challenge.html", {
            "text": challenge_text,
            "month": month
        })
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
   
    
