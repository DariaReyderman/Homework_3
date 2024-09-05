# START

x: int = int(input("What is the volume level? "))
match x:
    case 0:
        print("Mute")
    case 1 | 2:
        print("Very quiet")
    case 3:
        print("Quiet")
    case 4:
        print("Moderately quiet")
    case 5:
        print("Medium")
    case 6:
        print("Moderately loud")
    case 7:
        print("Loud")
    case 8:
        print("Very loud")
    case 9 | 10:
        print("Extremely loud")

# STOP
