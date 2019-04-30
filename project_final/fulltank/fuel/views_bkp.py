from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
import geoip2.database
from django.urls import reverse
import os
import csv

from .models import FuelConsumption, Price, Cities

def index(request):
    # c = FuelConsumption(brand="KIA", model="PICANTO",
    #                     version="EX5/ LX5 1.0 FF MT",
    #                     fuel="F", km_per_liter_ethanol_city=7.9, km_per_liter_ethanol_road=10.3,
    #                     km_per_liter_gas_city=11.6, km_per_liter_gas_road=15)
    # c.save()

    fuel = FuelConsumption.objects.filter(model="NEW QQ")
    km_liter_ethanol_city = fuel.first().km_per_liter_ethanol_city
    km_liter_gas_city = fuel.first().km_per_liter_gas_city
    brand = fuel.first().brand
    model = fuel.first().model

    price = Price.objects.filter(city="SAO PAULO", product="ETANOL HIDRATADO")
    avg_price_ethanol = price.first().avg_price
    price = Price.objects.filter(city="SAO PAULO", product="GASOLINA COMUM")
    avg_price_gas = price.first().avg_price
    city = price.first().city
    state = price.first().state

    km_price_ethanol_city = float(avg_price_ethanol)/km_liter_ethanol_city
    km_price_gas_city = float(avg_price_gas) / km_liter_gas_city
    lower_price = min(km_price_ethanol_city, km_price_gas_city)
    if km_price_ethanol_city < km_price_gas_city:
        message = "It is better to use ethanol to fill the tank"
    elif km_price_ethanol_city > km_price_gas_city:
        message = "It is better to use gasoline to fill the tank"
    else:
        message = "You can fill the tank with ethanol or gasoline. There is no difference"

    cars = FuelConsumption.objects.all()
    last = []
    brands =[]
    for car in cars:
        if not car.brand in last:
            brands.append(car.brand)
        last.append(car.brand)

    reader = geoip2.database.Reader('GeoLite2-City_20190326/GeoLite2-City.mmdb')
    response = reader.city('201.6.197.29')
    city2 = (response.subdivisions.most_specific.name).upper()
    reader.close()

    context = {
        "cars": cars,
        "brands": brands,
        "fuels": FuelConsumption.objects.all(),
        "prices": Price.objects.all(),
        "locations": Cities.objects.all(),
        "km_price_ethanol_city": km_price_ethanol_city,
        "km_price_gas_city": km_price_gas_city,
        "city": city,
        "city2": city2,
        "state": state,
        "brand": brand,
        "model": model,
        "lower_price": lower_price,
        "message": message
    }



    return render(request, "fuel/index3.html", context)

def load(request):

    # count = 0
    # f = open("veiculos_leves_2019_smallpdf.csv")
    # reader = csv.reader(f)
    # for brand, model, version, fuel, km_per_liter_ethanol_city, km_per_liter_ethanol_road, km_per_liter_gas_city, km_per_liter_gas_road in reader:
    #     if km_per_liter_ethanol_city == "":
    #         km_per_liter_ethanol_city = 0
    #     if km_per_liter_ethanol_road == "":
    #         km_per_liter_ethanol_road = 0
    #     if km_per_liter_gas_city == "":
    #         km_per_liter_gas_city = 0
    #     if km_per_liter_gas_road == "":
    #         km_per_liter_gas_road = 0
    #     c = FuelConsumption(brand=brand, model=model,
    #                         version=version,
    #                         fuel=fuel, km_per_liter_ethanol_city=km_per_liter_ethanol_city, km_per_liter_ethanol_road=km_per_liter_ethanol_road,
    #                         km_per_liter_gas_city=km_per_liter_gas_city, km_per_liter_gas_road=km_per_liter_gas_road)
    #     c.save()
    #     count += 1
    #     print(f"car number {count} added")
    # print(f"{count} cars loaded")

    count = 0
    city_list = []
    city_dict = {}
    f = open("price_fev19_3.csv")
    reader = csv.reader(f)
    for date, product, region, state, city, avg_price in reader:
        # p = Price(date=date, product=product, region=region, state=state, city=city, avg_price=avg_price)
        # p.save()
        city_state = city + '-' + state
        if city_state not in city_list:
            city_list.append(city_state)

        city_dict[city] = state
        count += 1
        # print(f"city number {count} added")
    print(f"{count} cities loaded")
    f.close()

    print(f"city_list: {city_list}")
    print(f"city_dict: {city_dict}")

    for city, state in city_dict.items():
        print(city)
        print(state)
        c = Cities(city=city, state=state)
        c.save()

