from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "Eating more foods",
    "march": "Walk and run in this month",
    "december": None,
}

# Create your views here.


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    # for month in months:
    #     capatalized_month = month.capitalize()
    #     list_items += f"""
    #         <li><a href="{reverse('month-challenge', args=[month])}"><h1>{capatalized_month}</h1></a></li>
    #     """
    # response_data = f"""

    #     <ul>
    #         {list_items}
    #     </ul>

    # """
    # return HttpResponse(response_data)
    return render(request, "challenges/index.html", {
        "months": months,
    })


def monthlyChallangeByNumber(request, month):
    monthName = ""
    if month == 0:
        month = 1
    try:
        monthName = list(monthly_challenges.keys())[month - 1]
    except:
        return HttpResponseNotFound("Entered month number is not correct")
    redirect_url = reverse("month-challenge", args=[monthName])
    return HttpResponseRedirect(redirect_url)


def monthlyChange(request, month):
    challengeText = ""
    try:
        challengeText = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {"challengeText": challengeText,
                                                             "month": month.capitalize()})
    except KeyError:
        return HttpResponseNotFound(f"<h1>Page not found: \"{month}\"</h1>")
