class ConsoleView:
    def print_menu(self):
        print("===DNA/RNA MVC console===")
        print("1. Ввести/оновити послідовність")
        print("2. Перевірити валідність")
        print("3. Транскрибувати ДНК -> РНК")
        print("4. Зворотна транскрипція РНК -> ДНК")
        print("5. Комплементарна послідовність")
        print("6. Обчислити GC%")
        print("7. Мутація")
        print("8. Зберегти у файл (FASTA)")
        print("9. Завантажити з файлу (FASTA)")
        print("0. Вихід")

    def prompt(self, msg):
        return input(msg)

    def show(self, msg):
        print(msg)

    def show_sequence(self, model):
        print("SEQ:", model.seq)