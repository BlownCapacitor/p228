import wave
import base64
song = wave.open("audEnc.wav", mode='rb')

frame_bytes = bytearray(list(song.readframes(song.getnframes())))

extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
string = "".join(chr(int("".join(map(str,extracted[i:i+8])),2)) for i in range(0,len(extracted),8))
decoded = string.split("###")[0]
data = decoded
data2 = data.rstrip(data[-1])
data3 = data2[2:]
print(data)
print(data2)
print(data3)

decoded_data = base64.b64decode(data2)
img_file = open('image.jpeg', 'wb')
img_file.write(decoded_data)
img_file.close()

song.close()
