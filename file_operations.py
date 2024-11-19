import json
import xml.etree.ElementTree as ET
from exceptions import FileOperationException
from audio_editor_classes import AudioEditor, Track


class FileOperations:
    """Класс для работы с файлами (сохранение и загрузка в JSON и XML)."""

    @staticmethod
    def save_project_json(editor: AudioEditor, filename: str):
        """Сохранить проект в файл JSON."""
        data = {
            "tracks": {
                track_id: vars(track) for track_id, track in editor.tracks.items()
            }
        }
        try:
            with open(filename, "w") as f:
                json.dump(data, f, indent=4)
            print(f"Проект сохранен в JSON файл: {filename}")
        except Exception as e:
            raise FileOperationException("saving", filename) from e

    @staticmethod
    def save_project_xml(editor: AudioEditor, filename: str):
        """Сохранить проект в файл XML."""
        root = ET.Element("project")

        tracks_element = ET.SubElement(root, "tracks")
        for track_id, track in editor.tracks.items():
            track_element = ET.SubElement(tracks_element, "track", id=str(track_id))
            track_element.text = track.title
            track_element.set(
                "duration", str(track.duration)
            )  # Добавляем длительность трека как атрибут

        tree = ET.ElementTree(root)
        try:
            tree.write(filename)
            print(f"Проект сохранен в XML файл: {filename}")
        except Exception as e:
            raise FileOperationException("saving", filename) from e
    @staticmethod
    def load_project_json(editor: AudioEditor, filename: str):
        """Загрузить проект из файла JSON."""
        try:
            with open(filename, "r") as f:
                data = json.load(f)

            # Загружаем все треки
            for track_id, track_data in data["tracks"].items():
                # Добавляем трек в словарь editor.tracks
                editor.tracks[int(track_id)] = Track(
                    track_id, track_data["title"], track_data["duration"]
                )

                print(f"Проект загружен из JSON файла: {filename}")

        except Exception as e:
            raise FileOperationException("loading", filename) from e
    @staticmethod
    def load_project_xml(editor: AudioEditor, filename: str):
        """Загрузить проект из файла XML."""
        try:
            tree = ET.parse(filename)
            root = tree.getroot()

            editor.tracks = {}
            # Загружаем все треки
            for track_element in root.findall("tracks/track"):
                track_id = int(track_element.attrib["id"])  # Чтение ID трека
                title = track_element.text  # Название трека
                duration = float(
                    track_element.attrib.get("duration", 0)
                )  # Извлекаем длительность
                editor.tracks[track_id] = Track(
                    track_id, title, duration
                )  # Создаём объект Track

            print(f"Проект загружен из XML файла: {filename}")
        except Exception as e:
            raise FileOperationException("loading", filename) from e