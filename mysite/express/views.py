from django.shortcuts import render
import os
from express.models import Type, Diner, Item

# Create your views here.
from django.http import HttpResponse
from django import template
import json
from datetime import datetime

def index(request):
    diners = Diner.objects.all()
    ldiners = []
    for diner in diners:
        ldiners.append({
            "did": diner.did,
            "name": diner.name,
            "loc": diner.loc,
            "openTime": "00:00:00",
            "closeTime": "23:59:59"
        })

    t = template.Template(open('index.html').read())
    c = template.Context({'data': json.dumps(ldiners)})
    return HttpResponse(t.render(c))

def order(request, diner_id):
    diners = Diner.objects.filter(did=diner_id)

    if len(diners) == 0:
        return HttpResponse("not found diner?")

    diner = diners[0]
    print "[DEBUG] diner.did = %d" % diner.did

    types = Type.objects.filter(did=diner)
    for t in types:
        print "[DEBUG] type[%d] = %s" % (t.tid, t.name)

    items = Item.objects.filter(did=diner)
    for i in items:
        print "[DEBUG] item[%d] = %s([%d]%s)" % (i.iid, i.name, i.tid.tid, i.tid.name)

    currentTime = datetime.now().time()


    data = {}

    data["timePicked"] = False

    data["pickedTime"] = "%02d:%02d:%02d" % (currentTime.hour, currentTime.minute, currentTime.second)

    data["types"] = [{ "tid": t.tid, "name": t.name } for t in types]

    data["tid"] = types[0].tid

    data["items"] = [{
        "iid": i.iid,
        "tid": i.tid.tid,
        "name": i.name,
        "price": i.price,
        "timeToCook": i.timeToCook.isoformat(),
        "startTime": "00:00:00",
        "endTime": "23:59:59"
    } for i in items]

    data["orders"] = []

    t = template.Template(open('order.html').read())

    c = template.Context({'data': json.dumps(data)})
    print "haha"
    return HttpResponse(t.render(c))

def js_file(request, file_name):
    return HttpResponse(open(file_name + ".js").read())

def css_file(request, file_name):
    return HttpResponse(open(file_name + ".css").read())