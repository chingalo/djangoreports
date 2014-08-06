from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from django.http import HttpResponseRedirect,HttpResponse
from reports.models import *
from django.shortcuts import render_to_response, get_object_or_404, render

def index(request):
	
	context = {}
	return render(request,'index.html',context)


def listUsers(request):
	
	members = Member.objects.all()
	
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'filename="users.pdf"'
	
	output = canvas.Canvas(response, pagesize=letter) 
	width, height = letter
	
	pointerOne = 80
	pointerTwo = 280
	pageNumber = 1	
	
	for member in members:		
		shiftWriter = 720		
		output.line(50,745,550,745)
		
		output.drawString(pointerOne, shiftWriter, "Name")
		output.drawString(pointerTwo, shiftWriter, member.name)
		shiftWriter = shiftWriter - 20;
		
		output.drawString(pointerOne, shiftWriter, "E-mail")
		output.drawString(pointerTwo, shiftWriter,  member.email)
		shiftWriter = shiftWriter - 20;
		
		output.drawString(pointerOne, shiftWriter, "Password")
		output.drawString(pointerTwo, shiftWriter, member.password)
		shiftWriter = shiftWriter - 20;
		
		output.drawString(pointerOne, shiftWriter, "Gender")
		output.drawString(pointerTwo, shiftWriter, member.sex)
		shiftWriter = shiftWriter - 20;
		
		output.drawString(pointerOne, shiftWriter, "Mobile number")
		output.drawString(pointerTwo, shiftWriter, member.mobile_number)
		shiftWriter = shiftWriter - 20;
		
		output.line(50,50,550,50)
		output.drawString(275, 35, str(pageNumber))
		output.showPage()
		pageNumber = pageNumber + 1
	
	output.save()
	
	return response
