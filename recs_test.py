import recs
import time
from bin import searchfile


CHUNK = 1024
CHANNELS = 1  # stereo ou mono
RATE = 44100
#FORMAT = pyaudio.paInt16  # passivel de mudança por seleção

save_path = searchfile.save_fname()
save_path = save_path + '.wav'

recs1 = recs.RecordingFile(save_path, 'wb', 1, RATE, CHUNK)

recs1.start_recording()
time.sleep(3)
recs1.stop_recording()
