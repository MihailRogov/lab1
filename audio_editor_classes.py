from exceptions import TrackNotFoundException

class Track:
    """Класс для представления трека."""

    def __init__(self, track_id: int, title: str, duration: float):
        """Инициализация трека с ID, названием и длительностью."""
        self.track_id = track_id
        self.title = title
        self.duration = duration

    def __str__(self):
        """Строковое представление трека."""
        return f"Track {self.track_id}: {self.title} - {self.duration}s"


class AudioEditor:
    """Класс для работы с аудиоредактором. Содержит треки и методы для их управления."""

    def __init__(self):
        """Инициализация редактора с пустым набором треков."""
        self.tracks = {}

    def add_track(self, track_id: int, title: str, duration: float):
        """Добавить трек в редактор."""
        if track_id in self.tracks:
            raise ValueError(f"Трек с ID {track_id} уже существует.")
        else:
            track = Track(track_id, title, duration)
            self.tracks[track_id] = track
            print(f"Трек добавлен: {track}")

    def remove_track(self, track_id: int):
        """Удалить трек из редактора по ID."""
        if track_id in self.tracks:
            del self.tracks[track_id]
            print(f"Трек с ID {track_id} удален.")
        else:
            raise TrackNotFoundException(track_id)

    def apply_effect(self, effect_name: str, track_id: int):
        """Применить эффект к треку (пока эффект не реализован)."""
        if track_id in self.tracks:
            print(f"Применение эффекта '{effect_name}' к треку с ID {track_id}.")
        else:
            raise TrackNotFoundException(track_id)
