from colorama import Fore, init
init(autoreset=True)

class ConsoleView:
    def print_menu(self):
        print(Fore.CYAN + "===DNA/RNA MVC console===")
        print(Fore.YELLOW + "1. Ввести/оновити послідовність")
        print(Fore.YELLOW + "2. Перевірити валідність")
        print(Fore.YELLOW + "3. Транскрибувати ДНК -> РНК")
        print(Fore.YELLOW + "4. Зворотна транскрипція РНК -> ДНК")
        print(Fore.YELLOW + "5. Комплементарна послідовність")
        print(Fore.YELLOW + "6. Обчислити GC%")
        print(Fore.YELLOW + "7. Мутація")
        print(Fore.YELLOW + "8. Зберегти у файл (FASTA)")
        print(Fore.YELLOW + "9. Завантажити з файлу (FASTA)")
        print(Fore.RED + "0. Вихід")

    def prompt(self, msg):
        return input(Fore.GREEN + msg)

    def show(self, msg):
        print(Fore.CYAN + msg)

    def show_sequence(self, model):
        print(Fore.MAGENTA + "SEQ:", model.seq)