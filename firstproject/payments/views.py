from django.shortcuts import render
from .models import User
# Create your views here.
def bk(request):
     return render(request, 'payments/payments-1.html')

def rk(request):
     return render(request,'payments/payments-2.html')