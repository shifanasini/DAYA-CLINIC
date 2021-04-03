import datetime
import random

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
# from Mod import *
# Create your views here.
from daya_clinic.models import Services, Tips, Employee, Login, Schedule, Feedback, About


def homepage(request):
    return render(request,"ADMIN/homepage.html")
def adm_add_schedule(request):
    if request.method == 'POST':
        did=request.POST['select']
        day=request.POST['select2']
        from_time=request.POST['txt_frm']
        to_time=request.POST['txt_to']
        doc_obj=Employee.objects.get(id=did)
        schedule_obj =Schedule()
        schedule_obj.day=day
        schedule_obj.from_time=from_time
        schedule_obj.to_time=to_time
        schedule_obj.EMPPLOYEE=doc_obj
        schedule_obj.save()
    emp_obj = Employee.objects.filter(emp_type="Doctor")
    return render(request,"ADMIN/Add schedule.html",{'data': emp_obj})

def adm_add_services(request):
    if request.method=='POST':
        serv_name=request.POST['service']

        serv_obj=Services()
        serv_obj.services=serv_name
        serv_obj.date=datetime.datetime.now().date()
        serv_obj.save()

    return render(request,"ADMIN/ADD_SERVICES.html")

def adm_add_tips(request):
    if request.method == 'POST':
        tips_name = request.POST['tips']

        tips_obj = Tips()
        tips_obj.tips = tips_name
        tips_obj.date = datetime.datetime.now().date()
        tips_obj.save()
    return render(request,"ADMIN/ADD_TIPS.html")

def adm_employee_registration(request):
    if request.method == 'POST':
        emp_name = request.POST['txt_name']
        emp_age = request.POST['txt_age']
        emp_dob = request.POST['txt_dob']
        emp_type = request.POST['selecttype']
        emp_gender = request.POST['radio_gender']
        emp_place = request.POST['txt_place']
        emp_housename = request.POST['txt_hname']
        emp_district = request.POST['txt_district']
        emp_pincode = request.POST['txt_pincode']
        emp_phno = request.POST['txt_phno']

        emp_state = request.POST['txt_state']
        emp_qualification = request.POST['txt_qualification']
        emp_email = request.POST['txt_email']
        emp_image= request.FILES['fileField']

        password=random.randint(10,99)

        #   SAVE IMAGE
        fs=FileSystemStorage()
        filename=fs.save(emp_image.name,emp_image)

        login_obj=Login()
        login_obj.uname=emp_email
        login_obj.password=password
        login_obj.logintype=emp_type
        login_obj.save()



        employee_obj = Employee()
        employee_obj.emp_name= emp_name
        employee_obj.age= emp_age
        employee_obj.dob= emp_dob
        employee_obj.gender= emp_gender
        employee_obj.place= emp_place
        employee_obj.housename= emp_housename
        employee_obj.district= emp_district
        employee_obj.pincode= emp_pincode
        employee_obj.state= emp_state
        employee_obj.emial_Id= emp_email
        employee_obj.phone_number= emp_phno
        employee_obj.qualification= emp_qualification
        employee_obj.photo= fs.url(filename)
        employee_obj.LOGIN=login_obj
        employee_obj.emp_type=emp_type
        employee_obj.save()



    return render(request,"ADMIN/EMPLOYEE REGISTRATION.html")


def adm_view_employee(request):
    if request.method=="POST":
        emp_search=request.POST['text']
        emp_obj=Employee.objects.filter(emp_name__contains=emp_search)
        return render(request, "ADMIN/VIEW EMPLOYEES.html", {'data': emp_obj})
    emp_obj =Employee.objects.all()
    return render(request,"ADMIN/VIEW EMPLOYEES.html",{'data': emp_obj})

def adm_delete_employee(request,id):
    emp_obj=Employee.objects.get(id=id)
    emp_obj.delete()
    emp_obj = Employee.objects.all()
    return render(request, "ADMIN/VIEW EMPLOYEES.html", {'data': emp_obj})

def adm_edit_employee(request,id):
    emp_obj=Employee.objects.get(id=id)

    print(id)
    return render(request, "ADMIN/EMPLOYEE UPDATION.html", {'data': emp_obj})
def adm_update_employee(request):
    if request.method == 'POST':
        emp_name = request.POST['txt_name']
        emp_age = request.POST['txt_age']
        emp_dob = request.POST['txt_dob']
        emp_type = request.POST['selecttype']
        emp_gender = request.POST['radio_gender']
        emp_place = request.POST['txt_place']
        emp_housename = request.POST['txt_hname']
        emp_district = request.POST['txt_district']
        emp_pincode = request.POST['txt_pincode']
        emp_phno = request.POST['txt_phno']

        emp_state = request.POST['txt_state']
        emp_qualification = request.POST['txt_qualification']
        emp_email = request.POST['txt_email']
        emp_image= request.FILES['fileField']



        #   SAVE IMAGE
        fs=FileSystemStorage()
        filename=fs.save(emp_image.name,emp_image)
        hid_id=request.POST['id']
        print(hid_id)

        employee_obj = Employee.objects.get(pk=hid_id)
        print(employee_obj)
        employee_obj.emp_name = emp_name
        employee_obj.age = emp_age
        employee_obj.dob = emp_dob
        employee_obj.gender = emp_gender
        employee_obj.place = emp_place
        employee_obj.housename = emp_housename
        employee_obj.district = emp_district
        employee_obj.pincode = emp_pincode
        employee_obj.state = emp_state
        employee_obj.emial_Id = emp_email
        employee_obj.phone_number = emp_phno
        employee_obj.qualification = emp_qualification
        employee_obj.photo = fs.url(filename)

        employee_obj.emp_type = emp_type
        employee_obj.save()


        emp_obj = Employee.objects.all()
        return render(request, "ADMIN/VIEW EMPLOYEES.html", {'data': emp_obj})


