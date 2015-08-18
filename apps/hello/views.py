from django.shortcuts import render
from hello.models import ident

#List_view_use#from hello.models import ident
#List_view_use#from django.views.generic import ListView

# Create your views here.

def helloview(request):
	table_data = ident.objects.all()
	return render(request,'/home/wr0ngman/git/42coffe/FortyTwoTestTask/templates/base.html',{"table_data": table_data})

#List_view_use#class HelloView(ListView):
#List_view_use#      model = ident
#List_view_use#      template_name = '/home/wr0ngman/git/42coffe/FortyTwoTestTask/templates/base.html'
