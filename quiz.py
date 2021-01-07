from qustions import Qustion
qustion_promt = ["what is the color of apple\n" "a)red\green\n" "b)blue\n" "c)black\n" "d)brown\n",
                 "how many colour in rainbow\n"  "a)seven\n" "b)nine\n" "c)eight\n" "d)eleven\n",
                 "how many hour in one day\n" "a)7\n" "b)9\n" "c)8\n" "d)24\n"
]
qustions = [
    Qustion(qustion_promt[0], "a"),
    Qustion(qustion_promt[1], "a"),
    Qustion(qustion_promt[2], "d")
]
def run_test (qustions):
    score =0
    for qustion in qustions:
        answer = input(qustion.promte)
        if answer == qustion.answer:
            score+=1
            print("you got" + str(score) + "/" + str(len(qustions)) + "correct")

run_test(qustions)