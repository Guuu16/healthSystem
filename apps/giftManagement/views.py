from django.shortcuts import render


# Create your views here.
def gift_detail(request):
    return render(request, 'reward_detail.html')

def assignGifts(request):
    return render(request, 'assignGifts.html')

def view_rewards(request):
    return render(request, 'view_rewards.html')