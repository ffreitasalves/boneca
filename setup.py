from cx_Freeze import setup, Executable

setup(
    name = "boneca",
    version = "1.0.0",
    options = {"build_exe": {
        'packages': ["os","sys","ctypes","win32con"],
        'excludes': ['tkinter','tcl','ttk'],
        'include_files': ['boneca.jpg'],
        'include_msvcr': True,
    }},
    executables = [Executable("boneca.py",base="Win32GUI")]
    )