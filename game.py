from rich import print
from rich.console import Console
from rich.text import Text
from rich.panel import Panel
import time
from os import system
from player import Player
from shop_game import Shop_game

class Game:
    console = Console()
    def __init__(self):
        self.vsavestrt = 'start_shoptyc::'
        self.game = 1
        self.user = Player()

    def titleScreen(self):
        title = Text()
        title.append("███╗   ███╗ █████╗ ██████╗ ██╗  ██╗███████╗████████╗    ████████╗██╗   ██╗ ██████╗ ██████╗  ██████╗ ███╗   ██╗\n")
        title.append("████╗ ████║██╔══██╗██╔══██╗██║ ██╔╝██╔════╝╚══██╔══╝    ╚══██╔══╝╚██╗ ██╔╝██╔════╝██╔═══██╗██╔═══██╗████╗  ██║\n")
        title.append("██╔████╔██║███████║██████╔╝█████╔╝ █████╗     ██║          ██║    ╚████╔╝ ██║     ██║   ██║██║   ██║██╔██╗ ██║\n")
        title.append("██║╚██╔╝██║██╔══██║██╔══██╗██╔═██╗ ██╔══╝     ██║          ██║     ╚██╔╝  ██║     ██║   ██║██║   ██║██║╚██╗██║\n")
        title.append("██║ ╚═╝ ██║██║  ██║██║  ██║██║  ██╗███████╗   ██║          ██║      ██║   ╚██████╗╚██████╔╝╚██████╔╝██║ ╚████║\n")
        title.append("╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝          ╚═╝      ╚═╝    ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝")
        title.stylize("#1F8FFF")
        self.console.print(title)
    
    def start(self):
        inp = ''
        system("CLS")
        print('\n')
        self.titleScreen()
        print(Panel("> [1] New Game\n" + 
                    "> [2] Load Game\n" + 
                    "> [3] Show Saves\n" + 
                    "> [4] Options\n" + 
                    "> [5] Quit",title="Main Menu", width=65))

        while True:
            try:
                inp = int(input("> "))
                
                if inp == 1:
                    self.new_game()
                    break
                elif inp == 2:
                    self.load_game()
                    break
                elif inp == 3:
                    self.display_saves()
                elif inp == 4:
                    print(self.user.get_player_name())
                elif inp == 5:
                    system("CLS")
                else:
                    print(Panel("'" + str(inp) + "'",style="#B3001B",title="Input Error",width=40,title_align="left"))
            except Exception as err:
                print(Panel.fit(str(err),style="#B3001B",title="Error Exception"))

    # File Handling
    def new_game(self):
        system("CLS")
        userdata = []
        self.display_saves()
        print(Panel("Which save do you want to select to create a new game?\nSave [1], Save [2], Save [3] | [4] Cancel"))
        while True:
            try:
                inp = int(input("> "))
                if inp == 1 or inp == 2 or inp == 3:
                    file_open = open("./shop{0}.sav".format(str(inp-1)), "w")
                    file_open.write(self.vsavestrt)
                    print()
                    userdata.append(input("What is your name: "))
                    userdata.append(input("What would you like to name your Company: "))
                    print()
                    file_open.write("\nplayer:: " + userdata[0])
                    file_open.write("\ncomp:: " + userdata[1])
                    file_open.write("\ncash:: " + "1000")
                    file_open.close()
                    self.user.create_player(userdata[0], userdata[1], 1000)
                    print(Panel.fit("Player: " + self.user.get_player_name() +"\nCompany: " + self.user.get_company() + "\nCash: " + self.user.get_cash(),title="Loaded Save {0}".format(str(inp))))
                    time.sleep(2)
                    userdata.clear()
                    self.game = Shop_game(self.user.get_player_name(),self.user.get_company(),self.user.get_cash())
                    break
                elif inp == 4:
                    self.start()
                    break
            except Exception as err:
                print(Panel.fit(str(err),style="#B3001B",title="Error Exception"))

    def load_game(self):
        system("CLS")
        self.display_saves()
        userdata = []
        file_open = ''
        print(Panel("Which save do you want to select to load?\nSave [1], Save [2], or Save [3] | [4] Cancel"))
        while True:
            try:
                inp = int(input("> "))
                if inp == 1 or inp == 2 or inp == 3:
                    if self.check_valid_saves("./shop{0}.sav".format(str(inp-1))) == False:
                        file_open = open("./shop{0}.sav".format(str(inp-1)), "r")
                        file_open.readline()
                        for data in file_open.readlines():
                            userdata.append(data)

                        for i in range(3):
                            index = userdata[i].split(':: ', 1)
                            if index[0] == "player":
                                self.user.set_player_name(index[1].partition("\n")[0])
                            if index[0] == "comp":
                                self.user.set_company(index[1].partition("\n")[0])
                            if index[0] == "cash":
                                self.user.set_cash(int(index[1].partition("\n")[0]))
                            else:
                                pass
                            i += 1
                        print()
                        print(Panel.fit("Player: " + self.user.get_player_name() +"\nCompany: " + self.user.get_company() + "\nCash: " + self.user.get_cash(),title="Loaded Save {0}".format(str(inp))))
                        time.sleep(2)
                        file_open.close()
                        userdata.clear()
                        self.game = Shop_game(self.user.get_player_name(),self.user.get_company(),self.user.get_cash())
                        break
                    else:
                        print("Save File Doesn't Exist!")
                elif inp == 4:
                    self.start()
                    break
            except Exception as err:
                print(Panel.fit(str(err),style="#B3001B",title="Error Exception"))

    def display_saves(self):
        file_open = ''
        for i in range(3):
            try:
                result = self.check_valid_saves("./shop{0}.sav".format(str(i)))
                if result == False:
                    text = Text()
                    file_open = open("./shop{0}.sav".format(str(i)))
                    file_open.readline()
                    for data in file_open.readlines():
                        text.append(data)
                    print(Panel(text,title="shop{0}.sav".format(str(i)),style='green'))
                elif result == True:
                    print(Panel("Not a Valid Save File",title="shop{0}.sav".format(str(i))))
                else:
                    print(Panel("No Save File Found",title="shop{0}.sav".format(str(i))))
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
