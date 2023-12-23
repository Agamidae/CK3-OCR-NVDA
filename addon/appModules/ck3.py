# An example app module.

import appModuleHandler
import api
import winUser
import tones
import scriptHandler
import ctypes
import time
import mouseHandler
import keyboardHandler
import inputCore
from globalCommands import commands
from contentRecog import uwpOcr, recogUi
from contentRecog import RecogImageInfo, ContentRecognizer, RecognitionResult, onRecognizeResultCallbackT
# import System
user32 = ctypes.windll.user32
screenWidth = user32.GetSystemMetrics(0)
screenHeight = user32.GetSystemMetrics(1)
# System.Diagnostics.Process.GetProcessesByName('GetProcessesByName')

class AppModule(appModuleHandler.AppModule):
    def goAway(self):
        winUser.setCursorPos(screenWidth, 0)

    def reOCR(self):
        object = api.getFocusObject()
        time.sleep(.2)
        recogUi.RecogResultNVDAObject.script_exit(object, None)
        commands.script_recognizeWithUwpOcr(None)

    @scriptHandler.script(gesture="kb:Control+2", description="Move the cursor to the center and right click, to send an army")
    def script_rightClickCenter(self, gesture):
        winUser.setCursorPos(screenWidth // 2, screenHeight // 2)
        time.sleep(.1)
        mouseHandler.doSecondaryClick()
        time.sleep(.1)
        self.goAway()
        self.reOCR()

    @scriptHandler.script(gesture="kb:Control+1", description="Move the cursor to the center and left click, to use a council task")
    def script_leftClickCenter(self, gesture):
        winUser.setCursorPos(screenWidth // 2, screenHeight // 2)
        time.sleep(.1)
        mouseHandler.doPrimaryClick()
        time.sleep(.1)
        self.goAway()
        self.reOCR()

    @scriptHandler.script(gesture="kb:Control+d", description="Dismiss tooltips by moving the cursor to the top right corner")
    def script_dismissTooltip(self, gesture):
        self.goAway()

    @scriptHandler.script(gesture="kb:Control+Shift+d", description="Dismiss tooltips and rescan the screen")
    def script_dismissTooltipOCR(self, gesture):
        self.goAway()
        # if isinstance(api.getFocusObject(), recogUi.RecogResultNVDAObject):
        # need to have a proper check, but i don't know how
        self.reOCR()
