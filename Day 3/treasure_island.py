
print("""
        __ _.--..--._ _
    .-' _/   _/\_   \\_'-.
   |__ /   _/\__/\_   \\__|
   |___/\\_\\__/  \\___|
           \\__/
            \\__/
             \\__/
              \\__/
           ____\\__/___
        . - '             ' -.
       /                      \\
~~~~~~~  ~~~~~ ~~~~~  ~~~ ~~~  ~~~~~
  ~~~   ~~~~~   ~!~~   ~~ ~  ~ ~ ~
""")
print("Welcome to Story Island")
print("Will you find the treasure or meet your death!")
print("You are on the island at a crossroads, you must choose right or left.")

user_choice = input()

if user_choice.lower() == "left":

    print("You have found yourself in a large pond")
    print("Will you swim to shore or wait in the water?")

    user_choice = input()

    if user_choice.lower() == "wait":

        print("You waited a while and a turtle helped guide you too shore.")
        print("Upon reaching the shore you find three doors")
        print("A blue door")
        print("A yellow door")
        print("A red door")
        print("Which will you enter?")
        user_choice = input()

        if user_choice.lower() == "yellow":

            exit("You found the treasure. Game Won!")

        elif user_choice.lower() == "red":
            exit("As you entered you were set ablaze and burned to death. Game Over!")
        else:
            exit("As you entered you were attacked by tigers and eaten. Game Over!")

    else:
        exit("You were attacked by trout and eaten. Game Over!")


else:
    exit("You fell in a whole and died.\n Game Over!")


