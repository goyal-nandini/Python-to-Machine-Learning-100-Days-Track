from turtle import Turtle, Screen
import random

# Constants
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.all_cars = []       # active cars on screen
        self.car_reserve = []    # offscreen cars ready to reuse
        self.car_speed = STARTING_MOVE_DISTANCE
        self.loop_counter = 0    # track game loop iterations

        # EXTRA PART📍 Register the car shape (make sure car.gif is in your project folder)
        screen = Screen()
        screen.addshape("car.gif")

    def car_creation(self):
        """Create a new car every 6th loop iteration."""
        self.loop_counter += 1
        if self.loop_counter % 6 == 0:
            # reuse a car if available
            if self.car_reserve:
                new_car = self.car_reserve.pop()
            else:
                new_car = Turtle("car.gif")
                new_car.penup()
                # optional tint if your gif supports transparency
                new_car.color(random.choice(COLORS))

            random_y = random.randint(-230, 230)
            new_car.goto(300, random_y)  # spawn at right edge
            self.all_cars.append(new_car)

    def car_motion(self):
        """Move cars leftwards and recycle offscreen ones."""
        for car in self.all_cars[:]:  # iterate over a copy to allow removal
            car.backward(self.car_speed)
            if car.xcor() < -320:     # offscreen
                self.all_cars.remove(car)
                self.car_reserve.append(car)

    def level_up(self):
        """Increase car speed when player levels up."""
        self.car_speed += MOVE_INCREMENT

    # 📍 NOT WORKING 
    def clear_all(self):
        """Hide and recycle all cars (used on game over or restart)."""
        for car in self.all_cars:
            car.hideturtle()
            self.car_reserve.append(car)
        self.all_cars.clear()
        self.car_speed = STARTING_MOVE_DISTANCE
        self.loop_counter = 0
