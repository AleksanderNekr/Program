import pyautogui
import time
import string


def base(num, base):
    ans = ''
    s = '0123456789' + string.ascii_uppercase
    while num > 0:
        num, index = divmod(num, base)
        ans = s[index] + ans
    return ans


time.sleep(10)
count = -1
cheker = 15
while 1 > 0:
    while count < cheker:
        count += 1
        for letter in base(count, 16):
            pyautogui.press(letter)
        pyautogui.press(' ')
    pyautogui.hotkey('enter')
    cheker += 16
    print('whoami')
