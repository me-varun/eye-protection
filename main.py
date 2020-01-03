import time
from PyQt5 import QtCore,QtMultimedia
import PyQt5.QtMultimedia as M
app = QtCore.QCoreApplication([])
abc = QtCore.QUrl.fromLocalFile("m.wav")
content = M.QMediaContent(abc)
player = M.QMediaPlayer()
player.setMedia(content)
player.setVolume(10)
#print(player.volume)
player.play()
#time.sleep(2)
#player.pause()
app.exec()
print("done!!")