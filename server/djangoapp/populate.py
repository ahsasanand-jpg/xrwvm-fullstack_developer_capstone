# djangoapp/populate.py
from .models import CarMake, CarModel

def initiate():
    # Check if already populated
    if CarMake.objects.exists() or CarModel.objects.exists():
        print("Data already exists, skipping populate.")
        return

    print("Populating CarMake and CarModel data...")

    # Sample Car Makes
    nissan = CarMake.objects.create(name="NISSAN", description="Nissan Cars")
    mercedes = CarMake.objects.create(name="Mercedes", description="Mercedes Cars")
    audi = CarMake.objects.create(name="Audi", description="Audi Cars")
    kia = CarMake.objects.create(name="Kia", description="Kia Cars")
    toyota = CarMake.objects.create(name="Toyota", description="Toyota Cars")

    # Sample Car Models
    CarModel.objects.create(name="Pathfinder", car_make=nissan, type="SUV", year=2023)
    CarModel.objects.create(name="XTRAIL", car_make=nissan, type="SUV", year=2023)
    CarModel.objects.create(name="A-Class", car_make=mercedes, type="SEDAN", year=2023)
    CarModel.objects.create(name="C-Class", car_make=mercedes, type="SEDAN", year=2023)
    CarModel.objects.create(name="E-Class", car_make=mercedes, type="SEDAN", year=2023)
    CarModel.objects.create(name="A4", car_make=audi, type="SEDAN", year=2023)
    CarModel.objects.create(name="A6", car_make=audi, type="SEDAN", year=2023)
    CarModel.objects.create(name="Carnival", car_make=kia, type="WAGON", year=2023)
    CarModel.objects.create(name="Cerato", car_make=kia, type="SEDAN", year=2023)
    CarModel.objects.create(name="Kluger", car_make=toyota, type="SUV", year=2023)

    print("Database populated successfully!")
