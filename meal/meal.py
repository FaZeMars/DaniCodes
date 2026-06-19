def main():
    timeinput = input("What time is it ")
    hora = convert(time)
    if hora.endswith(".pm"):
       int((hora.replace(".pm", "")) + 12.0


    if 7.0 <= hora <= 8.0:
        print("breakfast time")
    elif 12.0 <= hora <= 13:
        print("lunch time")
    elif 18.0 <= hora <= 19.0:
        print("dinner time")

def convert(time):
    partes = time.split(":")
    horas = float(partes[0])
    minutos = float(partes[1])
    return horas + (minutos / 60)


main()
