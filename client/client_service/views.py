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
            return redirect('home', response.json())
        # Đăng nhập thất bại
        context = {}
        print(response.json()['non_field_errors'][0])
        try:
            context = {'message': response.json()['non_field_errors'][0]}
        except:
            context = {'message': 'Lỗi kết nối'}
        return render(request, 'login.html', context)

class HomeView(View):
    def get(self, request):
        user_data = request.GET
        response = requests.get('http://localhost:4002/api/ecomSys/book/all/')
        items_data = response.json()
        if response.status_code == 200:
            context = {
                'user': user_data,
                'items': items_data
            }
            print(context)
            return HttpResponse("Login successful!")
            #return render(request, 'homepage.html', context)
    


def fetch_books(request):
    response = requests.get('http://localhost:4002/api/ecomSys/book/all')
    if response.status_code == 200:
        books = response.json()
    else:
        books = []

    return render(request, 'all_books.html', {'books': books})