def adm_employee_updation(request):
    return render(request,"ADMIN/EMPLOYEE UPDATION.html")


def adm_feedback(request):
    feedback_obj =Feedback.objects.all()

    return render(request,"ADMIN/Feedback.html",{'data':feedback_obj})


def adm_leave_approval(request):
    return render(request,"ADMIN/Leave Approval.html")
def admin_view_stock(request):
    return render(request,"ADMIN/LView stock.html")
def adm_feedback_replay(request):
    return render(request,"ADMIN/Send replay to paitents.html")


def adm_add_attendance(request):
    res=Employee.objects.all()
    if request.method==['post']:
        pass
    return render(request,"ADMIN/ADD ATTENDANCE.html",{'data':res})

def adm_view_attendance(request):



    return render(request,"View attendance_adm.html")
def adm_view_employees(request):
    return render(request,"ADMIN/VIEW EMPLOYEES.html")
def adm_view_patients(request):
    return render(request,"ADMIN/View patients.html")
def adm_view_sales_report_main(request):
    return render(request,"ADMIN/Sales Repor.html")


def adm_view_schedule(request):

    schedule_obj = Schedule.objects.all()
    return render(request,"ADMIN/View schedule.html",{'data':schedule_obj})
def adm_delete_schedule(request,id):
    schedule_obj=Tips.objects.get(id=id)

    schedule_obj.delete()
    schedule_obj = Schedule.objects.all()
    return render(request, "ADMIN/View schedule.html", {'data': schedule_obj})

def adm_view_services(request):
    service_obj = Services.objects.all()

    return render(request,"ADMIN/View service.html",{'data': service_obj})

def adm_edit_service(request,id):
    serv_obj=Services.objects.get(id=id)
    print(id)
    return render(request, "ADMIN/Update service.html", {'data': serv_obj})

def adm_update_service(request):
    if request.method == 'POST':
        service = request.POST['services']


        hid_id=request.POST['id']
        print(hid_id)
        service_obj = Services.objects.get(pk=hid_id)
        print(service_obj)
        service_obj.emp_name =service
        service_obj.save()

        serev_obj = Services.objects.all()
        return render(request, "ADMIN/View service.html", {'data': serev_obj})
def adm_service_updation(request):
    return render(request,"ADMIN/Update service.html")

def adm_delete_services(request,id):
    service_obj=Services.objects.get(id=id)

    service_obj.delete()
    service_obj = Services.objects.all()
    return render(request, "ADMIN/View service.html", {'data': service_obj})


def adm_view_tips(request):
    tips_obj=Tips.objects.all()
    return render(request,"ADMIN/View tips.html",{'data':tips_obj})
def adm_delete_tips(request,id):
    tips_obj=Tips.objects.get(id=id)
    tips_obj.delete()
    tips_obj = Tips.objects.all()
    return render(request, "ADMIN/View tips.html", {'data': tips_obj})



def adm_view_booking_info(request):
    return render(request,"ADMIN/View booking info.html")

def adm_add_about(request):
    if request.method=='POST':
        about_obj=request.POST['about']
        img_obj=request.FILES['fileField']
        fs = FileSystemStorage()
        filename = fs.save(img_obj.name, img_obj)
        image=fs.url(filename)

        date=datetime.datetime.now().date()
        res=About(about=about_obj,photo=image,date=date)
        res.save()

    return render(request,"ADMIN/ABOUT DAYA.html")
def adm_view_about(request):
    about_obj=About.objects.all()
    return render(request,"ADMIN/VIEW ABOUT.html",{'data':about_obj})




def adm_temp(request):
    return render(request,"adm_index.html")
# Create your views here.
def homepage_doctor(request):
    return render(request,"DOCTOR/homepagepharmacist.html")
def doc_add_prescription(request):
    return render(request,"DOCTOR/ADD PRESCRIPTION.html")
def doc_view_leave_satatus(request):
    return render(request,"DOCTOR/Leave Status doctor.html")
def doc_add_leave(request):
    return render(request,"DOCTOR/LEAVE APPLICATION DOCTOR.html")
def doc_next_slot(request):
    return render(request,"DOCTOR/Next slot.html")
def doc_add_next_visit(request):
    return render(request,"DOCTOR/NEXT VISIT ENTRY.html")
def doc_view_medicine(request):
    return render(request,"DOCTOR/View medicine.html")
def doc_view_patients(request):
    return render(request,"DOCTOR/View patients doctor.html")

def doc_view_prescription(request):
    return render(request,"DOCTOR/VIew prescription.html")
def doc_view_schedule(request):
    return render(request,"DOCTOR/View schedule.html")
