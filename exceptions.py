class AudioEditorException(Exception):
    """Базовый класс исключений для аудиоредактора."""

    pass


class TrackNotFoundException(AudioEditorException):
    """Ошибка, возникающая при попытке работать с несуществующим треком."""

    def __init__(self, track_id):
        self.track_id = track_id
        self.message = f"Трек с ID {track_id} не найден."
        super().__init__(self.message)

class InvalidFormatException(AudioEditorException):
    """Ошибка, возникающая при попытке сохранить или загрузить проект в неподдерживаемом формате."""

    def __init__(self, format_type):
        self.format_type = format_type
        self.message = f"Invalid format: {format_type}."
        super().__init__(self.message)

class FileOperationException(AudioEditorException):
    """Ошибка при сохранении или загрузке файлов."""

    def __init__(self, operation, filename):
        self.operation = operation
        self.filename = filename
        self.message = f"Error {operation} file: {filename}."
        super().__init__(self.message)