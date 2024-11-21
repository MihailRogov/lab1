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
            raise TrackNotFoundException(track.track_id)

    def __str__(self) -> str:
        """Строковое представление плейлиста."""
        track_list = '\n'.join([str(track) for track in self.tracks])
        return f"Плейлист '{self.name}':\n{track_list}"


class Mixer:
    """Класс для сведения треков в аудиомикс."""

    def __init__(self):
        """Инициализация миксера с пустым набором треков."""
        self.tracks = []

    def add_track(self, track: Track) -> None:
        """Добавить трек в микс."""
        self.tracks.append(track)
        print(f"Трек '{track.title}' добавлен в микс.")

    def remove_track(self, track: Track) -> None:
        """Удалить трек из микса."""
        if track in self.tracks:
            self.tracks.remove(track)
            print(f"Трек '{track.title}' удален из микса.")
        else:
            print(f"Трек '{track.title}' не найден в миксе.")

    def mix(self, output_title: str) -> Track:
        """Создать новый трек из смешанных треков."""
        if not self.tracks:
            raise TrackNotFoundException("В миксе нет треков.")
        total_duration = sum(track.duration for track in self.tracks)
        print(f"Создан микс '{output_title}' из {len(self.tracks)} треков, длительность: {total_duration} секунд.")
        return Track(track_id=-1, title=output_title, duration=total_duration)
    
class Effect:
    """Класс для представления эффекта, который можно применить к треку."""

    def __init__(self, name: str, description: str):
        """Инициализация эффекта с именем и описанием."""
        self.name = name
        self.description = description

    def apply(self, track: Track) -> None:
        """Применить эффект к треку (базовая реализация)."""
        print(f"Эффект '{self.name}' применен к треку: {track.title}.")

class AudioEffectChain:
    """Класс для управления цепочкой аудиоэффектов."""

    def __init__(self):
        """Инициализация пустой цепочки эффектов."""
        self.effects = []

    def add_effect(self, effect: 'Effect') -> None:
        """Добавить эффект в цепочку."""
        self.effects.append(effect)
        print(f"Эффект '{effect.name}' добавлен в цепочку.")

    def remove_effect(self, effect: 'Effect') -> None:
        """Удалить эффект из цепочки."""
        if effect in self.effects:
            self.effects.remove(effect)
            print(f"Эффект '{effect.name}' удален из цепочки.")
        else:
            print(f"Эффект '{effect.name}' не найден в цепочке.")

    def apply(self, track: 'Track') -> None:
        """Применить все эффекты из цепочки к треку."""
        for effect in self.effects:
            effect.apply(track)
        print(f"Все эффекты из цепочки применены к треку '{track.title}'.")