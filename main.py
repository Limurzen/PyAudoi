import pyaudio
import wave

# Установка параметров записи
FORMAT = pyaudio.paInt16 # формат записи (16-битный звук)
CHANNELS = 1 # количество каналов (моно)
RATE = 44100 # частота дискретизации (частота оцифровки звука)
CHUNK = 1024 # размер буфера записи

# Создание объекта PyAudio
audio = pyaudio.PyAudio()

# Создание потока записи
stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)

# Начало записи
frames = []

print("Запись начата...")

while True:
    data = stream.read(CHUNK)
    frames.append(data)
    # остановка записи при нажатии клавиши Enter
    if input() == '':
        break

print("Запись завершена...")

# Остановка потока записи
stream.stop_stream()
stream.close()
audio.terminate()

# Сохранение записанного звука в файл
WAVE_OUTPUT_FILENAME = "recorded_audio.wav"

waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()
