def main():
    info = input("")

    if "😐" in info:
        infor = info.replace("😐", ":)")
        print(infor)

    elif "🙁" in info:
        infor = info.replace("🙁", ":(")
        print(info)

main()
