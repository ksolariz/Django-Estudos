from turtle import forward
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound, HttpResponseRedirect

# Create your views here.

monthly_challenges = {
    "january": "This works",
    "february": "meczada",
    "march": "pogger"
}

def monthly_challenge_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    
    redirect_month = months[month - 1]
    return HttpResponseRedirect("/challenges/" + redirect_month)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported!")
   
    
