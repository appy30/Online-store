from django.shortcuts import render
from django.views import View
from store.models.product import Product1
from store.models.category import Category


# Create your views here.
class index(View):
    def get(self, request):
        prds = None
        ctrs = Category.get_all_categories()

        category_id = request.GET.get('category')
        if category_id:
            prds = Product1.get_all_products_by_categoryid(category_id)
        else:
            prds = Product1.get_all_products()
        data = {}
        data['products'] = prds
        data['categories'] = ctrs
        da = request.session.get('cusemail')
        return render(request, 'index.html', data, )

