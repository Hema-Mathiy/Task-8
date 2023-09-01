#Defining TV class
class TV:
    def __init__(self, brand):
        self.brand = brand
        self.channel = 1
        self.volume = 100

    def increase_volume(self):
        self.volume = min(100, self.volume + 1)

    def decrease_volume(self):
        self.volume = max(0, self.volume - 1)

    def set_channel(self, channel):
        self.channel = max(1, min(50, channel))

    def reset(self):
        self.channel = 1
        self.volume = 50

    def status(self):
        return f"{self.brand} at channel {self.channel}, volume {self.volume}"

# Defining the TV type in a class function
class TVType(TV):
    def __init__(self, brand, screen_thickness, energy_usage, lifespan, refresh_rate=None, viewing_angle=None, backlight=None):
        super().__init__(brand)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate
        self.viewing_angle = viewing_angle
        self.backlight = backlight

    def details(self):
        type_name = self.__class__.__name__
        details_str = f"{type_name} Details: Brand - {self.brand}, Screen Thickness - {self.screen_thickness} inches, " \
                      f"Energy Usage - {self.energy_usage}, Lifespan - {self.lifespan} years"
        if self.refresh_rate:
            details_str += f", Refresh Rate - {self.refresh_rate} Hz"
        if self.viewing_angle:
            details_str += f", Viewing Angle - {self.viewing_angle} degrees"
        if self.backlight:
            details_str += f", Backlight - {self.backlight}"
        return details_str

led_tv = TVType("Sony", 1.5, "Low", 5, refresh_rate=120)
plasma_tv = TVType("LG", 2.0, "Medium", 6, viewing_angle=160, backlight="Yes")

#printing the status and details of the TV
print(led_tv.status())
print(led_tv.details())

print(plasma_tv.status())
print(plasma_tv.details())


