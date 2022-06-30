# Inspired by: https://twinfinite.net/2020/08/hardest-halo-trivia-quiz/

questions = {
    "On what planet did humans first encounter the Covenant?": {"answer": "Harvest",
                                                                "options": ["Harvest", "Earth", "Reach", "Onyx"]},

    "What's the Arbiter's real name?": {"answer": "Thel 'Vadam",
                                        "options": ["Thal 'Vadem", "Thel 'Vadam", "Thel 'Vadam", "Thele 'Vaddon"]},

    "When does Halo 3: ODST take place?": {"answer": "Between Halo 2 and Halo 3",
                                           "options": ["Between Halo: Reach and Halo 1", "Between Halo 1 and Halo 2", "Between Halo 3 and Halo 4", "Between Halo 2 and Halo 3"]},

    "On Noble Team, who is the only Spartan-II?": {"answer": "Jorge",
                                                   "options": ["Jorge", "Noble Six", "Carter", "Kat", "Emile", "Jun"]},

    "What is Cortana's AI serial number?": {"answer": "CTN 0452-9",
                                            "options": ["CTN 0429-1", "CTN 1178-3", "CTN 8271-2", "CTN 0452-9"]},

    "According to the Covenant's religion, what is The Great Journey?": {"answer": "An ascension to godhood",
                                                                         "options": ["An ascension to godhood", "The journey to the Ark", "A pilgrimage to specific planets", "A journey across the galaxy"]},

    "After creation, rampancy in Human Artificial Intelligence generally begins when?": {"answer": "Seven years into their lifespan",
                                                                                         "options": ["Four years into their lifespan", "Six years into their lifespan", "Seven years into their lifespan", "Five years into their lifespan"]},

    "What weapon was used to kill Kat in Halo: Reach?": {"answer": "A Needle Rifle",
                                                         "options": ["A Needle Rifle", "A Brute Shot", "A Beam Rifle", "A Needler"]},

    "What was the last test Catherine Halsey gave to a young John-117 to decide if he'd be conscripted into the Spartan-II program?": {"answer": "A coin flip",
                                                                                                                                       "options": ["A math puzzle", "A game of rock, paper, scissors", "A coin flip", "A riddle"]},

    "What designation is given to Spartan-IIs after they die?": {"answer": "Missing in Action (MIA)",
                                                                 "options": ["Killed in Action (KIA)", "Wounded in Action (WIA)", "Missing in Action (MIA)", "Prisoner of War (POW)"]}
}

scores = 0
answer = " "

while answer != "quit":
    print("Welcome to the Halo Quiz!\n")
    for question, answer in questions.items():
        print(question)
        print()
        for i, option in enumerate(answer["options"]):
            print(i, option)
            print()
        choice = input("Enter a number or type quit to exit:\n")
        if choice == "quit":
            print("Goodbye! Thanks for playing!")
            exit()
        elif choice.isdigit():
            choice = int(choice)
            if choice < len(answer["options"]):
                if answer["options"][choice] == answer["answer"]:
                    scores += 1
                    print()
                    print("Correct!\n")
                else:
                    print("Incorrect")
                    # print the correct answer
                    print("The correct answer is:", answer["answer"])
                    print()
            else:
                print("Invalid choice. I asked for a valid integer answer and you either gave me a string or a number that is out of range, so you don't get a point for this question.")

        else:
            print("Invalid choice. I asked for a valid integer answer and you either gave me a string or a number that is out of range, so you don't get a point for this question.")

    # Calculate the total number of questions and print the score
    if scores == len(questions):
        print("You got all correct! You are a true Spartan!")
        exit()
    elif scores == 0:
        print("You got no correct answers at all. You are a Grunt!")
        exit()
    else:
        print("You got", scores, "correct out of",
              len(questions), "questions.")
        exit()
