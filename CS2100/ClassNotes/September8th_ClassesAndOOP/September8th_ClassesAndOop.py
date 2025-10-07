# Classes and OOP

# # all variables are objects and have types
# x = 10
# y = 10.5
# my_bool = True

# print(type(x))
# print(type(y))
# print(type(my_bool))



# #example class
# #header, traditionally start with uppercase
# class Car: 
#     #constructor
#     def __init__(self, car_model: str,car_year:int,car_color: str):
#         self.model: str = car_model
#         self.year: int = car_year
#         self.color: str = car_color

#     #methods
#     def drive(self) -> None:
#         print("vroom vroom")

#     def get_car_age(self,current_year: int) -> int:
#         return current_year - self.year

# def main() -> None:
#     car: Car = Car("Corvette", 1978, "black")
#     car.drive()
#     print(car.get_car_age(2025))



# # Cartesian Point class
class CartesianPoint:
    def __init__(self,x:float, y:float):
        self.x:float = x
        self.y:float = y

    def print_position(self) -> None:
        print(f"({self.x}, {self.y})")

    def add_to_x(self,dx: float) -> None:
        self.x += dx

    def add_to_y(self,dy: float) -> None:
        self.y += dy

# def main() -> None:
#     point: CartesianPoint = CartesianPoint(1.0,1.0)
#     point.print_position()

#     point.add_to_x(1.0)
#     point.print_position()

#     point.add_to_y(1.0)
#     point.print_position()

# if __name__ == "__main__":
#     main()


