command = ""
engine_state = 0
while True:
    command = input("> ").lower()
    if command == "start" and engine_state == 0:
        print("car started....")
        engine_state = 1
    elif command == "start" and engine_state == 1:
        print("Car is alread running")
    elif command == "stop" and engine_state == 1:
        print("car stopped")
        engine_state = 0
    elif command == "stop" and engine_state == 0:
        print("Car is already off")
    elif command == "help":
        print("start - to start the car\nstop - to stop the car\nquit - to finish")
    elif command == "quit":
        break
else:
    print("i dont understand")