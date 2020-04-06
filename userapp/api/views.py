from userapp.models import *
from rest_framework.response import Response
from django.http import HttpResponse
from userapp.api.serializers import *
import json

def MemberActivity(request):
    if request.method == "GET":
        services = Members.objects.all()
        data = MembersSerializers(services, many=True).data
        my_json_string = json.dumps(data)
        return HttpResponse(my_json_string,content_type='application/json')
        
def Memberdetail(request,name):
    services = Members.objects.filter(real_name=name)
    data = MembersSerializers(services, many=True).data
    my_json_string = json.dumps(data)
    return HttpResponse(my_json_string,content_type='application/json')

        