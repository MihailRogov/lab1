from audio_editor_classes import AudioEditor, Track
from file_operations import FileOperations
from exceptions import TrackNotFoundException, FileOperationException, InvalidFormatException


def print_menu():
    """Вывести главное меню."""
    print("\nМеню аудиоредактора:")
    print("1. Добавить трек")
    print("2. Удалить трек")
    print("3. Применить эффект к треку")
    print("4. Сохранить проект (JSON)")
    print("5. Сохранить проект (XML)")
    print("6. Загрузить проект (JSON)")
    print("7. Загрузить проект (XML)")
    print("8. Просмотреть все треки")
    print("9. Выйти")


def print_tracks(editor: AudioEditor):
    """Вывести все треки, сохранённые в аудиоредакторе."""
    if editor.tracks:
        print("\nСписок всех треков:")
        for track in editor.tracks.values():
            print(
                track
            )  # Используем __str__ из класса Track для вывода информации о треке
    else:
        print("Нет сохранённых треков.")


def main():
    editor = AudioEditor()

    while True:
        print_menu()
        choice = input("Введите ваш выбор: ")

        if choice == "1":  # Добавить трек
            try:
                track_id = int(input("Введите ID трека: "))
                title = input("Введите название трека: ")
                duration = float(input("Введите длительность трека (в секундах): "))
                editor.add_track(track_id, title, duration)
            except ValueError:
                print("Ошибка: введены некорректные данные. Убедитесь, что ID и длительность — числа.")


        elif choice == "2":  # Удалить трек
            try:
                track_id = int(input("Введите ID трека для удаления: "))
                editor.remove_track(track_id)
            except TrackNotFoundException as e:
                print(e)
            except ValueError:
                print("Ошибка: ID трека должен быть числом.")

        elif choice == "3":  # Применить эффект
            try:
                effect_name = input("Введите название эффекта: ")
                track_id = int(input("Введите ID трека, к которому применить эффект: "))
                editor.apply_effect(effect_name, track_id)
            except TrackNotFoundException as e:
                print(e)
            except ValueError:
                print("Ошибка: ID трека должен быть числом.")

        elif choice == "4":  # Сохранить проект (JSON)
            filename = input("Введите имя файла для сохранения (JSON): ")
            try:
                FileOperations.save_project_json(editor, filename)
            except InvalidFormatException as e:
                print(f"Ошибка: {e}")  # Выводим сообщение, если формат файла некорректен
            except FileOperationException as e:
                print(e)

        elif choice == "5":  # Сохранить проект (XML)
            filename = input("Введите имя файла для сохранения (XML): ")
            try:
                FileOperations.save_project_xml(editor, filename)
            except InvalidFormatException as e:
                print(f"Ошибка: {e}")
            except FileOperationException as e:
                print(e)

        elif choice == "6":  # Загрузить проект
            filename = input("Введите имя файла для загрузки (JSON): ")
            try:
                FileOperations.load_project_json(editor, filename)
            except FileOperationException as e:
                print(e)

        elif choice == "7":  # Загрузить проект
            filename = input("Введите имя файла для загрузки (XML): ")
            try:
                FileOperations.load_project_xml(editor, filename)
            except FileOperationException as e:
                print(e)

        elif choice == "8":  # Просмотреть треки
            print_tracks(editor)

        elif choice == "9":  # Выход
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
