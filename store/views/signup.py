from django.shortcuts import render, redirect

from store.models.customer import Customer
from django.contrib.auth.hashers import make_password, check_password
from django.views import View


class signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        fname = postData.get('firstname')
        lname = postData.get('lastname')
        email = postData.get('email')
        password = postData.get('password')
        mob = postData.get('phone')
        value = {
            'firstname': fname, 'lastname': lname, 'email': email, 'mobile': mob
        }
        errormsg = ''
        customer = Customer(firstname=fname, lastname=lname, email=email, mobile=mob, password=password)

        if not fname:
            errormsg = "FIRST NAME REQUIRED"
        elif not lname:
            errormsg = "last NAME REQUIRED"
        elif not email:
            errormsg = 'EMAIL REQUIRED'
        elif not password:
            errormsg = "PASSWORRD REQUIRED"
        elif not mob:
            errormsg = "MOBILE NUMBER REQUIRED"
        elif len(mob) < 10:
            errormsg = "INVALID MOBILE NUMBER"
        elif customer.is_exist():
            errormsg = "email already exist"

        if not errormsg:
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')
        else:
            data = {
                'error': errormsg,
                'values': value
            }
            return render(request, 'signup.html', data)
