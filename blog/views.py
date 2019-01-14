from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Data_set
from django.utils import timezone
from .forms import DateFrom
#from .forms import DateTo
from django.http import HttpResponseRedirect


# Create your views here.
def get(request):
    form1=DateFrom()
    a=request.POST.get('From','')
    b=request.POST.get('To','')
    if len(a)==0:
        a='2020-01-01 00:00:00'
        b='2020-01-01 00:00:00'
    else:
        a=a+" 00:00:00"
        b=b+" 00:00:00"
    posts = Data_set.objects.filter(created_date__gte=a, created_date__lte=b).order_by('created_date')
    #form2=DateTo()
    return render(request, 'blog/post_list.html', {'posts': posts, 'form1':form1})


#def post(self,request):
#	form1=DateFrom(request.POST)
#	if form1.is_valid():
#		form1.save()
#		form1 = DateFrom()
#		return redirect()
#
#	args = {'form1':form1, 'text':text}
#	return render(request, 'blog/post_list.html',args)

