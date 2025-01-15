# interface/interface.py

class ConsoleUserInterface:

    def __init__(self,line_length):
        self.line_length = line_length
        self.application = None

    def print_line(self, symbol="="):
        print(symbol * self.line_length)

    def print_message(self, message):
        self.print_line()
        print(message)

    # def new_task_input(self):
    #     self.print_line()
    #     new_task = None
    #     while (new_task == None):
    #         new_task = input("Zadejte nový úkol: ").strip()
    #         if (len(new_task) < 1):
    #             print("Neplatné zadání musíte zadat nějaký text")
    #             new_task = None
    #     return new_task

    def menu_input(self):
        commands = [
            ("Vypsat seznam", self.application.show_task_list),
            ("Přidat na seznam", self.application.add_task),
            ("Smazat celý seznam", self.application.remove_task_list),
            ("Ukončit program", self.application.terminate),
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