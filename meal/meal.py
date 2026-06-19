def main():
    timeinput = input("What time is it ")

    hora = convert(timeinput)



    if 7.0 <= hora <= 8.0:
        print("breakfast time")
    elif 12.0 <= hora <= 13:
        print("lunch time")
    elif 18.0 <= hora <= 19.0:
        print("dinner time")

def convert(time):
    if time.endswith(".pm"):
        realtime = time.replace(".pm", "")
        partes = realtime.split(":")
        horas = float(partes[0]) + 12
        minutos = float(partes[1])
        return horas + (minutos / 60)

    elif time.endswith("am"):
        realtime = time.replace(".am", "")
        partes = realtime.split(":")
        horas = float(partes[0])
        minutos = float(partes[1])
        return horas + (minutos / 60)

    else:
        partes = time.split(":")
        horas = float(partes[0])
        minutos = float(partes[1])
        return horas + (minutos / 60)


main()
