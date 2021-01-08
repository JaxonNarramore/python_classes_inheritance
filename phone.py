class Phone():
    """ This is a phone class that can be used for inheritance purposes """

    def __init__(self, phone_number, color):
        self.phone_number = phone_number
        self.color = color

    def __str__(self):
        return f'This phone belongs to {self.phone_number}'

    def call(self, other_number):
        print(f'Calling number: {other_number}')

    def text(self, other_number, message):
        print(f'sending text to {other_number}')
        print(message)

    def open_app(self, app_name):
        print(f'Opening {app_name}')


class Android(Phone):
    def __init__(self, phone_number, color):
        super().__init__(phone_number, color)
        self.passcode = None
        self.battery = 50

    def __str__(self):
        return f'Android phone that belongs to number {self.phone_number}'

    def set_passcode(self, passcode):
        self.passcode = passcode

    def unlock_phone(self, passcode):
        if passcode == self.passcode:
            print('Phone unlocked')

    def view_battery_life(self):
        print(f'Battery life: {self.battery}')

    def charge_phone(self, charging_amount):
        self.battery += charging_amount

        if self.battery > 100:
            self.battery = 100

    def view_phone_number(self):
        print(f'Phone number: {self.phone_number}')


frank_phone = Android('666-420-6969', 'black')

frank_phone.view_battery_life()
frank_phone.charge_phone(20)
frank_phone.view_battery_life()
frank_phone.view_phone_number()

frank_phone.call('512-777-7777')
frank_phone.open_app('Zoom')


class Iphone(Phone):
    def __init__(self, phone_number, color):
        super().__init__(phone_number, color)
        self.passcode = None
        self.facetime = 'yes'

    def __str__(self):
        return f'iPhone that belongs to number {self.phone_number}'

    def set_passcode(self, passcode):
        self.passcode = passcode

    def view_phone_number(self):
        print(f'Phone number: {self.phone_number}')

    def facetime(self):
        print(f'iPhones are able to facetime: {self.facetime}')


jaxon_iphone = Iphone('512-850-4200', 'space grey')
jaxon_iphone.facetime()


# class GalaxyPhone(Andriod):
#     def __init__(self, )
