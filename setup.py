import esky.bdist_esky
from esky.bdist_esky import Executable as Executable_Esky
from cx_Freeze import setup, Executable

include_files = ['boneca.jpg','chuck.jpg', 'seu-boneco.jpg']

setup(
    name = 'boneca',
    version = '1.0.2',
    options = {
        'build_exe': {
            'packages': ['os','sys','ctypes','win32con'],
            'excludes': ['tkinter','tcl','ttk'],
            'include_files': include_files,
            'include_msvcr': True,
        },
        'bdist_esky': {
            'freezer_module': 'cx_freeze',
        }
    },
    data_files = include_files,
    scripts = [
        Executable_Esky(
            "boneca.py",
            gui_only = True,
            #icon = XPTO #Coloque um icone aqui se quiser ,
            ),
    ],
    executables = [Executable('boneca.py',base='Win32GUI')]
    )