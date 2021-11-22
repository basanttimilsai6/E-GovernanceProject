from django.shortcuts import render,HttpResponse,redirect
from . models import Person
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
def home(request):
    return render(request,'home.html')       
def details(request):
    dat = Person.objects.all()
    query = request.GET.get('query')
    query1=request.GET.get('query1')
    query2=request.GET.get('query2')
    if query != '' and query is not None and query1 != '' and query1 is not None and query2 != '' and query2 is not None :
        xdat=dat.filter(license_no=query, citizenship=query1, phone=query2)
        params = {'xdat':xdat}
        return render(request,'details.html', params)
    else:
        messages.error(request, "कृपया सबै डेटा राख्नुहोस!")
        return redirect('/')
def rules(request):
    return render(request,'rules.html')
def contact(request):
    # messages.info(request, 'एड्मिन ! धेरै जनाको डाटा हाल्न अनुरोध गर्दछौं !')
    if request.method=='POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        paddress = request.POST['paddress']
        taddress = request.POST['taddress']
        vehicle = request.POST['vehicle']
        phone = request.POST['phone']
        fathername = request.POST['fathername']
        mothername = request.POST['mothername']
        citizenshipnumber = request.POST['citizenshipnumber']
        licensenumber = request.POST['licensenumber']
        if len(fname)<2 or len(lname)<2 or len(email)<13 or len(phone)!=10 or len(citizenshipnumber)<8 or len(licensenumber)<5:
            messages.error(request,"दिइयको डेटा सहि छैन")
        
        elif vehicle=='bike' or vehicle=='car' or vehicle=='bus' or vehicle=='taxi':
            person=Person(first_name=fname, last_name=lname, email=email, permanent_address=paddress, temporary_address=taddress, vehicle=vehicle, phone=phone, father_name=fathername, mother_name=mothername, citizenship=citizenshipnumber, license_no=licensenumber)
            person.save()
            messages.success(request,"एड्मिन! डाटा सफलतापूर्वक पेश गरीएको छ")
        
        else:
            messages.error(request,"दिइयको डेटा सहि छैन")
    return render(request,'contact.html')

def loginn(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass2 = request.POST['pass2']


        user = authenticate(request, username=username, password=pass2)
        if user is not None:
            login(request, user)
            messages.success(request,"हजुरको लगइन सिस्टम सफलतापुर्बक खोलिएको छ, अब डाटा अप्डेट गर्न सक्नुहुन्छ!")
            return redirect('/')
        else:
            messages.error(request,"हजुरको विवरण मिलेन ! पुनः लग इन गर्नुहोस")
            return redirect('/')
    else:
        return HttpResponse('404 not found')


def logoutt(request):
    logout(request)
    messages.success(request,"हजुर सिस्ट्मबाट लगआउट हुनुभयो!")
    return redirect('/')