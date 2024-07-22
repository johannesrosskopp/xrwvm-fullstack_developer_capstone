from .models import CarMake, CarModel

def initiate():
    car_make_data = [
        {"name":"NISSAN", "description":"Great cars. Japanese technology", "country_of_origin":"Japan"},
        {"name":"Mercedes", "description":"Great cars. German technology", "country_of_origin":"Germany"},
        {"name":"Audi", "description":"Great cars. German technology", "country_of_origin":"Germany"},
        {"name":"Kia", "description":"Great cars. Korean technology", "country_of_origin":"Korea"},
        {"name":"Toyota", "description":"Great cars. Japanese technology", "country_of_origin":"Japan"},
    ]

    car_make_instances = []
    for data in car_make_data:
            car_make_instances.append(CarMake.objects.create(name=data['name'], description=data['description'], country_of_origin=data['country_of_origin']))


    # Create CarModel instances with the corresponding CarMake instances
    car_model_data = [
      {"name":"Pathfinder", "car_type":"SUV", "year": 2023, "car_make":car_make_instances[0], "seats":5},
      {"name":"Qashqai", "car_type":"SUV", "year": 2023, "car_make":car_make_instances[0], "seats":5},
      {"name":"XTRAIL", "car_type":"SUV", "year": 2023, "car_make":car_make_instances[0], "seats":5},
      {"name":"A-Class", "car_type":"SUV", "year": 2023, "car_make":car_make_instances[1], "seats":5},
      {"name":"C-Class", "car_type":"SUV", "year": 2023, "car_make":car_make_instances[1], "seats":5},
      {"name":"E-Class", "car_type":"SUV", "year": 2023, "car_make":car_make_instances[1], "seats":5},
      {"name":"A4", "car_type":"SUV", "year": 2023, "car_make":car_make_instances[2], "seats":5},
      {"name":"A5", "car_type":"SUV", "year": 2023, "car_make":car_make_instances[2], "seats":5},
      {"name":"A6", "car_type":"SUV", "year": 2023, "car_make":car_make_instances[2], "seats":5},
      {"name":"Sorrento", "car_type":"SUV", "year": 2023, "car_make":car_make_instances[3], "seats":5},
      {"name":"Carnival", "car_type":"SUV", "year": 2023, "car_make":car_make_instances[3], "seats":5},
      {"name":"Cerato", "car_type":"Sedan", "year": 2023, "car_make":car_make_instances[3], "seats":5},
      {"name":"Corolla", "car_type":"Sedan", "year": 2023, "car_make":car_make_instances[4], "seats":5},
      {"name":"Camry", "car_type":"Sedan", "year": 2023, "car_make":car_make_instances[4], "seats":5},
      {"name":"Kluger", "car_type":"SUV", "year": 2023, "car_make":car_make_instances[4], "seats":5},
        # Add more CarModel instances as needed
    ]

    for data in car_model_data:
            CarModel.objects.create(name=data['name'], car_make=data['car_make'], car_type=data['car_type'], year=data['year'], seats=data['seats'])