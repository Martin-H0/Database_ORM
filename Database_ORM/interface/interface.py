# interface/interface.py
from interface.customer_interface import CustomerInterface
from interface.payment_interface import PaymentInterface
from interface.points_history_interface import PointsHistoryInterface
from interface.reservation_interface import ReservationInterface
from interface.reservation_room_interface import ReservationRoomInterface
from interface.room_interface import RoomInterface

class MainInterface:

    def __init__(self,line_length):
        self.line_length = line_length
        self.application = None

    def print_line(self, symbol="="):
        print(symbol * self.line_length)

    def print_message(self, message):
        self.print_line()
        print(message)

    def menu_input(self):
        commands = [
            ('Customer', CustomerInterface(self.mappers['customer'])),
            ('Room', RoomInterface(self.mappers['room'])),
            ('Reservation', ReservationInterface(self.mappers['reservation'])),
            ('Reservation_Room', RoomInterface(self.mappers['reservation_room'])),
            ('Points_History', RoomInterface(self.mappers['points_history'])),
            ('Payment', RoomInterface(self.mappers['payment'])),
            ('Exit', None)
        ]

        self.print_line()
        print("Vyberte příkaz:")
        num = 0
        for label, action in commands:
            num += 1
            print("\t" + str(num) + ". " + label)

        choosen_num = None
        while (choosen_num == None):
            choosen_num = input("Zadejte číslo příkazu (1-" + str(len(commands)) + "): ").strip()
            try:
                choosen_num = int(choosen_num)
                if (not 0 < choosen_num <= len(commands)):
                    raise Exception()
            except:
                print("Neplatné zadání musíte zadat číslo mezi 1 až " + str(len(commands)))
                choosen_num = None

        return commands[choosen_num - 1][1]




    # def __init__(self):  #, mappers
    #     # self.mappers = mappers
    #     self.options = {
            # '1': ('Customer', CustomerInterface(self.mappers['customer'])),
            # '2': ('Room', RoomInterface(self.mappers['room'])),
            # '3': ('Reservation', ReservationInterface(self.mappers['reservation'])),
            # '4': ('Reservation_Room', RoomInterface(self.mappers['reservation_room'])),
            # '5': ('Points_History', RoomInterface(self.mappers['points_history'])),
            # '6': ('Payment', RoomInterface(self.mappers['payment'])),
            # '0': ('Exit', None)
    #     }

    # def display_menu(self):
    #     print("\n=== Main Interface ===")
    #     for key, (name, _) in self.options.items():
    #         print(f"{key}. {name}")

    # def run(self):
    #     while True:
    #         self.display_menu()
    #         choice = input("Vyberte možnost: ").strip()
    #         if choice == '0':
    #             print("Ukončuji program. Nashledanou!")
    #             break
    #         option = self.options.get(choice)
    #         if option:
    #             name, interface = option
    #             if interface:
    #                 interface.run()
    #         else:
    #             print("Neplatná volba. Zkuste to znovu.")
