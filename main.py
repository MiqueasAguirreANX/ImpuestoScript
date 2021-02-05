# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as font
import tkinter.messagebox as msg


def main():
    def calcular():
        try:
            _sueldo = int(sueldo.get())
            _antiguedad = int(antiguedad.get())
            _anios = int(anios.get())
            _presentismo = int(presentismo.get())
            _hijos = int(hijos.get())
            _adicionales = int(adicionales.get())
            _estado_civil = estado_civil.get()
            _seguro_colectivo = int(seguro_colectivo.get())
            if _hijos >= 2:
                if _estado_civil.lower() == 'casado':
                    if _sueldo >= 119000:
                        _diferencia = _sueldo - 119000
                        _suma = _sueldo + (_sueldo * _antiguedad * _anios / 100) + _presentismo + _adicionales
                        _resta = _sueldo * (17 / 100) + _sueldo / 5 + _seguro_colectivo + (_diferencia*0.35)
                        _neto = _suma - _resta

                        resultado.set(str(_neto))
                    else:
                        _suma = _sueldo + (_sueldo*_antiguedad*_anios/100) + _presentismo + _adicionales
                        _resta = _sueldo*(17/100) + _sueldo/5 + _seguro_colectivo
                        resultado.set(str(_suma-_resta))
                else:
                    if _sueldo >= 104000:
                        _diferencia = _sueldo - 104000
                        _suma = _sueldo + (_sueldo * _antiguedad * _anios / 100) + _presentismo + _adicionales
                        _resta = _sueldo * (17 / 100) + _sueldo / 5 + _seguro_colectivo + (_diferencia*0.35)
                        resultado.set(str(_suma - _resta))
                    else:
                        _suma = _sueldo + (_sueldo * _antiguedad * _anios / 100) + _presentismo + _adicionales
                        _resta = _sueldo * (17 / 100) + _sueldo / 5 + _seguro_colectivo
                        resultado.set(str(_suma - _resta))
            else:
                if _sueldo >= 90000:
                    _diferencia = _sueldo - 90000
                    _suma = _sueldo + (_sueldo * _antiguedad * _anios / 100) + _presentismo + _adicionales
                    _resta = _sueldo * (17 / 100) + _sueldo / 5 + _seguro_colectivo + (_diferencia*0.35)
                    resultado.set(str(_suma - _resta))
                else:
                    _suma = _sueldo + (_sueldo * _antiguedad * _anios / 100) + _presentismo + _adicionales
                    _resta = _sueldo * (17 / 100) + _sueldo / 5 + _seguro_colectivo
                    resultado.set(str(_suma - _resta))
        except Exception as e:
            print(e)
            msg.showerror('Datos invalidos', 'Porfavor ingrese datos validos!')

    # Realizar la calculadora
    app = tk.Tk()
    ventana = tk.Frame(app)
    # Columnas
    # Ganancia
    # 1
    sueldo = tk.StringVar()
    lbl_sueldo = tk.Label(ventana, text='Sueldo')
    lbl_sueldo.grid(column=0, row=0, pady=10)
    txt_sueldo = tk.Entry(ventana, textvariable=sueldo)
    txt_sueldo.grid(column=1, row=0, pady=10)
    # 2
    antiguedad = tk.StringVar()
    lbl_antiguedad = tk.Label(ventana, text='Antiguedad (%)')
    lbl_antiguedad.grid(column=0, row=1, pady=10)
    txt_antiguedad = tk.Entry(ventana, textvariable=antiguedad)
    txt_antiguedad.grid(column=1, row=1, pady=10)
    # 3
    anios = tk.StringVar()
    lbl_anios = tk.Label(ventana, text='Años')
    lbl_anios.grid(column=0, row=2, pady=10)
    txt_anios = tk.Entry(ventana, textvariable=anios)
    txt_anios.grid(column=1, row=2, pady=10)
    # 4
    hijos = tk.StringVar()
    lbl_hijos = tk.Label(ventana, text='Hijos')
    lbl_hijos.grid(column=0, row=2+1, pady=10)
    txt_hijos = tk.Entry(ventana, textvariable=hijos)
    txt_hijos.grid(column=1, row=2+1, pady=10)
    # 5
    presentismo = tk.StringVar()
    lbl_presentismo = tk.Label(ventana, text='Presentismo')
    lbl_presentismo.grid(column=0, row=3+1, pady=10)
    txt_presentismo = tk.Entry(ventana, textvariable=presentismo)
    txt_presentismo.grid(column=1, row=3+1, pady=10)
    # 6
    adicionales = tk.StringVar()
    lbl_adicionales = tk.Label(ventana, text='Adicionales')
    lbl_adicionales.grid(column=0, row=4+1, pady=10)
    txt_adicionales = tk.Entry(ventana, textvariable=adicionales)
    txt_adicionales.grid(column=1, row=4+1, pady=10)
    # separador
    s = ttk.Separator(ventana)
    s.grid(column=2, row=0, rowspan=4)
    
    btn_calcular = tk.Button(ventana, text='Calcular', bg='#4ac', command=calcular,
                             font=font.Font(family='Times', size=18, weight='bold'))
    btn_calcular.grid(column=0, row=6, columnspan=2, ipadx=25, pady=25)
    
    # Descuentos
    # 1
    jubilacion = tk.StringVar()
    lbl_jubilacion = tk.Label(ventana, text='Jubilacion (%)')
    lbl_jubilacion.grid(column=3, row=0, pady=10)
    txt_jubilacion = tk.Entry(ventana, textvariable=jubilacion, state=tk.DISABLED)
    jubilacion.set('11')
    txt_jubilacion.grid(column=4, row=0, pady=10)
    # 2
    pami = tk.StringVar()
    lbl_pami = tk.Label(ventana, text='Pami (%)')
    lbl_pami.grid(column=3, row=2-1, pady=10)
    txt_pami = tk.Entry(ventana, textvariable=pami, state=tk.DISABLED)
    pami.set('3')
    txt_pami.grid(column=4, row=2-1, pady=10)
    # 3
    obra_social = tk.StringVar()
    lbl_obra_social = tk.Label(ventana, text='Obra Social (%)')
    lbl_obra_social.grid(column=3, row=3-1, pady=10)
    txt_obra_social = tk.Entry(ventana, textvariable=obra_social, state=tk.DISABLED)
    obra_social.set('3')
    txt_obra_social.grid(column=4, row=3-1, pady=10)
    # 4
    sindicato = tk.StringVar()
    lbl_sindicato = tk.Label(ventana, text='Sindicato (%)')
    lbl_sindicato.grid(column=3, row=4-1, pady=10)
    txt_sindicato = tk.Entry(ventana, textvariable=sindicato, state=tk.DISABLED)
    sindicato.set('3')
    txt_sindicato.grid(column=4, row=4-1, pady=10)
    # 5
    estado_civil = tk.StringVar()
    lbl_estado_civil = tk.Label(ventana, text='Estado Civil')
    lbl_estado_civil.grid(column=3, row=5-1, pady=10)
    txt_estado_civil = tk.Entry(ventana, textvariable=estado_civil)
    txt_estado_civil.grid(column=4, row=5-1, pady=10)
    # 6
    seguro_colectivo = tk.StringVar()
    lbl_seguro_colectivo = tk.Label(ventana, text='Seguro Colectivo')
    lbl_seguro_colectivo.grid(column=3, row=6-1, pady=10)
    txt_seguro_colectivo = tk.Entry(ventana, textvariable=seguro_colectivo)
    txt_seguro_colectivo.grid(column=4, row=6-1, pady=10)

    resultado = tk.StringVar()
    lbl_resultado = tk.Label(ventana, text='Resultado', font=font.Font(family='Times', size=14))
    lbl_resultado.grid(column=0, row=7, pady=10)
    txt_resultado = tk.Entry(ventana, textvariable=resultado, font=font.Font(family='Times', size=14))
    txt_resultado.grid(column=1, row=7, pady=10)

    ventana.pack(pady=10, padx=50)
    app.title('Calculadora de sueldos')
    app.mainloop()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
