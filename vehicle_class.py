class vehicle:
    def __init__(self, marca, color, tipo):
        self.marca = marca
        self.color = color
        self.tipo = tipo
        self.velocity = 0
        self.direction = ""


    def __cilindrada__(self, cilindrada):
        self.cilindrada = float(cilindrada)

    def acelerar(self):
        print("Acelerando")

    def frenar(self):
        print("Frenado")

    def doblar(self):
        print("Girando")

    def acceleration(self):
        self.velocity += 10

        if self.velocity <= 0:
            print("You are stoped")
        else:
            print(self.velocity, "km/h")
            if self.velocity > 350:
                print("you are flying!!")

    def deceleration(self):
        self.velocity -= 10

        if self.velocity <= 0:
            print("You are stoped")
        else:
            print(self.velocity, "km/h")


    def _direction_(self, direction):
        self.direction = direction


    def show_features(self):
        print("")
        print("Features")
        print("")
        print(self.marca)
        print(self.tipo)
        print(self.color)
        print(self.cilindrada)



    def show_state(self):
        print("")
        print(f"State of the {self.tipo}")
        print("")

        print("Direction: " + self.direction)
        print("Velocity: " + self.velocity)
