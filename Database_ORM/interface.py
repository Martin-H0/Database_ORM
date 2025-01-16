# interface.py
from src.Customer.customer_interface import CustomerInterface
from src.Payment.payment_interface import PaymentInterface
from src.Points_History.points_history_interface import PointsHistoryInterface
from src.Reservation.reservation_interface import ReservationInterface
from src.Reservation_Room.reservation_room_interface import ReservationRoomInterface
from src.Room.room_interface import RoomInterface
import aplication_task
class Interface:
    def __init__(self):
        self.isrunning = True

        self.commands = {}
        self.commands["help"] = self.menu_input
        self.commands["exit"] = self.exit
        self.commands["customer"] = CustomerInterface().run
        # self.commands["room"] = bankinterface.BankInterface().start
        # self.commands["reservation"] = accountinterface.AccountInterface().start
        # self.commands["payment"] = transactioninterface.TransactionInterface().start

    def exit(self):
        self.isrunning = False

    def menu_input(self):
        print("exit: Exit")
        print("customer: Manage customers")
        print("room: Manage rooms")
        print("reservation: Manage reservations")
        print("payment: pay")
        print("transaction: Manage reservation_room")
        print("transaction: Manage LP points")

    def run(self):
        self.isrunning = True
        aplication_task.print_title("Welcome to ORM databse system")
        self.menu_input()
        while self.isrunning:
            try:
                cmd = input(": ")
                if cmd in self.commands:
                    self.commands[cmd]()
                else:
                    print("Unknown command")
            except EOFError:
                self.isrunning = False
            except Exception as error:
                print("Error:", error)
        print("EXIT")

        







    # def __init__(self):  #, mappers
    #     # self.mappers = mappers
    #     self.options = {
    #         '1': ('Customer', CustomerInterface(self.mappers['customer'])),
    #         '2': ('Room', RoomInterface(self.mappers['room'])),
    #         '3': ('Reservation', ReservationInterface(self.mappers['reservation'])),
    #         '4': ('Reservation_Room', RoomInterface(self.mappers['reservation_room'])),
    #         '5': ('Points_History', RoomInterface(self.mappers['points_history'])),
    #         '6': ('Payment', RoomInterface(self.mappers['payment'])),
    #         '0': ('Exit', None)
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





    # def __init__(self):
    #     self.isrunning = True
    #     self.m_interface = [
    #         CustomerInterface(self),
    #         RoomInterface(self),
    #         ReservationInterface(self),
    #         ReservationRoomInterface(self),
    #         PointsHistoryInterface(self),
    #         PaymentInterface(self),
    #     ]
    # def run(self):
    #     self.print_message("MainMenu")
    #     self._is_running = True
    #     while(self._is_running):
    #         self.menu_input()

        

    # def print_line(self, symbol="="):
    #     """Slou69 pro v7pis odn2lovac9 48rz"""
    #     print(symbol * 60)

    # def print_message(self, message):
    #     """Výpis menu_input"""
    #     self.print_line()
    #     print(message)

    # def menu_input(self):
    #     """Hlavní Menu, stará se o přidávání položek a načítání uživatelských inputů"""
    #     commands = [
    #         ('Customer', self.m_interface[1].menu_input),
    #         # ('Room', self.m_interface[2].menu_input),
    #         # ('Reservation', self.m_interface[3].menu_input),
    #         # ('Reservation_Room', self.m_interface[4].menu_input),
    #         # ('Points_History', self.m_interface[5].menu_input),
    #         # ('Payment', self.m_interface[6].menu_input),
    #         ('Exit', self.exit)
    #     ]

    #     self.print_line()
    #     print("Vyberte příkaz:")
    #     num = 0
    #     for label, action in commands:
    #         num += 1
    #         print("\t" + str(num) + ". " + label)

    #     choosen_num = None
    #     while (choosen_num == None):
    #         choosen_num = input("Zadejte číslo příkazu (1-" + str(len(commands)) + "): ").strip()
    #         try:
    #             choosen_num = int(choosen_num)
    #             if (not 0 < choosen_num <= len(commands)):
    #                 raise Exception()
    #         except:
    #             print("Neplatné zadání musíte zadat číslo mezi 1 až " + str(len(commands)))
    #             choosen_num = None

    #     return commands[choosen_num - 1][1]
    
    # def exit(self):
    #     """Nastaví hodnotu _is_running na FALSE a ukončí program"""
    #     self._is_running = False
    #     self.print_message("Exit.")







