from django import forms
from django.shortcuts import render
from postgresTest.models import InventoryModel
from django.contrib import messages
from postgresTest.forms import InventoryForms
from django.db import connection

def showinv(request):
    showall=InventoryModel.objects.all()
    return render(request,'index.html',{"data":showall})


def insertinv(request):
    if request.method == "POST":
        if request.POST.get('toy_id'):
            allval = InventoryModel.objects.all()
            for i in allval:
                if int(i.toy_id)==int(request.POST.get('toy_id')):
                    messages.success(request,'This Toy Id already exists! Enter unique Toy Id.');
                    return render(request,'insert.html')

            saverecord = InventoryModel()
            saverecord.toy_id = request.POST.get('toy_id')
            saverecord.toy_name = request.POST.get('toy_name')
            saverecord.manufacturer_id = request.POST.get('manufacturer_id')
            saverecord.price = request.POST.get('price')
            saverecord.quantity = request.POST.get('quantity')
            saverecord.country = request.POST.get('country')
            saverecord.category = request.POST.get('category')
            saverecord.raw_material = request.POST.get('raw_material')
            saverecord.color = request.POST.get('color')
            saverecord.save()
            messages.success(request, 'Toy ID ' + saverecord.toy_id + ' added successfully...! ')
            return render(request, 'insert.html')
        else:
            return render(request, 'insert.html')
    else:
        return render(request, 'insert.html')


def editinv(request,temp):
    editinvobj=InventoryModel.objects.get(toy_id=temp)
    return render(request,'edit.html',{"InventoryModel":editinvobj})

def updateinv(request,toy_id):

    Updateinv=InventoryModel.objects.get(toy_id=toy_id)

    form=InventoryForms(request.POST,instance=Updateinv)
    if form.is_valid():
        form.save()
        messages.success(request,'Record updated successfully......')
    return render(request,'edit.html',{"InventoryModel":Updateinv})


def deleteinv(request,toy_id):
    delinv=InventoryModel.objects.get(toy_id=toy_id)
    delinv.delete()
    showall=InventoryModel.objects.all()
    return render(request,'index.html',{"data":showall})

