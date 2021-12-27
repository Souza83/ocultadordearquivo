import ctypes

pasta = input("Digite a pasta a ser ocultada ex (C:/pasta): ")

atributo_ocultar = 0x02  # Atributo exdecimal para ocultar

retorno = ctypes.windll.kernel32.SetFileAttributesW(pasta, atributo_ocultar)

if retorno:
    print("Arquivo ocultado!")
else:
    print("Arquivo não ocultado!")
