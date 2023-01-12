from Controller.Ctrl_Usuario import Ctrl_Usuario
import os

objCtrl_Usuario = Ctrl_Usuario()

os.system("cls")

if objCtrl_Usuario.usuario_existente():
    while True:
        objUsuario  = objCtrl_Usuario.set_credentials()
        registro = objCtrl_Usuario.validar_password(objUsuario)
        if objCtrl_Usuario.is_ok_password(registro): break
else:
    objCtrl_Usuario.agregar_usuario()

while True:
    objCtrl_Usuario.showMenu()
    opcion_seleccionada = objCtrl_Usuario.choose_operation()
    is_opcionValida = objCtrl_Usuario.validar_opcion(opcion_seleccionada)
    if is_opcionValida:
        is_finPrograma = objCtrl_Usuario.ejecutar_operacion_seleccionada(opcion_seleccionada)
        if is_finPrograma:
            break
    else:
        os.system("cls")
        print("\n[x] Opcion Invalida [x]")