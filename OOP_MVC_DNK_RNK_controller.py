from OOP_MVC_DNK_RNK_model import SequenceModel
from OOP_MVC_DNK_RNK_view import ConsoleView

class Controller:
    def __init__(self, view, model=None):
        self.view = view
        self.model = model

    def cmd_input_seq(self):
        s=self.view.prompt("Введіть послідовність:")
        self.model=SequenceModel(s)
        self.view.show("Послідовність оновлена.")
        self.view.show_sequence(self.model)

    def cmd_validate(self):
        if self.model is None:
            self.view.show("Спочатку введіть послідовність.")
            return
        if self.model.validate():
            self.view.show("Послідовність коректна.")
        else:
            self.view.show("Послідовність містить некоректні символи.")

    def cmd_transcribe(self):
        if self.model is None:
            self.view.show("Спочатку введіть послідовність.")
            return
        self.model=self.model.transcribe()
        self.view.show("ДНК -> РНК виконано.")
        self.view.show_sequence(self.model)

    def cmd_rev_transcribe(self):
        if self.model is None:
            self.view.show("Спочатку введіть послідовність.")
            return
        self.model=self.model.reverse_transcribe()
        self.view.show("РНК -> ДНК виконано.")
        self.view.show_sequence(self.model)

    def cmd_rev_comp(self):
        if self.model is None:
            self.view.show("Спочатку введіть послідовність.")
            return
        self.model=self.model.complement()
        self.view.show("Комплементарна послідовність обчислена.")
        self.view.show_sequence(self.model)

    def cmd_gc_len(self):
        if self.model is None:
            self.view.show("Спочатку введіть послідовність.")
            return
        gc = self.model.gc_content()
        self.view.show(f"GC% = {gc:.2f}")
        self.view.show(f"Довжина = {len(self.model.seq)}")

    def cmd_mutate(self):
        if self.model is None:
            self.view.show("Спочатку введіть послідовність.")
            return
        pos = int(self.view.prompt("Позиція (1-базна): "))
        base = self.view.prompt("Нова літера (A/T/G/C/U): ")
        self.model = self.model.mutate(pos, base)
        self.view.show("Мутація виконана.")
        self.view.show_sequence(self.model)

    def run(self):
        while True:
            self.view.print_menu()
            choice = self.view.prompt("Ваш вибір: ")
            if choice == "1":
                self.cmd_input_seq()
            elif choice == "2":
                self.cmd_validate()
            elif choice == "3":
                self.cmd_transcribe()
            elif choice == "4":
                self.cmd_rev_transcribe()
            elif choice == "5":
                self.cmd_rev_comp()
            elif choice == "6":
                self.cmd_gc_len()
            elif choice == "7":
                self.cmd_mutate()
            elif choice == "0":
                self.view.show("Завершення роботи.")
                break
            else:
                self.view.show("Невірний вибір.")

if __name__ == "__main__":
    view = ConsoleView()
    controller = Controller(view)
    controller.run()