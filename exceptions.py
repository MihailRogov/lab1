class AudioEditorException(Exception):
    """Базовый класс исключений для аудиоредактора."""

    pass


class TrackNotFoundException(AudioEditorException):
    """Ошибка, возникающая при попытке работать с несуществующим треком."""

    def __init__(self, track_id):
        self.track_id = track_id
        self.message = f"Трек с ID {track_id} не найден."
        super().__init__(self.message)