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
