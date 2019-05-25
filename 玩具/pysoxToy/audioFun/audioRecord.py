import pyaudio
import wave
import sox
import os
import threading

input_filename = "input.wav"               # 麦克风采集的语音输入
input_filepath = "./"              # 输入文件的path
in_path = input_filepath + input_filename


def paly_audio():
    try:
        os.remove("./input.wav")
        os.remove("./output.wav")
    except:
        return

def get_audio(filepath):
    CHUNK = 256
    FORMAT = pyaudio.paInt16
    CHANNELS = 2                # 声道数
    RATE = 44100                # 采样率
    RECORD_SECONDS = 1          # 录入时长
    WAVE_OUTPUT_FILENAME = filepath
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("*"*10, "开始录音：请在" + str(RECORD_SECONDS) + "秒内输入语音")
    frames = []


    t_play = threading.Thread(target=paly_audio)
    t_play.start()
    
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    print("*"*10, "录音结束\n")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

get_audio(in_path)

tfm = sox.Transformer()
# tfm.reverse()
# tfm.pitch(3.1)
tfm.compand()
# tfm.noiseprof("./noise_conf/noise.wav", "./noise_conf/noise.txt")
tfm.noisered("./noise_conf/noise.txt",amount = 0.5)
tfm.fade(fade_in_len=1.0, fade_out_len=1)
tfm.build("./input.wav",'./output.wav')
print(tfm.effects_log)