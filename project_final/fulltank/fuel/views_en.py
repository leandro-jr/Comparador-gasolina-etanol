from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.shortcuts import render
import geoip2.database
from django.urls import reverse
import os
import csv
import time
from django.core.mail import EmailMessage

from .models import FuelConsumption, FCShort, Price, Cities, States

def index(request):
    """render initial page with FCShort and Cities DB. FCShort contains all cars with short description to fit smartphone
    screens. Cities contains all cities"""

    try:
        # oder by year(in reverse), brand, model, version and engine
        cars = FCShort.objects.all().order_by('-year', 'brand', 'model', 'version', 'engine')
        locations = Cities.objects.all()

    except FuelConsumption.DoesNotExist:
        return render(request, "fuel/error.html", {"message": "We are experiencing a problem on our system. Please try again in a few minutes"})
    except Cities.DoesNotExist:
        return render(request, "fuel/error.html", {"message": "We are experiencing a problem on our system. Please try again in a few minutes"})

    # obtain city using IP
    reader = geoip2.database.Reader('GeoLite2-City_20190326/GeoLite2-City.mmdb')
    response = reader.city('201.6.197.29')
    city = (response.subdivisions.most_specific.name).upper()
    reader.close()

    # present major Brazilian cities first on the datalist
    cities = ['SAO PAULO', 'RIO DE JANEIRO', 'BELO HORIZONTE', 'BRASILIA', 'PORTO ALEGRE',
              'RECIFE', 'FORTALEZA', 'SALVADOR', 'CURITIBA']

    context = {
        "cars": cars,
        "locations": locations,
        "cities": cities,
    }
    return render(request, "fuel/index3.html", context)

def advanced_search(request):
    """render advanced search page with list of years"""

    years = ['2019', '2018', '2017', '2016', '2015', '2014', '2013', '2012', '2011', '2010', '2009']

    reader = geoip2.database.Reader('GeoLite2-City_20190326/GeoLite2-City.mmdb')
    response = reader.city('201.6.197.29')
    city = (response.subdivisions.most_specific.name).upper()
    reader.close()

    context = {
        "years": years,
        "city": city,
    }

    return render(request, "fuel/advanced_search.html", context)

def contact(request):
    """render contact page with form to send user send a message"""

    return render(request, "fuel/contact.html")

def contact_input(request):
    """Input is email and contact_input. Those data will be used to send an email to site administrator"""

    try:
        email_contact = request.POST["email"]
        contact_input = request.POST["contact_input"]

    except KeyError:
        return render(request, "fuel/error.html", {"message": "email ou mensagem inválidas. Tente novamente"})

    if (email_contact == "" or contact_input == ""):
        return render(request, "fuel/error.html", {"message": "Email ou mensagem vazias. Tente novamente"})

    email_msg = email_contact + ' wrote a new Message: ' + contact_input
    email = EmailMessage('Message from Comparador', email_msg, to=["lealmeida.jr@gmail.com"])
    email.send()
    context = {
        "message": "Mensagem enviada. Retornaremos em breve."
    }

    return render(request, "fuel/contact.html", context)

def faq(request):
    """Render faq page"""
    return render(request, "fuel/faq.html")


