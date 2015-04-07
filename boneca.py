# -*- coding: utf-8 -*-
# Baseado no post do Tim Golden: http://timgolden.me.uk/python/win32_how_do_i/catch_system_wide_hotkeys.html
#
#
#        Modo de Usar:
#
#       se for rodar pelo script, dê pythonw.exe boneca.py
#       Para aparecer a boneca pressione Print Screen
#       Para fechar o programa pressione Windows + F4
#
#
#
import os
import sys
import ctypes
from ctypes import wintypes
import win32con
import esky

if hasattr(sys,"frozen"):
    app = esky.Esky(sys.executable,"http://teenspirit.com.br/exemplo_boneca/")
    app.auto_update()

byref = ctypes.byref
user32 = ctypes.windll.user32

HOTKEYS = {
    1 : (win32con.VK_SNAPSHOT, 0), ####Essa Linha Pega a entrada "PRINT SCREEN" do teclado
    2 : (win32con.VK_F4, win32con.MOD_WIN)
}

def handle_win_f3 ():
    os.startfile(os.path.join(os.path.realpath(os.path.dirname(sys.argv[0])),"seu-boneco.jpg"))

def handle_win_f4 ():
    user32.PostQuitMessage (0)

HOTKEY_ACTIONS = {
    1 : handle_win_f3,
    2 : handle_win_f4
}

#
# Registrando as chaves sem dar o print pra ficar escondido na tela.
for id_key, (vk, modifiers) in HOTKEYS.items ():
    #print "Registering id", id, "for key", vk
    if not user32.RegisterHotKey (None, id_key, modifiers, vk):
        #print "Unable to register id", id
        pass


# Executando as funções e tirando o registro das chaves depois do encerramento do programa.
try:
    msg = wintypes.MSG ()
    while user32.GetMessageA (byref (msg), None, 0, 0) != 0:
        if msg.message == win32con.WM_HOTKEY:
            action_to_take = HOTKEY_ACTIONS.get (msg.wParam)
            if action_to_take:
                action_to_take ()

        user32.TranslateMessage (byref (msg))
        user32.DispatchMessageA (byref (msg))

finally:
    for id_key in HOTKEYS.keys ():
        user32.UnregisterHotKey (None, id_key)
