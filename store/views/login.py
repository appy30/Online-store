from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponse

from store.models.category import Category
from store.models.customer import Customer
from django.contrib.auth.hashers import make_password, check_password


class Login(View):
    errormsg = ""

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_data_by_email(email)
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['cus_id']=customer.id
                request.session['cusemail'] = customer.email
                return redirect('homepage')
            else:
                errormsg = "INVALID PASSWORRD"
        else:
            errormsg = "INVALID EMAIL"

        return render(request, 'login.html', {'error': errormsg})
