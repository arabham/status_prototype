from cx_Freeze import setup, Executable

base = None    

executables = [Executable("B1UpChecker.py", base=base)]

packages = ["idna","pysftp"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "B1 Status",
    options = options,
    version = "0.1a",
    description = 'Check status of building ones rigs.',
    executables = executables
)