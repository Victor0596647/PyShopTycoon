import time
import keyboard
from os import system
from player import Player


class Game:

    def __init__(self):
        self.vsavestrt = 'start_shoptyc::'
        self.user = Player()

    def start(self):
        system("CLS")
        print("+--------------------------------------+")
        print("             Shop Tycoon")
        print("+--------------------------------------+\n")
        print("> [1] New Game")
        print("> [2] Load Game")
        print("> [3] Show Saves")
        print("> [4] Options")
        print("> [5] Quit\n")
        print("+--------------------------------------+")

        while True:
            inp = input("> ")
            if inp == '1':
                self.new_game()
            elif inp == '2':
                self.load_game()
            elif inp == '3':
                self.display_saves()
            elif inp == '4':
                print(self.user.get_player_name())
            elif inp == '5':
                quit()
            else:
                print("INPUT ERROR")

    # File Handling
    def new_game(self):
        system("CLS")
        userdata = []
        self.display_saves()
        print("Which save do you want to select to create a new game?")
        print("save 1, save 2, or save 3")
        while True:
            inp = input("> ")
            if inp.endswith("1"):
                file_open = open("./shop0.sav", "w")
                file_open.write(self.vsavestrt)
                userdata.append(input("What is your name: "))
                userdata.append(
                    input("What would you like to name your Company: "))
                file_open.write("\nplayer:: " + userdata[0])
                file_open.write("\ncomp:: " + userdata[1])
                file_open.close()
                self.user.create_player(userdata[0], userdata[1], 1000)
                userdata.clear()
                break

            if inp.endswith("2"):
                file_open = open("./shop1.sav", "w")
                file_open.write(self.vsavestrt)
                userdata.append(input("What is your name: "))
                userdata.append(
                    input("What would you like to name your Company: "))
                file_open.write("\n" + "player:: " + userdata[0])
                file_open.write("\ncomp:: " + userdata[1])
                file_open.close()
                self.user.create_player(userdata[0], userdata[1], 1000)
                userdata.clear()
                break

            if inp.endswith("3"):
                file_open = open("./shop2.sav", "w")
                file_open.write(self.vsavestrt)
                userdata.append(input("What is your name: "))
                userdata.append(
                    input("What would you like to name your Company: "))
                file_open.write("\nplayer:: " + userdata[0])
                file_open.write("\ncomp:: " + userdata[1])
                file_open.close()
                self.user.create_player(userdata[0], userdata[1], 1000)
                userdata.clear()
                break
        self.start()

    def load_game(self):
        system("CLS")
        self.display_saves()
        userdata = []
        file_open = ''
        print("Which Save Slot do you want to load?\nSave 1, Save 2, or Save 3")
        while True:
            inp = input("> ")

            if inp.endswith("1"):
                if self.check_valid_saves("./shop0.sav") == False:
                    file_open = open("./shop0.sav", "r")
                    file_open.readline()
                    for data in file_open.readlines():
                        userdata.append(data)

                    for i in range(2):
                        index = userdata[i].split(':: ', 1)
                        if index[0] == "player":
                            self.user.set_player_name(
                                index[1].partition("\n")[0])
                        if index[0] == "comp":
                            self.user.set_company(index[1].partition("\n")[0])
                        else:
                            pass
                        i += 1
                    print("\n======Loaded Save======")
                    print("Player: " + self.user.get_player_name())
                    print("Company: " + self.user.get_company())
                    print("=======================\n")
                    time.sleep(3)
                    file_open.close()
                    userdata.clear()
                    break
                else:
                    print("Save File Doesn't Exist!")
                    time.sleep(2)
                    break

            if inp.endswith("2"):
                if self.check_valid_saves("./shop1.sav") == False:
                    file_open = open("./shop1.sav", "r")
                    file_open.readline()
                    for data in file_open.readlines():
                        userdata.append(data)

                    for i in range(2):
                        index = userdata[i].split(':: ', 1)
                        if index[0] == "player":
                            self.user.set_player_name(
                                index[1].partition("\n")[0])
                        if index[0] == "comp":
                            self.user.set_company(index[1].partition("\n")[0])
                        else:
                            pass
                        i += 1
                    print("\n======Loaded Save======")
                    print("Player: " + self.user.get_player_name())
                    print("Company: " + self.user.get_company())
                    print("=======================\n")
                    time.sleep(3)
                    file_open.close()
                    userdata.clear()
                    break
                else:
                    print("Save File Doesn't Exist!")
                    time.sleep(2)
                    break

            if inp.endswith("3"):
                if self.check_valid_saves("./shop2.sav") == False:
                    file_open = open("./shop2.sav", "r")
                    file_open.readline()
                    for data in file_open.readlines():
                        userdata.append(data)

                    for i in range(2):
                        index = userdata[i].split(':: ', 1)
                        if index[0] == "player":
                            self.user.set_player_name(
                                index[1].partition("\n")[0])
                        if index[0] == "comp":
                            self.user.set_company(index[1].partition("\n")[0])
                        else:
                            pass
                        i += 1
                    print("\n======Loaded Save======")
                    print("Player: " + self.user.get_player_name())
                    print("Company: " + self.user.get_company())
                    print("=======================\n")
                    time.sleep(3)
                    file_open.close()
                    userdata.clear()
                    break
                else:
                    print("Save File Doesn't Exist!")
                    time.sleep(2)
                    break
        self.start()

    def display_saves(self):
        file_open = ''
        for i in range(3):
            try:
                result = self.check_valid_saves("./shop{0}.sav".format(str(i)))
                if result == False:
                    file_open = open("./shop{0}.sav".format(str(i)))
                    print("\n=================\n[shop{0}.sav]".format(str(i)))
                    file_open.readline()
                    for data in file_open.readlines():
                        print(data)
                elif result == True:
                    print(
                        "=================\n[shop{0}.sav]\nNot A Valid Save File".format(str(i)))
                else:
                    print(
                        "=================\n[shop{0}.sav]\nNo Save File Found".format(str(i)))
                if i == 2:
                    print("=================\n")
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
            return None
