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
