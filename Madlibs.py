print("Pick your game of Madlibs:\n1 - A wild night out\n2 - The Worst First Date\n3 - The Worst Job Ever\n4 - A Disaster at the Wedding\n5 - A Nightmare at the Doctor’s Office")

game_out= "Result.txt"

options =["1","2","3","4","5"]
while True:
    pick = input(f"Pick a number between 1 and {len(options)}: ")
    if pick in options:
        match pick:
            case "1":
                game = "1-A Wild Night Out.txt"
                question = "1-A_Wild_Night_Out_Questions.txt"
            case "2":
                game = "2-The Worst First Date.txt"
                question = "2-The Worst First Date Questions.txt"
            case "3":
                game = "3-The Worst Job Ever.txt"
                question = "3-The Worst Job Ever Questions.txt"
            case "4":
                game = "4-A Disaster at the Wedding.txt"
                question = "4-A Disaster at the Wedding Questions.txt"
            case "5":
                game = "5-A Nightmare at the Doctor’s Office.txt"
                question = "5-A Nightmare at the Doctor’s Office Questions.txt"    
        break
    print("Sorry, thats not an options")

blank = open(game,"r", encoding="utf-8").read()
list_questions = open(question)

list_questions = [line.strip().replace("_","") for line in list_questions]


one = input(list_questions[0])
two = input(list_questions[1])
three = input(list_questions[2])
four = input(list_questions[3])
five = input(list_questions[4])
six = input(list_questions[5])
seven = input(list_questions[6])
eight = input(list_questions[7])
nine = input(list_questions[8])
ten = input(list_questions[9])


new = blank.replace("1", one)
new = new.replace("2", two)
new = new.replace("3", three)
new = new.replace("4", four)
new = new.replace("5", five)
new = new.replace("6", six)
new = new.replace("7", seven)
new = new.replace("8", eight)
new = new.replace("9", nine)
new = new.replace("0", ten)

print(new)
filled =open(game_out, "w", encoding="utf-8").write(new)