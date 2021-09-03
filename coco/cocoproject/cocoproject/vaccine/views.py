from django.shortcuts import render
from .models import *

# Create your views here.
def base(request):
    district = District.objects.all()
    d = {'district': district}
    return render(request, 'base.html', d)

def load_centers(request):
    district_id = request.GET.get('district')
    centers = Center.objects.filter(district_id=district_id).order_by('name')
    return render(request, 'centers_dropdown_list_options.html', {'centers': centers})
