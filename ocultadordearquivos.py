import ctypes

pasta = input("Digite o caminho da pasta a ser ocultada ex ")

atributo_ocultar = 0x02

retorno = ctypes.windll.kernel32.SetFileAttributesW('ocultar.txt', atributo_ocultar)

if retorno:
    print('arquivo foi ocultado')
else:
    print("arquivo não foi ocultado.")