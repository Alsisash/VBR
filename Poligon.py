import os
import time
import os
import time
import pyautogui
import openpyxl
import  TablForm
os.system(r'C:\Users\Alex\AppData\Local\Viber\Viber.exe')
a = pyautogui.screenshot()
a.save('scr1.PNG')

poisk = pyautogui.locateOnScreen('Dok.PNG' or 'Dok2.PNG'or 'PodklKlienta.PNG')
pyautogui.click(poisk)
                                                            # poisk2 = pyautogui.locateOnScreen('Poisk2.PNG')
                                                            # pyautogui.click(poisk2)
pyautogui.hotkey('ctrl','a')
pyautogui.press('delete')
##############################################
pyautogui.typewrite(TablForm.vozvrat_tel())
##############################################         # Работа с таблицами
