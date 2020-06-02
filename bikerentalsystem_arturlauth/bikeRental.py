from datetime import datetime, timedelta



class BikeRental:


    def __init__(self, stock_value = 0):

        self.stock_value = stock_value

    def displaystock(self):

        return self.stock_value
    
    def rentBikeOnHourlyBasis(self, value):

        if value <= 0:
            print('number of bikes negative')
            return None

        if value > self.stock_value:
            print(f"Can't rent. Number of bikes available: {self.stock_value}")
            return None
        else:
            print(f"You rented {value} bikes, the price is 5 per hour")
            self.stock_value = self.stock_value - value

            time = datetime.now()

            return time

    def rentBikeOnDailyBasis(self, value):

        if value <= 0:
            print('number of bikes negative')
            return None

        if value > self.stock_value:
            print(f"Can't rent. Number of bikes available: {self.stock_value}")
            return None
        else:
            print(f"You rented {value} bikes, the price is 20 per day")
            self.stock_value = self.stock_value - value
            time = datetime.now()

            return time

    def rentBikeOnWeeklyBasis(self, value):

        if value <= 0:
            print('number of bikes negative')
            return None

        elif value > self.stock_value:
            print(f"Can't rent. Number of bikes available: {self.stock_value}")
            return None

        else:
            print(f"You rented {value} bikes, the price is 60 per week")
            self.stock_value = self.stock_value - value
            time = datetime.now()

            return time


    def returnBike(self, request):

        rentalTime, rentalBasis, bikes = request

        if rentalBasis == 1:
            self.rentBikeOnHourlyBasis(bikes)
            price = 5
            total_time = (datetime.now() - rentalTime).seconds / 3600

        elif rentalBasis == 2:
            self.rentBikeOnDailyBasis(bikes)
            price = 20
            total_time = (datetime.now() - rentalTime).days

        else:
            self.rentBikeOnDailyBasis(bikes)
            price = 60
            total_time = (datetime.now() - rentalTime).days / 7

        bill = price * total_time * bikes

        if 3 <= bikes <= 5:
            bill = bill * 0.7


        print(f"Your bill cost is : {bill}")

        return bill



class Customer():


    def __init__(self):

        self.rentalTime = 0
        self.rentalBasis = 0
        self.bikes = 0
        self.bill = 0

    def rentBike(self):

        self.bikes = input("Number of bikes:")
        self.rentalBasis = input("Type of rent:")

        if rentalBasis == 1:
            self.rentalTime = BikeRental.rentBikeOnHourlyBasis(bikes)

        elif rentalBasis == 2:
            self.rentalTime = BikeRental.rentBikeOnDailyBasis(bikes)

        else:
            self.rentalTime = BikeRental.rentBikeOnDailyBasis(bikes)


    def returnBike(self):

        if self.bikes < 0:
            return None

        if self.rentalBasis > 3:
            return 0, 0, 0

        if isinstance(self.rentalTime, datetime) is False:
            return 0, 0, 0

        return self.rentalTime, self.rentalBasis, self.bikes



if __name__ == '__main__':
    shop = BikeRental(50)
    customer1 = Customer()
    customer2 = Customer()
    customer3 = Customer()
    customer4 = Customer()
    customer5 = Customer()
    customer6 = Customer()

    # create valid rentalBasis for each customer
    customer1.rentalBasis = 1  # hourly
    customer2.rentalBasis = 1  # hourly
    customer3.rentalBasis = 2  # daily
    customer4.rentalBasis = 2  # daily
    customer5.rentalBasis = 3  # weekly
    customer6.rentalBasis = 3  # weekly

    # create valid bikes for each customer
    customer1.bikes = 1
    customer2.bikes = 5  # eligible for family discount 30%
    customer3.bikes = 2
    customer4.bikes = 8
    customer5.bikes = 15
    customer6.bikes = 30

    # create past valid rental times for each customer

    customer1.rentalTime = datetime.now() + timedelta(hours=-4)
    customer2.rentalTime = datetime.now() + timedelta(hours=-23)
    customer3.rentalTime = datetime.now() + timedelta(days=-4)
    customer4.rentalTime = datetime.now() + timedelta(days=-13)
    customer5.rentalTime = datetime.now() + timedelta(weeks=-6)
    customer6.rentalTime = datetime.now() + timedelta(weeks=-12)

    # make all customers return their bikes
    request1 = customer1.returnBike()
    request2 = customer2.returnBike()
    request3 = customer3.returnBike()
    request4 = customer4.returnBike()
    request5 = customer5.returnBike()
    request6 = customer6.returnBike()

    # check if all of them get correct bill
    shop.returnBike(request1)# 20)
    shop.returnBike(request2)# 402.5)
    shop.returnBike(request3)# 160)
    shop.returnBike(request4)# 2080)
    shop.returnBike(request5)# 5400)
    shop.returnBike(request6)# 21600)