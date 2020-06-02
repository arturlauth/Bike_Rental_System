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

    def requestBike(self):

        bikes = input("Number of bikes: ")
        self.bikes = int(bikes)

        return self.bikes

    def returnBike(self):

        if self.bikes < 0:
            return None

        if self.rentalBasis > 3:
            return 0, 0, 0

        if isinstance(self.rentalTime, datetime) is False:
            return 0, 0, 0

        return self.rentalTime, self.rentalBasis, self.bikes
