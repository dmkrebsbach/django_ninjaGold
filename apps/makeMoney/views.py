from django.shortcuts import render, redirect
import random

def index(request):
    if 'totalGold' not in request.session:
        request.session['totalGold'] = 0
    if 'activity' not in request.session:
        request.session['activity'] = []
    if 'colors' not in request.session:
        request.session['colors'] = []

    return render(request, 'makeMoney/index.html')

def process_money(request):

    if request.method == "POST":
        if request.POST['location'] == 'Farm':
            random_number = random.randint(10, 20)
            request.session["activity"].insert(0, "You found " + str(random_number) + " gold coins on a " + request.POST['location'])
        
        if request.POST['location'] == 'Cave':
            random_number = random.randint(5,10)
            request.session["activity"].insert(0,"You found " + str(random_number) + " gold coins a " + request.POST['location'])
        
        if request.POST['location'] == 'House':
            random_number = random.randint(2,5)
            request.session["activity"].insert(0,"You found " + str(random_number) + " gold coins in your " + request.POST['location'])
        
        if request.POST['location'] == 'Casino':
            random_number = random.randint(-50,50)
            if random_number > 0:
                request.session["activity"].insert(0,"You won " + str(random_number) + " gold coins in the " + request.POST['location'])
            else:
                request.session["activity"].insert(0,"You went to a casino and lost " + str(-random_number) + " gold coins...")
        
        request.session['totalGold'] += random_number

    return redirect('/')

def reset(request):
    if request.method == "POST":
        request.session.clear()
    return redirect('/')