def location(request):
    city = request.POST["city"]
    city_search = Cities.objects.filter(city__startswith=city)
    context = {
        "cities": city_search,
    }

    return render(request, "fuel/result_location.html", context)

def location2(request):
    city = request.POST["city2"]
    city_search = Cities.objects.filter(city=city)
    context = {
        "cities": city_search,
    }

    return render(request, "fuel/result_location.html", context)

def location3(request):
    city = request.POST["city20"]
    city_search = Cities.objects.filter(city=city)
    context = {
        "cities": city_search
    }

    return render(request, "fuel/result_location.html", context)

def car_city(request):
    brand = request.POST["car3"]
    print(f"brand is {brand}")
    cars_models = FuelConsumption.objects.filter(brand=brand)
    print(f"cars_models is {cars_models}")
    last = []
    models = []
    for car_model in cars_models:
        if not car_model.model in last:
            models.append(car_model.model)
        last.append(car_model.model)

    # city = request.POST["city1"]
    # city_search = Cities.objects.get(city=city)
    print(f"models is {models}")
    context = {
        "models": models,
        # "cities": city_search
    }
    # return render(request, "fuel/result_model.html", context)
    return render(request, "fuel/index.html", context)

def car_city2(request):
    model = request.POST["car4"]
    print(f"model is {model}")
    cars_versions = FuelConsumption.objects.filter(model=model)
    print(f"cars_versions is {cars_versions}")
    last = []
    versions = []
    for car_version in cars_versions:
        if not car_version.version in last:
            versions.append(car_version.version)
        last.append(car_version.version)
    print(f"versions is {versions}")
    context = {
        "cities": Cities.objects.all(),
        "versions": versions
    }

    return render(request, "fuel/index.html", context)

def car_city3(request):
    version = request.POST["car5"]
    print(f"version is {version}")
    car_filter = FuelConsumption.objects.filter(version=version)
    print(f"car_filter is {car_filter}")
    car = FuelConsumption.objects.get(version=version)
    print(f"car is {car}")

    city_select = request.POST["city1"]

    reader = geoip2.database.Reader('GeoLite2-City_20190326/GeoLite2-City.mmdb')

    response = reader.city('201.6.197.29')

    print(response.subdivisions.most_specific.name)  # good
    print(city_select)
    print(response.city.name)  # good com acento
    city = (response.subdivisions.most_specific.name).upper()
    reader.close()

    # price = Price.objects.get(city=city, product="ETANOL HIDRATADO")
    city_search = Cities.objects.get(city=city)




    price_ethanol = Price.objects.filter(city=city, product="ETANOL HIDRATADO")
    avg_price_ethanol = price_ethanol.first().avg_price
    price_gas = Price.objects.filter(city=city, product="GASOLINA COMUM")
    avg_price_gas = price_gas.first().avg_price

    #city
    km_per_liter_ethanol_city = car.km_per_liter_ethanol_city
    if km_per_liter_ethanol_city == 0:
        km_price_ethanol_city = 0
    else:
        km_price_ethanol_city = float(avg_price_ethanol) / km_per_liter_ethanol_city

    km_per_liter_gas_city = car.km_per_liter_gas_city
    if km_per_liter_gas_city == 0:
        km_price_gas_city = 0
    else:
        km_price_gas_city = float(avg_price_gas) / km_per_liter_gas_city

    if km_price_ethanol_city < km_price_gas_city:
        message_city = "It is better to use ethanol to fill the tank when driving in the city"
        if km_price_ethanol_city == 0:
            message_city = "This car cannot use ethanol to fill the tank when driving in the city"

    elif km_price_ethanol_city > km_price_gas_city:
        message_city = "It is better to use gasoline to fill the tank when driving in the city"
    else:
        message_city = "You can either fill the tank with ethanol or gasoline when driving in the city. There is no difference"

    #road
    km_per_liter_ethanol_road =  car.km_per_liter_ethanol_road
    if km_per_liter_ethanol_road == 0:
        km_price_ethanol_road =0
    else:
        km_price_ethanol_road = float(avg_price_ethanol) / km_per_liter_ethanol_road

    km_per_liter_gas_road = car.km_per_liter_gas_road
    km_price_gas_road = float(avg_price_gas) / km_per_liter_gas_road

    if km_price_ethanol_road < km_price_gas_road:
        message_road = "It is better to use ethanol to fill the tank when driving on the road"
        if km_price_ethanol_road == 0:
            message_road = "This car cannot use ethanol to fill the tank when driving on the road"

    elif km_price_ethanol_road > km_price_gas_road:
        message_road = "It is better to use gasoline to fill the tank when driving on the road"
    else:
        message_road = "You can either fill the tank with ethanol or gasoline when driving on the road. There is no difference"

    brand = car.brand
    model = car.model
    # state = city_state.first().state

    context = {
        "city": city_search,
        # "state": state,
        "brand": brand,
        "model": model,
        "message_city": message_city,
        "message_road": message_road
    }

    return render(request, "fuel/result.html", context)

