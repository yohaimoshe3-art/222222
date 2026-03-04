num = int(input("enter the number 1-10:"))
match num :
    case 1 :
        print("very quiet")
    case 2 :
        print("quiet")
    case 3 | 4 :
        print("low")

    case 5 :
        print("medium")
    case 6 :
        print("medium high")
    case 7 :
        print("loud")
    case 8 :
        print("very loud")
    case 9 | 10 :
        print("max volume")
    case _ :
        print("invalid volume")

