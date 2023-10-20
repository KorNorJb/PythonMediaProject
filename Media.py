from icecream import ic 

class MediaFile:
    def __init__(self, name, format):
        self.name = name
        self.format = format

    def play(self):
        print(f"Воспроизведение {self.name}")

    def stop(self):
        print(f"Остановка воспроизведения {self.name}")

    def info(self):
        print(f"Файл: {self.name}, Формат: {self.format}")
class AudioFile(MediaFile):
    def __init__(self, name, format, bitrate, duration):
        super().__init__(name, format)
        self.bitrate = bitrate
        self.duration = duration

    def info(self):
        super().info()
        print(f"Битрейт: {self.bitrate} kbps, Длительность: {self.duration} (минуты/секунды)")

class VideoFile(MediaFile):
    def __init__(self, name, format, resolution, duration):
        super().__init__(name, format)
        self.resolution = resolution
        self.duration = duration

    def info(self):
        super().info()
        print(f'Разрешение: {self.resolution}, Длительность: {self.duration} (минуты/секунды)')
audio = AudioFile("SomeSound.mp3", "MP3", 256, '3:22')
video = VideoFile("SomeVideo.mp4", "MP4", "2560 x 1440", '43:23')
media_files = [audio, video]

for media in media_files:
    media.play()
    media.stop()
    media.info()
    print()