def load(request):
    """Function used to load csv to database. Should be commented. To be used only by administrator in debug"""
    # count = 0
    # f = open("smallpdf2012.csv", encoding='utf-8')
    reader = csv.reader(f)
    # 2009-2012 for year, brand, model, version, engine,  fuel, km_per_liter_ethanol_city, km_per_liter_gas_city, km_per_liter_ethanol_road, km_per_liter_gas_road in reader:
    # 2013-2019 for year, brand, model, version, engine, fuel, km_per_liter_ethanol_city, km_per_liter_ethanol_road, km_per_liter_gas_city, km_per_liter_gas_road in reader:
    if km_per_liter_ethanol_city == "":
        km_per_liter_ethanol_city = 0
    if km_per_liter_ethanol_road == "":
        km_per_liter_ethanol_road = 0
    if km_per_liter_gas_city == "":
        km_per_liter_gas_city = 0
    if km_per_liter_gas_road == "":
        km_per_liter_gas_road = 0

    print(km_per_liter_ethanol_city)
    print(km_per_liter_ethanol_road)
    print(km_per_liter_gas_city)
    print(km_per_liter_gas_road)
    c = FuelConsumption(year=year, brand=brand, model=model, version=version, engine=engine, fuel=fuel,
                              km_per_liter_ethanol_city=km_per_liter_ethanol_city, km_per_liter_ethanol_road=km_per_liter_ethanol_road,
                              km_per_liter_gas_city=km_per_liter_gas_city, km_per_liter_gas_road=km_per_liter_gas_road)

    c.save()
    count += 1
    print(f"car number {count} added")
    print(f"{count} cars loaded")

    # count = 0
    # city_list = []
    # city_dict = {}
    # f = open("price_fev19_3.csv")
    # reader = csv.reader(f)
    # for date, product, region, state, city, avg_price in reader:
    #     # p = Price(date=date, product=product, region=region, state=state, city=city, avg_price=avg_price)
    #     # p.save()
    #     city_state = city + '-' + state
    #     if city_state not in city_list:
    #         city_list.append(city_state)
    #
    #     city_dict[city] = state
    #     count += 1
    #     # print(f"city number {count} added")
    # print(f"{count} cities loaded")
    # f.close()
    #
    # print(f"city_list: {city_list}")
    # print(f"city_dict: {city_dict}")
    #
    # for city, state in city_dict.items():
    #     print(city)
    #     print(state)
    #     c = Cities(city=city, state=state)
    #     c.save()

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
    """inputs year. With it, filter db and copy brands to a list of unique elements and return the json results"""
    try:
        year1 = request.POST["year1"]
        # add unicode \ufeff because it eventually shows up on the database
        year1_bom = '\ufeff' + year1
        cars_brands = FuelConsumption.objects.filter(year=year1) | FuelConsumption.objects.filter(year=year1_bom)

    except KeyError:
        return render(request, "fuel/error.html", {"message": "No year was selected. Please try again"})

    except FuelConsumption.DoesNotExist:
        return render(request, "fuel/error.html", {"message": "Car was not found on database. Please try again"})

    last = []
    brands = []
    for car_brand in cars_brands:
        if not car_brand.brand.upper() in last:
            brands.append(car_brand.brand.upper())
        last.append(car_brand.brand.upper())

    size = len(brands)
    return JsonResponse({"brands": brands, "size": size})


def car_city2(request):
    """inputs year and brand. With it, filter db and copy models to a list of unique elements and return the json results"""
    try:
        brand1 = request.POST["brand1"]
        year = request.POST["year"]
        # add unicode \ufeff because it eventually shows up on the database
        year_bom = '\ufeff' + year


        cars_models = (FuelConsumption.objects.filter(year=year, brand=brand1) | FuelConsumption.objects.filter(year=year_bom, brand=brand1))

    except KeyError:
        return render(request, "fuel/error.html", {"message": "No year/brand was selected. Please try again"})

    except FuelConsumption.DoesNotExist:
        return render(request, "fuel/error.html", {"message": "Car was not found on database. Please try again"})

    last = []
    models = []
    for car_model in cars_models:
        if not car_model.model in last:
            models.append(car_model.model)
        last.append(car_model.model)

    size_models = len(models)
    return JsonResponse({"models": models, "size_models": size_models})


def car_city3(request):
    """inputs year, brand and model. With it, filter db and copy versions to a list of unique elements and return the json results"""
    try:
        model1 = request.POST["model1"]
        brand = request.POST["brand"]
        year = request.POST["year"]
        # add unicode \ufeff because it eventually shows up on the database
        year_bom = '\ufeff' + year
        cars_versions = (FuelConsumption.objects.filter(year=year, brand=brand, model=model1) | FuelConsumption.objects.filter(
                        year=year_bom, brand=brand, model=model1))

    except KeyError:
        return render(request, "fuel/error.html", {"message": "No year/brand/model was selected. Please try again"})

    except FuelConsumption.DoesNotExist:
        return render(request, "fuel/error.html", {"message": "Car was not found on database. Please try again"})

    last = []
    versions = []
    for car_version in cars_versions:
        if not car_version.version in last:
            versions.append(car_version.version)
        last.append(car_version.version)

    size_versions = len(versions)
    return JsonResponse({"versions": versions, "size_versions": size_versions})

