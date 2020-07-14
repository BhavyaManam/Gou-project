from django.shortcuts import render,redirect
from FirstApp.models import *
from django.http import HttpResponse
from GOU.settings import EMAIL_HOST_USER #
from django.core.mail import send_mail
from GOU import settings
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required
# Create your views here.
def login(request):
	if request.method=='POST':
		uname=request.POST['email']
		pwd=request.POST['password']
		data=MOU.objects.all().filter(mailid=uname,password=pwd)
		print(list(data))
		if data:
			return render(request,'welcome.html',{'uname':uname})
		return HttpResponse('<h2 style="color:red;">Invalid User</h2>')
	return render(request,'Login.html')

def register(request):
	if request.method=='POST':
		fname=request.POST['fname']
		lname=request.POST['lname']
		dob=request.POST['dob']
		mobile=request.POST['mobile']
		img=request.FILES['img']
		mailid=request.POST['email']
		password=request.POST['password']
		data=MOU(fname=fname,lname=lname,dob=dob,img=img,mobile=mobile,mailid=mailid,password=password)
		data.save()
		return redirect('/login')


	return render(request,'Register.html')



def document(request):
	
	return render(request,'document.html')

def documentupload(request):
	
	return render(request,'documentupload.html')

def mailsend(req):
	if req.method=="POST":
		sub=req.POST['subject']
		msg=req.POST['body']
		mailid=req.POST['email']
		frommail=EMAIL_HOST_USER
		email=EmailMessage(sub,msg,EMAIL_HOST_USER,[mailid])
		email.content_subtype='html'
		file=req.FILES['files']
		email.attach(file.name,file.read(),file.content_type)
		email.send()
		return render(req,'mailsendwelcomepage.html',{'mailid':mailid})
	return render(req,'documentupload.html')