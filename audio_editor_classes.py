from exceptions import TrackNotFoundException

class Track:
    """Класс для представления трека."""

    def __init__(self, track_id: int, title: str, duration: float):
        """Инициализация трека с ID, названием и длительностью."""
        self.track_id = track_id
        self.title = title
        self.duration = duration

    def __str__(self) ->str:
        """Строковое представление трека."""
        return f"Track {self.track_id}: {self.title} - {self.duration}s"


class AudioEditor:
    """Класс для работы с аудиоредактором. Содержит треки и методы для их управления."""

    def __init__(self):
        """Инициализация редактора с пустым набором треков."""
        self.tracks = {}

    def add_track(self, track_id: int, title: str, duration: float) -> None:
        """Добавить трек в редактор."""
        if track_id in self.tracks:
            raise ValueError(f"Трек с ID {track_id} уже существует.")
        else:
            track = Track(track_id, title, duration)
            self.tracks[track_id] = track
            print(f"Трек добавлен: {track}")

    def remove_track(self, track_id: int) -> None:
        """Удалить трек из редактора по ID."""
        if track_id in self.tracks:
            del self.tracks[track_id]
            print(f"Трек с ID {track_id} удален.")
        else:
            raise TrackNotFoundException(track_id)

    def apply_effect(self, effect_name: str, track_id: int) -> None:
        """Применить эффект к треку (пока эффект не реализован)."""
        if track_id in self.tracks:
            print(f"Применение эффекта '{effect_name}' к треку с ID {track_id}.")
        else:
            raise TrackNotFoundException(track_id)

class Playlist:
    """Класс для управления плейлистами в аудиоредакторе."""

    def __init__(self, name: str):
        """Инициализация плейлиста с названием."""
        self.name = name
        self.tracks = []

    def add_track(self, track: Track) -> None:
        """Добавить трек в плейлист."""
        if track in self.tracks:
            print(f"Трек '{track.title}' уже находится в плейлисте '{self.name}'.")
        else:
            self.tracks.append(track)
            print(f"Трек '{track.title}' добавлен в плейлист '{self.name}'.")

    def remove_track(self, track: Track) -> None:
        """Удалить трек из плейлиста."""
        if track in self.tracks:
            self.tracks.remove(track)
            print(f"Трек '{track.title}' удален из плейлиста '{self.name}'.")
        else:
            print(f"Трек '{track.title}' не найден в плейлисте '{self.name}'.")

    def __str__(self) -> str:
        """Строковое представление плейлиста."""
        track_list = '\n'.join([str(track) for track in self.tracks])
        return f"Плейлист '{self.name}':\n{track_list}"