def car_city4(request):
    # city = request.POST["city2"]
    # city_search = Cities.objects.filter(city=city)

    print(f"Teste")
    city = request.POST["city2"]
    print(f"city is {city}")
    car2 = request.POST["answer"]
    print(f"car is {car2}")
    # print(f"car_id is {car2.id}")
    # car_filter = FuelConsumption.objects.filter(version=car2.version)
    # print(f"car_filter is {car_filter}")
    # car = FuelConsumption.objects.get(version=car2.version)
    car = FuelConsumption.objects.get(pk=car2)
    print(f"car is {car}")



    # reader = geoip2.database.Reader('GeoLite2-City_20190326/GeoLite2-City.mmdb')
    #
    # response = reader.city('201.6.197.29')
    #
    # print(response.subdivisions.most_specific.name)  # good
    # print(city_select)
    # print(response.city.name)  # good com acento
    # city = (response.subdivisions.most_specific.name).upper()
    # reader.close()

    # price = Price.objects.get(city=city, product="ETANOL HIDRATADO")
    city_search = Cities.objects.get(city=city)




    price_ethanol = Price.objects.filter(city=city, product="ETANOL HIDRATADO")
    avg_price_ethanol = price_ethanol.first().avg_price
    price_gas = Price.objects.filter(city=city, product="GASOLINA COMUM")
    avg_price_gas = price_gas.first().avg_price

    #city
    km_per_liter_ethanol_city = car.km_per_liter_ethanol_city
    if km_per_liter_ethanol_city == 0:
        km_price_ethanol_city = 0
    else:
        km_price_ethanol_city = float(avg_price_ethanol) / km_per_liter_ethanol_city

    km_per_liter_gas_city = car.km_per_liter_gas_city
    if km_per_liter_gas_city == 0:
        km_price_gas_city = 0
    else:
        km_price_gas_city = float(avg_price_gas) / km_per_liter_gas_city

    if km_price_ethanol_city < km_price_gas_city:
        message_city = "It is better to use ethanol to fill the tank when driving in the city"
        if km_price_ethanol_city == 0:
            message_city = "This car cannot use ethanol to fill the tank when driving in the city"

    elif km_price_ethanol_city > km_price_gas_city:
        message_city = "It is better to use gasoline to fill the tank when driving in the city"
    else:
        message_city = "You can either fill the tank with ethanol or gasoline when driving in the city. There is no difference"

    #road
    km_per_liter_ethanol_road =  car.km_per_liter_ethanol_road
    if km_per_liter_ethanol_road == 0:
        km_price_ethanol_road =0
    else:
        km_price_ethanol_road = float(avg_price_ethanol) / km_per_liter_ethanol_road

    km_per_liter_gas_road = car.km_per_liter_gas_road
    km_price_gas_road = float(avg_price_gas) / km_per_liter_gas_road

    if km_price_ethanol_road < km_price_gas_road:
        message_road = "It is better to use ethanol to fill the tank when driving on the road"
        if km_price_ethanol_road == 0:
            message_road = "This car cannot use ethanol to fill the tank when driving on the road"

    elif km_price_ethanol_road > km_price_gas_road:
        message_road = "It is better to use gasoline to fill the tank when driving on the road"
    else:
        message_road = "You can either fill the tank with ethanol or gasoline when driving on the road. There is no difference"

    brand = car.brand
    model = car.model
    # state = city_state.first().state

    context = {
        "city": city_search,
        # "state": state,
        "brand": brand,
        "model": model,
        "message_city": message_city,
        "message_road": message_road
    }

    return render(request, "fuel/result.html", context)


