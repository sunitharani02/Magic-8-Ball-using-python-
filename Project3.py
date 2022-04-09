#import modules
import random, sys, csv

class magic8ball:
    #initial function
    def __init__(self, name):
        self.__name = name
        self.__mQuestions = []
        self.__start_game()

#private function to start game
    def __start_game(self):
        #list of proper 8 ball responses
        mResponses = ["IT IS CERTAIN", "YOU MAY RELY ON IT", "AS I SEE IT, YES",
             "OUTLOOK LOOKS GOOD", "MOST LIKELY", "IT IS DECIDELY SO",
             "WITHOUT A DOUBT", "YES, DEFENITELY"]

        #loop condition
        lQuestions = True

        #print welcome message
        print("Welcome " + self.__name)

        #run continues loop
        while lQuestions:
            #get uestions from user
            mQues = input("Please enter a question: ")

            #pick random response
            mRespond = mResponses[random.randint(0,7)]

            #exit if no question and user presses enter
            #else append question to mQuestions
            if mQues == "":
                print("Thankyou for playing!")
                #call function to write questions to .csv file
                self.__write_questions()
                sys.exit()
            else:
                print(mRespond)
                self.__mQuestions.append(mQues)

#function writing questions to .csv file
    def __write_questions(self):
        f = open("magic_questions.csv", "a", newline="")
        wrt = csv.writer(f)
        for q in self.__mQuestions:
            wrt.writerow([q])
        f.close()

#To run,
#new8 = magic8ball("Lucy")