def car_city4(request):
    """inputs year, brand, model and version. With it, filter db and copy engines to a list of unique elements and return the json results"""
    try:
        version1 = request.POST["version1"]
        brand = request.POST["brand"]
        model = request.POST["model"]
        year = request.POST["year"]
        # add unicode \ufeff because it eventually shows up on the database
        year_bom = '\ufeff' + year
        cars_engines = (FuelConsumption.objects.filter(year=year, brand=brand, model=model, version=version1) | FuelConsumption.objects.filter(
                year=year_bom, brand=brand, model=model, version=version1))

    except KeyError:
        return render(request, "fuel/error.html", {"message": "No year/brand/model/version was selected. Please try again"})

    except FuelConsumption.DoesNotExist:
        return render(request, "fuel/error.html", {"message": "Car was not found on database. Please try again"})

    last = []
    engines = []
    for car_engine in cars_engines:
        if not car_engine.engine in last:
            engines.append(car_engine.engine)
        last.append(car_engine.engine)

    size_engines = len(engines)
    return JsonResponse({"engines": engines, "size_engines": size_engines})


def car_city5(request):
    """Provide cities list formed by city from Cities db and state from States db and return the json results"""
    try:
        engine1 = request.POST["engine1"]
        cities_all = Cities.objects.all()
    except KeyError:
        return render(request, "fuel/error.html", {"message": "No engine was selected. Please try again"})

    except Cities.DoesNotExist:
        return render(request, "fuel/error.html", {"message": "City was not found on database. Please try again"})

    cities = ['SAO PAULO-SP', 'RIO DE JANEIRO-RJ', 'BELO HORIZONTE-MG','BRASILIA-DF', 'PORTO ALEGRE-RS',
              'RECIFE-PE', 'FORTALEZA-CE', 'SALVADOR-BA', 'CURITIBA-PR']
    for c in cities_all:
        city = c.city

        try:
            state = States.objects.get(state_full=c.state)
            city_state = city + "-" + state.state_short
        except States.DoesNotExist:
            city_state = city + "-" + c.state

        cities.append(city_state)

    size_cities = len(cities)
    return JsonResponse({"cities": cities, "size_cities": size_cities})



