from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import numpy as np
import matplotlib.pyplot as plt
from io import StringIO
from . import readfile
from . import makegraph


"""
Simple web controller for the app makes readfile read and return data then supplies
the data to makegraph to make the graph and then renders the page with the new
graph
"""
def index(request):
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    date_of_birth = request.POST.get('date_of_birth')
    myfile = request.FILES['myfile']
    fs = FileSystemStorage()
    filename = fs.save(myfile.name, myfile)
    months, income, expense = readfile.read_xlsx(myfile.name)
    g = makegraph.graphs(months, income, expense)
    context = {'graph': g.make()}
    return render(request, 'graph_add_data.html', context)




# Create your views here.
