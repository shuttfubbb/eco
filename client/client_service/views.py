from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
import requests
from django.http import JsonResponse
class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        
        data = {
            'username': username,
            'password': password
        }
        response = requests.post('http://localhost:4001/api/ecomSys/user/login/', data=data)
        if response.status_code == 200:
            # Đăng nhập thành công, chuyển hướng đến trang thành công
            return redirect('success')
        else:
            context = {'message': 'Đăng nhập thất bại'}
            return render(request, 'login.html', context)

def success(request):
    return HttpResponse("Login successful!")

class HomeView(View):
    def get(self, request):
        return render(request, 'homepage.html')
    