def car_city6(request):
    """inputs are city_state, year, brand, model, version and engine. Calculates the cheapest option and return the json results"""
    try:
        city_state = request.POST["city1"]
        # split city and state
        city = city_state.split("-")[0]
        state = city_state.split("-")[1]

        year = request.POST["year"]
        brand = request.POST["brand"]
        model = request.POST["model"]
        version = request.POST["version"]
        engine = request.POST["engine"]
        # add unicode \ufeff because it eventually shows up on the database
        year_bom = '\ufeff' + year
        # lookup for car using provided inputs
        car = (FuelConsumption.objects.filter(year=year, brand=brand, model=model, version=version, engine=engine) | FuelConsumption.objects.filter(year=year_bom, brand=brand, model=model, version=version, engine=engine)).first()
        fuel = car.fuel

    except KeyError:
        return render(request, "fuel/error.html", {"message": "No year/brand/model/version/engine was selected. Please try again"})

    except FuelConsumption.DoesNotExist:
        return render(request, "fuel/error.html", {"message": "Car was not found on database. Please try again"})

    # obtain fuel prices from Price db
    try:
        price_ethanol = Price.objects.filter(city=city, product="ETANOL HIDRATADO")
        avg_price_ethanol = price_ethanol.first().avg_price
        price_gas = Price.objects.filter(city=city, product="GASOLINA COMUM")
        avg_price_gas = price_gas.first().avg_price
        date = price_ethanol.first().date

    except Price.DoesNotExist:
        return render(request, "fuel/error.html", {"message": "Fuel price was not found on database. Please try again"})

    # calculate R$/km and determine cheapest fuel
    # city
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
        message_city = "ethanol"
        if (km_price_ethanol_city == 0) and (fuel == 'G'):
            message_city = "This car is gasoline only."
        elif (km_price_ethanol_city == 0) and (fuel == 'D'):
            message_city = "This car is diesel only."

    elif km_price_ethanol_city > km_price_gas_city:
        message_city = "gasoline"
    else:
        if km_price_gas_city == 0:
            message_city = "This car does not use ethanol or gasoline. We can't compare witch option is best"
        else:
            message_city = "You can either fill the tank with ethanol or gasoline in the city. There is no difference"


    # road
    km_per_liter_ethanol_road = car.km_per_liter_ethanol_road
    if km_per_liter_ethanol_road == 0:
        km_price_ethanol_road = 0
    else:
        km_price_ethanol_road = float(avg_price_ethanol) / km_per_liter_ethanol_road

    km_per_liter_gas_road = car.km_per_liter_gas_road
    if km_per_liter_gas_road == 0:
        km_price_gas_road = 0
    else:
        km_price_gas_road = float(avg_price_gas) / km_per_liter_gas_road

    if km_price_ethanol_road < km_price_gas_road:
        message_road = "ethanol"
        if (km_price_ethanol_road == 0) and (fuel == 'G'):
            message_road = "This car is gasoline only."
        elif (km_price_ethanol_road == 0) and (fuel == 'D'):
            message_road = "This car is diesel only."

    elif km_price_ethanol_road > km_price_gas_road:
        message_road = "gasoline"
    else:
        if km_price_gas_road == 0:
            message_road = "This car does not use ethanol or gasoline. We can't compare witch option is best"
        else:
            message_road = "You can either fill the tank with ethanol or gasoline when driving on the road. There is no difference"

    if fuel == 'F':
        fuel_type = 'flex'
    elif fuel == 'G':
        fuel_type = 'gasoline'
    elif (fuel == 'E') or (fuel == 'A'):
        fuel_type = 'ethanol'
    elif fuel == 'D':
        fuel_type = 'diesel'
    else:
        fuel_type = 'not available'

    # create message with summary od car and city
    city = city.title()
    message = str(car) + ", fuel: " + str(fuel_type) + ", at " + str(city) + " - " + str(state)

    ethanol_price = avg_price_ethanol
    gas_price = avg_price_gas

    # delay for user see loading spinner
    time.sleep(1)

    # return json
    return JsonResponse({"success": 1, "message": message, "message_city": message_city, "message_road": message_road,
                         "ethanol_price": str(ethanol_price).replace('.',','), "gas_price": str(gas_price).replace('.',','), "km_per_liter_ethanol_city": str(km_per_liter_ethanol_city).replace('.',','),
                         "km_per_liter_ethanol_road": str(km_per_liter_ethanol_road).replace('.',','), "km_per_liter_gas_city": str(km_per_liter_gas_city).replace('.',','),
                         "km_per_liter_gas_road": str(km_per_liter_gas_road).replace('.',','), "date": date})


