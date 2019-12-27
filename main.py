import time
from PyQt5 import QtCore,QtMultimedia
import PyQt5.QtMultimedia as M
app = QtCore.QCoreApplication([])
abc = QtCore.QUrl.fromLocalFile("m.wav")
content = M.QMediaContent(abc)
player = M.QMediaPlayer()
player.setMedia(content)
player.play()
# time.sleep(10)
# player.pause()
app.exec()
print("done!!")