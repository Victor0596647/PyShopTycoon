import keyboard
import os


class Game:
    def __init__(self):
        #file_open = open('')
        self.vsavestrt = 'start_shoptyc::'
        pass

    def start(self):
        print("+--------------------------------------+")
        print("             Shop Tycoon")
        print("+--------------------------------------+")
        print()
        print("> [1] New Game")
        print("> [2] Load Game")
        print("> [3] Options")
        print("> [4] Quit")
        print("+--------------------------------------+")

        while True:
            inp = input("> ")
            if inp == '1':
                self.display_saves()
            elif inp == '2':
                self.display_saves()
            elif inp == '3':
                pass
            elif inp == '4':
                quit()
            else:
                pass

    # File Handling
    def new_game(self, file_name):
        file_open = open(file_name, 'w')

        file_open.close()

    def display_saves(self):
        file_open = ''
        for i in range(3):
            try:
                result = self.check_valid_saves("./shop{0}.sav".format(str(i)))
                if result == False:
                    file_open = open("./shop{0}.sav".format(str(i)))
                    print("=================\n[shop{0}.sav]".format(str(i)))
                    file_open.readline()
                    for data in file_open.readlines():
                        print(data)
                elif result == True:
                    print(
                        "=================\n[shop{0}.sav]\nNot A Valid Save File".format(str(i)))
                else:
                    print(
                        "=================\n[shop{0}.sav]\nNo Save File Found".format(str(i)))
                file_open.close()
                i += 1
            except:
                pass

    def check_valid_saves(self, fileName):
        file_open = ''
        index = []
        try:
            file_open = open(fileName, 'r')
            index.append(file_open.readline())
            if index[0].find(self.vsavestrt):
                file_open.close()
                return True
            else:
                return False
        except:
            return "bro"