def search_car_city(request):
    """inputs are answer(car.id), city4 and optionally fuel prices. Calculates the
        cheapest option and return the json results"""

    # fuel prices
    try:
        ethanol_price = request.POST.get("ethanol_price")
        gas_price = request.POST.get("gas_price")
    except NameError:
        ethanol_price = ""
        gas_price = ""

    # obtain car.id and lookup for it on db
    try:
        car2 = request.POST.get("answer")
        car = FuelConsumption.objects.get(pk=car2)
        fuel = car.fuel
    except ValueError:
        message = "No car was selected"
        message_city = ""
        message_road = ""
        return JsonResponse({"success": 0, "message": message, "message_city": message_city, "message_road": message_road})
    except KeyError:
        message = "No car was selected"
        message_city = ""
        message_road = ""
        return JsonResponse({"success": 0, "message": message, "message_city": message_city, "message_road": message_road})
    except FuelConsumption.DoesNotExist:
        message = "Car was not found on database"
        message_city = ""
        message_road = ""
        return JsonResponse({"success": 0, "message": message, "message_city": message_city, "message_road": message_road})

    # if fuel prices are not entered by user, use the city selected
    city = ""
    if (ethanol_price == "") or (gas_price == "") or (ethanol_price == "undefined") or (gas_price == "undefined"):
        try:
            city = request.POST.get("city2")
        except KeyError:
            message = "No city was selected"
            message_city = ""
            message_road = ""
            return JsonResponse({"success": 0, "message": message, "message_city": message_city, "message_road": message_road})
    # otherwise, they should be used
    if not city:
        avg_price_ethanol = float(ethanol_price)
        avg_price_gas = float(gas_price)
        city_search = city
    # obtain fuel prices from db using selected city
    else:
        try:
            city_search = Cities.objects.get(city=city)
            price_ethanol = Price.objects.filter(city=city, product="ETANOL HIDRATADO")
            price_gas = Price.objects.filter(city=city, product="GASOLINA COMUM")
        except Cities.DoesNotExist:
            message = "City was not found on database"
            message_city = ""
            message_road = ""
            return JsonResponse({"success": 0, "message": message, "message_city": message_city, "message_road": message_road})
        except Price.DoesNotExist:
            message = "Fuel price was not found on database"
            message_city = ""
            message_road = ""
            return JsonResponse({"success": 0, "message": message, "message_city": message_city, "message_road": message_road})

        avg_price_ethanol = price_ethanol.first().avg_price
        avg_price_gas = price_gas.first().avg_price
        date = price_ethanol.first().date

    # calculate R$/km and determine cheapest fuel
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
        message_city = "ethanol"
        if (km_price_ethanol_city == 0) and (fuel == 'G'):
            message_city = "This car is gasoline only."
        elif (km_price_ethanol_city == 0) and (fuel == 'D'):
            message_city = "This car is diesel only."

    elif km_price_ethanol_city > km_price_gas_city:
        message_city = "gasoline"
    else:
        if km_price_gas_city == 0:
            message_city = "This car does not use ethanol or gasoline. We can't compare which option is best"
        else:
            message_city = "You can either fill the tank with ethanol or gasoline in the city. There is no difference"

    #road
    km_per_liter_ethanol_road = car.km_per_liter_ethanol_road
    if km_per_liter_ethanol_road == 0:
        km_price_ethanol_road = 0
    else:
        km_price_ethanol_road = float(avg_price_ethanol) / km_per_liter_ethanol_road

    km_per_liter_gas_road = car.km_per_liter_gas_road
    if km_per_liter_gas_road == 0:
        km_price_gas_road = 0
    else:
        km_price_gas_road = float(avg_price_gas) / km_per_liter_gas_road

    if km_price_ethanol_road < km_price_gas_road:
        message_road = "ethanol"
        if (km_price_ethanol_road == 0) and (fuel == 'G'):
            message_road = "This car is gasoline only."
        elif (km_price_ethanol_road == 0) and (fuel == 'D'):
            message_road = "This car is diesel only."

    elif km_price_ethanol_road > km_price_gas_road:
        message_road = "gasoline"
    else:
        if km_price_gas_road == 0:
            message_road = "This car does not use ethanol or gasoline. We can't compare which option is best"
        else:
            message_road = "You can either fill the tank with ethanol or gasoline on the road. There is no difference"

    # fuel
    if fuel == 'F':
        fuel_type = 'flex'
    elif fuel == 'G':
        fuel_type = 'gasoline'
    elif (fuel == 'E') or (fuel == 'A'):
        fuel_type = 'ethanol'
    elif fuel == 'D':
        fuel_type = 'diesel'
    else:
        fuel_type = 'not available'

    # create message if using fuel prices provided by user or through city selected
    if not city_search:
        message = str(car) + ", fuel: " + str(fuel_type)
        date = ""
    else:
        city_search_city = city_search.city.title()
        try:
            state = States.objects.get(state_full=city_search.state)
            city_search_state = state.state_short
        except States.DoesNotExist:
            city_search_state = city_search.state.title()
        message = str(car) + ", fuel: " + str(fuel_type) + ", at " + str(city_search_city) + " - " + str(city_search_state)

        ethanol_price = avg_price_ethanol
        gas_price = avg_price_gas

    # delay for user see loading spinner
    time.sleep(0.5)

    # return json
    return JsonResponse({"success": 1, "message": message, "message_city": message_city, "message_road": message_road,
                         "ethanol_price": str(ethanol_price).replace('.',','), "gas_price": str(gas_price).replace('.',','), "km_per_liter_ethanol_city": str(km_per_liter_ethanol_city).replace('.',','),
                         "km_per_liter_ethanol_road": str(km_per_liter_ethanol_road).replace('.',','), "km_per_liter_gas_city": str(km_per_liter_gas_city).replace('.',','),
                         "km_per_liter_gas_road": str(km_per_liter_gas_road).replace('.',','), "date": date})


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
    """obtain visitor IP to be used for location"""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    print(x_forwarded_for)
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
        print(ip)
    return HttpResponse(ip)

def get(request):
    context = RequestContext(request)
    context_dict = {}
    # Update the dictionary with csrf_token
    conext_dict.update(csrf(request))
    return render_to_response("index3.html", context_dict, context)
