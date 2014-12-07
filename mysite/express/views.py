from django.shortcuts import render
import os
from express.models import *

# Create your views here.
from django.http import HttpResponse
from django import template
import json
from datetime import datetime, tzinfo, date
from dateutil import tz

def index(request):
    diners = Diner.objects.all()
    ldiners = []
    for diner in diners:
        day = date.today().weekday()
        if day == 0:
            day = 'MO'
        elif day == 1:
            day = 'TU'
        elif day == 2:
            day = 'WE'
        elif day == 3:
            day = 'TH'
        elif day == 4:
            day = 'FR'
        elif day == 5:
            day = 'SA'
        else:
            day = 'SU'
        hour = DinerHour.objects.filter(did=diner, day=day)

        if hour:
            print hour[0]
            openTime = hour[0].openTime.strftime("%H:%M:%S")
            closeTime = hour[0].closeTime.strftime("%H:%M:%S")
        else:
            openTime = "00:00:00"
            closeTime = "23:59:59"

        ldiners.append({
            "did": diner.did,
            "name": diner.name,
            "loc": diner.loc,
            "openTime": openTime,
            "closeTime": closeTime,
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

    data["did"] = diner_id

    day = date.today().weekday()
    if day == 0:
        day = 'MO'
    elif day == 1:
        day = 'TU'
    elif day == 2:
        day = 'WE'
    elif day == 3:
        day = 'TH'
    elif day == 4:
        day = 'FR'
    elif day == 5:
        day = 'SA'
    else:
        day = 'SU'
        
    data["items"] = []
    for i in items:
        hour = ItemHour.objects.filter(iid=i, day=day)
        if hour:
            print hour[0]
            openTime = hour[0].openTime.strftime("%H:%M:%S")
            closeTime = hour[0].closeTime.strftime("%H:%M:%S")
        else:
            openTime = "00:00:00"
            closeTime = "23:59:59"
        data["items"].append({
            "iid": i.iid,
            "tid": i.tid.tid,
            "name": i.name,
            "price": i.price,
            "timeToCook": i.timeToCook.isoformat(),
            "startTime": openTime,
            "endTime": closeTime,
        })
        
    # data["items"] = [{
    #     "iid": i.iid,
    #     "tid": i.tid.tid,
    #     "name": i.name,
    #     "price": i.price,
    #     "timeToCook": i.timeToCook.isoformat(),
    #     "startTime": "00:00:00",
    #     "endTime": "14:59:59"
    # } for i in items]

    data["orders"] = []

    t = template.Template(open('order.html').read())

    c = template.Context({'data': json.dumps(data), 'did': diner_id})
    print "haha"
    return HttpResponse(t.render(c))

def list_orders(request, diner_id):
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

    data = {}

    data["types"] = [{ "tid": t.tid, "name": t.name } for t in types]

    data["tid"] = types[0].tid

    data["did"] = diner_id

    day = date.today().weekday()
    if day == 0:
        day = 'MO'
    elif day == 1:
        day = 'TU'
    elif day == 2:
        day = 'WE'
    elif day == 3:
        day = 'TH'
    elif day == 4:
        day = 'FR'
    elif day == 5:
        day = 'SA'
    else:
        day = 'SU'
        
    data["items"] = []
    for i in items:
        hour = ItemHour.objects.filter(iid=i, day=day)
        if hour:
            print hour[0]
            openTime = hour[0].openTime.strftime("%H:%M:%S")
            closeTime = hour[0].closeTime.strftime("%H:%M:%S")
        else:
            openTime = "00:00:00"
            closeTime = "23:59:59"
        data["items"].append({
            "iid": i.iid,
            "tid": i.tid.tid,
            "name": i.name,
            "price": i.price,
            "timeToCook": i.timeToCook.isoformat(),
            "startTime": openTime,
            "endTime": closeTime,
        })
    # data["items"] = [{
    #     "iid": i.iid,
    #     "tid": i.tid.tid,
    #     "name": i.name,
    #     "price": i.price,
    #     "timeToCook": i.timeToCook.isoformat(),
    #     "startTime": "00:00:00",ItemHour.objects.filter(iid=i, day=)
    #     "endTime": "23:59:00"
    # } for i in items]

    data["orders"] = []

    orders = Order.objects.filter(did=diner)
    for order in orders:
        data["orders"].append({
            "oid" : order.oid,
            "cardid" : order.cardid.cardid,
            "scheduledPickUpTime" : order.scheduledPickUpTime.strftime("%Y/%m/%d %H:%M:%S"),
            "stat" : order.stat,
            "items" : [
                { "name" : i.iid.name, "number" : i.number }
                for i in Include.objects.filter(oid=order)
            ]
        })

    t = template.Template(open('list.html').read())

    c = template.Context({'data': json.dumps(data), 'did': diner_id})
    print "haha"
    return HttpResponse(t.render(c))

def js_file(request, file_name):
    return HttpResponse(open(file_name + ".js").read())

def css_file(request, file_name):
    return HttpResponse(open(file_name + ".css").read())

def send_order(request):
    if request.method == "POST":

        # retrive the data
        data = json.loads(request.body)

        print 'cardid =', data['cardid']
        print 'name =', data['name']
        print 'phone =', data['phone']

        # find if we already have this cardid
        query_user = User.objects.filter(cardid=data['cardid'])
        if query_user:
            print 'found user'
            query_user.update(
                name=data['name'],
                phone=data['phone'],
                email=data['email'],
            )
            for user in query_user:
                user.save()
            print 'user saved'
        else:
            print 'create user'
            new_user = User(
                cardid=data['cardid'],
                name=data['name'],
                phone=data['phone'],
                email=data['email'],
            )

            new_user.save()

        print data['pickUpTime']
        print data['cardid']
        print data['did']
        print 'now:', datetime.now()
        print 'json:', data['pickUpTime']
        pickUpTime = datetime.strptime(data['pickUpTime'], '%Y-%m-%dT%H:%M:%S.%fZ')
        pickUpTime = pickUpTime.replace(tzinfo=tz.tzutc())
        pickUpTime = pickUpTime.astimezone(tz.tzlocal())
        print pickUpTime

        # create new order
        new_order = Order(
            cardid=User.objects.get(cardid=data['cardid']),
            did=Diner.objects.get(did=data['did']),
            timePlaced=datetime.now(),
            scheduledPickUpTime=datetime.strptime(data['pickUpTime'], '%Y-%m-%dT%H:%M:%S.%fZ'),
            # stat='PE',
        )
        new_order.save()

        print 'new_order'

        for order in data['orders']:
            include = Include(
                oid=new_order,
                iid=Item.objects.get(iid=order['iid']),
                number=order['number'],
            )
            include.save()

        print 'include'
        return HttpResponse("send_order_finished")
    else:
        return HttpResponse("what_the_huck")

def change_status(request):
    if request.method == "POST":

        # retrive the data
        data = json.loads(request.body)

        orders = Order.objects.filter(oid=data["oid"])
        orders.update(stat=data["stat"])
        for o in orders:
            o.save()

        return HttpResponse("hahaha")