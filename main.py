from audio_editor_classes import (
    AudioEditor,
    Track,
    Effect,
    AudioEffectChain,
    Playlist,
    Mixer,
)
from file_operations import FileOperations
from exceptions import (
    TrackNotFoundException,
    FileOperationException,
    InvalidFormatException,
)


def print_menu():
    """Вывести главное меню."""
    print("\nМеню аудиоредактора:")
    print("1. Добавить трек")
    print("2. Удалить трек")
    print("3. Применить эффекты к треку")
    print("4. Сохранить проект (JSON)")
    print("5. Сохранить проект (XML)")
    print("6. Загрузить проект (JSON)")
    print("7. Загрузить проект (XML)")
    print("8. Просмотреть все треки")
    print("9. Создать плейлист")
    print("10. Добавить трек в плейлист")
    print("11. Просмотреть плейлист")
    print("12. Создать микс")
    print("13. Выйти")


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
    playlists = {}
    mixer = Mixer()
    effect_chain = AudioEffectChain()

    while True:
        print_menu()
        choice = input("Введите ваш выбор: ")

        if choice == "1":  # Добавить трек
            try:
                track_id = int(input("Введите ID трека: "))
                title = input("Введите название трека: ")
                duration = float(input("Введите длительность трека (в секундах): "))
                editor.add_track(track_id, title, duration)
            except ValueError as e:
                print(e)

        elif choice == "2":  # Удалить трек
            try:
                track_id = int(input("Введите ID трека для удаления: "))
                editor.remove_track(track_id)
            except TrackNotFoundException as e:
                print(e)
            except ValueError:
                print("Ошибка: ID трека должен быть числом.")

        elif choice == "3":  # Применить эффекты к треку
            try:
                while True:
                    effect_name = input(
                        "Введите название эффекта (или 'end' для завершения): "
                    )
                    if effect_name.lower() == "end":
                        break
                    effect_chain.add_effect(
                        Effect(effect_name, f"Описание эффекта {effect_name}")
                    )
                track_id = int(
                    input("Введите ID трека для применения цепочки эффектов: ")
                )
                track = editor.tracks.get(track_id)
                if not track:
                    raise TrackNotFoundException(track_id)
                effect_chain.apply(track)
            except TrackNotFoundException as e:
                print(e)
            except ValueError:
                print("Ошибка: ID трека должен быть числом.")

        elif choice == "4":  # Сохранить проект (JSON)
            filename = input("Введите имя файла для сохранения (JSON): ")
            try:
                FileOperations.save_project_json(editor, filename)
            except InvalidFormatException as e:
                print(
                    f"Ошибка: {e}"
                )  # Выводим сообщение, если формат файла некорректен
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

        elif choice == "9":  # Создать плейлист
            name = input("Введите название нового плейлиста: ")
            if name in playlists:
                print(f"Плейлист с именем '{name}' уже существует.")
            else:
                playlists[name] = Playlist(name)
                print(f"Плейлист '{name}' создан.")

        elif choice == "10":  # Добавить трек в плейлист
            name = input("Введите название плейлиста: ")
            if name not in playlists:
                print(f"Плейлист '{name}' не найден.")
            else:
                try:
                    track_id = int(input("Введите ID трека для добавления: "))
                    track = editor.tracks.get(track_id)
                    if not track:
                        raise TrackNotFoundException(track_id)
                    playlists[name].add_track(track)
                except TrackNotFoundException as e:
                    print(e)
                except ValueError:
                    print("Ошибка: ID трека должен быть числом.")

        elif choice == "11":  # Просмотреть плейлист
            name = input("Введите название плейлиста: ")
            if name not in playlists:
                print(f"Плейлист '{name}' не найден.")
            else:
                print(playlists[name])

        elif choice == "12":  # Создать микс
            try:
                while True:
                    track_id = int(
                        input(
                            "Введите ID трека для добавления в микс (или -1 для завершения): "
                        )
                    )
                    if track_id == -1:
                        break
                    track = editor.tracks.get(track_id)
                    if not track:
                        raise TrackNotFoundException(track_id)
                    mixer.add_track(track)
                output_title = input("Введите название нового микса: ")
                mixed_track = mixer.mix(output_title)
                print(f"Создан новый микс: {mixed_track}")
            except TrackNotFoundException as e:
                print(e)
            except ValueError:
                print("Ошибка: ID трека должен быть числом.")

        elif choice == "13":  # Выход
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