def car_price(request):
    try:
        fuel_id = int(request.POST["car1"])
        print(f"fuel_id: {fuel_id}")
        car = FuelConsumption.objects.get(pk=fuel_id)

        city = request.POST["city1"]
        print(f"city: {city}")
        city_state = Cities.objects.filter(city=city)

    except FuelConsumption.DoesNotExist:
        raise Http404("Car does not exist")

    except Cities.DoesNotExist:
        raise Http404("City does not exist")

    price_ethanol = Price.objects.filter(city=city, product="ETANOL HIDRATADO")
    avg_price_ethanol = price_ethanol.first().avg_price
    price_gas = Price.objects.filter(city=city, product="GASOLINA COMUM")
    avg_price_gas = price_gas.first().avg_price

    #city
    km_per_liter_ethanol_city = car.km_per_liter_ethanol_city
    if km_per_liter_ethanol_city == 0:
        km_price_ethanol_city = 0
    else:
        km_price_ethanol_city = float(avg_price_ethanol) / km_per_liter_ethanol_city

    km_per_liter_gas_city = car.km_per_liter_gas_city
    if km_per_liter_gas_city == 0:
        km_price_gas_city = 0
    else:
        km_price_gas_city = float(avg_price_gas) / km_per_liter_gas_city

    if km_price_ethanol_city < km_price_gas_city:
        message_city = "It is better to use ethanol to fill the tank when driving in the city"
        if km_price_ethanol_city == 0:
            message_city = "This car cannot use ethanol to fill the tank when driving in the city"

    elif km_price_ethanol_city > km_price_gas_city:
        message_city = "It is better to use gasoline to fill the tank when driving in the city"
    else:
        message_city = "You can either fill the tank with ethanol or gasoline when driving in the city. There is no difference"

    #road
    km_per_liter_ethanol_road =  car.km_per_liter_ethanol_road
    if km_per_liter_ethanol_road == 0:
        km_price_ethanol_road =0
    else:
        km_price_ethanol_road = float(avg_price_ethanol) / km_per_liter_ethanol_road

    km_per_liter_gas_road = car.km_per_liter_gas_road
    km_price_gas_road = float(avg_price_gas) / km_per_liter_gas_road

    if km_price_ethanol_road < km_price_gas_road:
        message_road = "It is better to use ethanol to fill the tank when driving on the road"
        if km_price_ethanol_road == 0:
            message_road = "This car cannot use ethanol to fill the tank when driving on the road"

    elif km_price_ethanol_road > km_price_gas_road:
        message_road = "It is better to use gasoline to fill the tank when driving on the road"
    else:
        message_road = "You can either fill the tank with ethanol or gasoline when driving on the road. There is no difference"

    brand = car.brand
    model = car.model
    state = city_state.first().state

    context = {
        "city": city,
        "state": state,
        "brand": brand,
        "model": model,
        "message_city": message_city,
        "message_road": message_road
    }

    return render(request, "fuel/result.html", context)

# def get_client_ip(request):
#     x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
#     if x_forwarded_for:
#         ip = x_forwarded_for.split(',')[0]
#     else:
#         ip = request.META.get('REMOTE_ADDR')
#     return ip



def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    print(x_forwarded_for)
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
        print(ip)
    return HttpResponse(ip)
