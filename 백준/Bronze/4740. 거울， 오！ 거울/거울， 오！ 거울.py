while True:
    userInput = input()

    if userInput == "***":
        break

    # print(userInput[::-1]) 로 바로 끝낼 수도 있음

    for s in range(len(userInput), 0, -1):
        print(userInput[s-1], end="")
    print()
