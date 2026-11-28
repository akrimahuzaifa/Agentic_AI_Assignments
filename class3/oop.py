# #object oriented programming

# # inheritance, encapsulation, Abstraction, polymorphism

# class Student:
#     # name = "Akrima"
#     # age = 12

#     def __init__(self, nameee, ageee):
#         #print("init is working")
#         self.name = nameee
#         self.age = ageee

# # s1 = Student()
# # s2 = Student()
# # s3 = Student()



# # print(type(s1))
# # print(s1)
# # print(s2.name)
# # print(s3.age)

# s1 = Student("Usama", 12)
# s2 = Student("Akrima", 20)
# s3 = Student("Hammad", 30)

# print(s1.name)
# print(s2.name)
# print(s3.name)



class Car:

    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    def carInfo(self):
        print(f"The brand of car is {self.brand} and model is {self.model} and color is {self.color}")    


car1 = Car("Toyota", "Corolla", "Black")
car2 = Car("Honda", "Ciyu", "Silver")
car3 = Car("Suzuki", "Alto", "White")

print(car1.carInfo())
print(car2.carInfo())
print(car3.carInfo())