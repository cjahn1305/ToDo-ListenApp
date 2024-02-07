class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Aufgabe hinzugefügt:", task)

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print("Aufgabe entfernt:", task)
        else:
            print("Aufgabe nicht gefunden.")

    def show_tasks(self):
        if self.tasks:
            print("ToDo-Liste:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")
        else:
            print("Keine Aufgaben in der Liste.")

def main():
    todo_list = TodoList()
    while True:
        print("\nToDo-Listen-App")
        print("1. Aufgabe hinzufügen")
        print("2. Aufgabe entfernen")
        print("3. Aufgaben anzeigen")
        print("4. Beenden")

        choice = input("Bitte wähle eine Option: ")

        if choice == "1":
            task = input("Gib die neue Aufgabe ein: ")
            todo_list.add_task(task)
        elif choice == "2":
            task = input("Gib die Aufgabe ein, die du entfernen möchtest: ")
            todo_list.remove_task(task)
        elif choice == "3":
            todo_list.show_tasks()
        elif choice == "4":
            print("Auf Wiedersehen!")
            break
        else:
            print("Ungültige Eingabe. Bitte wähle eine der verfügbaren Optionen.")

if __name__ == "__main__":
    main()
