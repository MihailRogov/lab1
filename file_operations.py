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