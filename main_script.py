# Andrew Ingrassia
# GUI: Risk Dice Roll Simulator
# PySide6 + Qt Designer


import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from main_ui import Ui_MainWindow
from random import randint


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # SINGLE TAB
        self.ui.roll_btn.pressed.connect(self.clear_roll_output)                # Clears previous result when pressed
        self.ui.roll_btn.released.connect(self.roll_btn)                        # Initiates single roll when released
        self.ui.atk_btn_1.clicked.connect(self.atk_btn_1)                       # Dice button connections...
        self.ui.atk_btn_2.clicked.connect(self.atk_btn_2)
        self.ui.atk_btn_3.clicked.connect(self.atk_btn_3)
        self.ui.def_btn_1.clicked.connect(self.def_btn_1)
        self.ui.def_btn_2.clicked.connect(self.def_btn_2)
        self.atk_list = []                                                      # SINGLE dice container (atk)
        self.def_list = []                                                      # SINGLE dice container (def)

        # ONSLAUGHT TAB
        self.ui.onslaught_btn.pressed.connect(self.clear_onslaught_output)      # Clears previous result when pressed
        self.ui.onslaught_btn.released.connect(self.onslaught_btn)              # Initiates onslaught roll when released
        self.ui.atk_army_total.valueChanged.connect(self.atk_available_armies)  # Updates current atk army total
        self.ui.def_army_total.valueChanged.connect(self.def_available_armies)  # Updates current def army total
        self.onslaught_atk_dice = []                                            # ONSLAUGHT dice container (atk)
        self.onslaught_def_dice = []                                            # ONSLAUGHT dice container (def)
        self.atk_total_armies = 0                                               # Current atk army total
        self.def_total_armies = 0                                               # Current def army total
        self.atk_army_losses = 0                                                # Post-ONSLAUGHT atk losses
        self.def_army_losses = 0                                                # Post-ONSLAUGHT def losses

    def atk_btn_1(self):
        """ When atk_btn_1 is clicked, atk_dice_num label is updated to read "1". """
        self.ui.atk_dice_num.setText("1")

    def atk_btn_2(self):
        """ When atk_btn_2 is clicked, atk_dice_num label is updated to read "2". """
        self.ui.atk_dice_num.setText("2")

    def atk_btn_3(self):
        """ When atk_btn_3 is clicked, atk_dice_num label is updated to read "3". """
        self.ui.atk_dice_num.setText("3")

    def def_btn_1(self):
        """ When def_btn_1 is clicked, def_dice_num label is updated to read "1". """
        self.ui.def_dice_num.setText("1")

    def def_btn_2(self):
        """ When def_btn_2 is clicked, def_dice_num label is updated to read "2". """
        self.ui.def_dice_num.setText("2")

    def clear_roll_output(self):
        """ Clears previous output when ROLL button is pressed. """

        # I added this function because when 2 subsequent outputs were identical ("ATK -1" ---> "ATK -1"), it looked as
        # though nothing changed. Having the previous result disappear briefly before the new result is displayed
        # creates a lovely "flicker" that serves as a reassuring visual cue for the user. I added the same "flicker"
        # to the ONSLAUGHT button.

        self.ui.atk_roll_result.setText("")
        self.ui.def_roll_result.setText("")

    def roll_btn(self):
        """ Runs the roll_sim function when ROLL button is released. """
        self.roll_sim()

    def roll_sim(self):
        """
        Simulates a single roll of the dice.
        Displays output within atk_roll_result and def_roll_result.
        Output represents resulting ATK and DEF army losses.
        """

        if self.ui.def_dice_num.text() == "1":
            self.def_list = [randint(1, 6)]
            if self.ui.atk_dice_num.text() == "1":
                self.atk_list = [randint(1, 6)]
                if self.def_list[0] >= self.atk_list[0]:
                    self.ui.atk_roll_result.setText("ATK -1")
                    self.ui.def_roll_result.setText("")
                else:
                    self.ui.atk_roll_result.setText("")
                    self.ui.def_roll_result.setText("DEF -1")
            elif self.ui.atk_dice_num.text() == "2":
                self.atk_list = sorted([randint(1, 6), randint(1, 6)])
                if (self.def_list[0] >= self.atk_list[0]) and (self.def_list[0] >= self.atk_list[1]):
                    self.ui.atk_roll_result.setText("ATK -1")
                    self.ui.def_roll_result.setText("")
                else:
                    self.ui.atk_roll_result.setText("")
                    self.ui.def_roll_result.setText("DEF -1")
            elif self.ui.atk_dice_num.text() == "3":
                self.atk_list = sorted([randint(1, 6), randint(1, 6), randint(1, 6)])
                if (self.def_list[0] >= self.atk_list[0]) and \
                        (self.def_list[0] >= self.atk_list[1]) and \
                        (self.def_list[0] >= self.atk_list[2]):
                    self.ui.atk_roll_result.setText("ATK -1")
                    self.ui.def_roll_result.setText("")
                else:
                    self.ui.atk_roll_result.setText("")
                    self.ui.def_roll_result.setText("DEF -1")

        elif self.ui.def_dice_num.text() == "2":
            self.def_list = sorted([randint(1, 6), randint(1, 6)])
            if self.ui.atk_dice_num.text() == "1":
                self.atk_list = [randint(1, 6)]
                if (self.atk_list[0] <= self.def_list[0]) or (self.atk_list[0] <= self.def_list[1]):
                    self.ui.atk_roll_result.setText("ATK -1")
                    self.ui.def_roll_result.setText("")
                else:
                    self.ui.atk_roll_result.setText("")
                    self.ui.def_roll_result.setText("DEF -1")
            elif self.ui.atk_dice_num.text() == "2":
                self.atk_list = sorted([randint(1, 6), randint(1, 6)])
                if (self.atk_list[0] <= self.def_list[0]) and (self.atk_list[1] <= self.def_list[1]):
                    self.ui.atk_roll_result.setText("ATK -2")
                    self.ui.def_roll_result.setText("")
                elif (self.atk_list[0] > self.def_list[0]) and (self.atk_list[1] > self.def_list[1]):
                    self.ui.atk_roll_result.setText("")
                    self.ui.def_roll_result.setText("DEF -2")
                else:
                    self.ui.atk_roll_result.setText("ATK -1")
                    self.ui.def_roll_result.setText("DEF -1")
            elif self.ui.atk_dice_num.text() == "3":
                self.atk_list = sorted([randint(1, 6), randint(1, 6), randint(1, 6)])
                if (self.atk_list[2] <= self.def_list[1]) and (self.atk_list[1] <= self.def_list[0]):
                    self.ui.atk_roll_result.setText("ATK -2")
                    self.ui.def_roll_result.setText("")
                elif (self.atk_list[2] > self.def_list[1]) and (self.atk_list[1] > self.def_list[0]):
                    self.ui.atk_roll_result.setText("")
                    self.ui.def_roll_result.setText("DEF -2")
                else:
                    self.ui.atk_roll_result.setText("ATK -1")
                    self.ui.def_roll_result.setText("DEF -1")

    def clear_onslaught_output(self):
        """ Clears previous ONSLAUGHT output. """
        self.ui.atk_onslaught_result.clear()
        self.ui.def_onslaught_result.clear()

    def onslaught_btn(self):
        """ Runs the onslaught_result_reset and onslaught_sim function when the ONSLAUGHT button is released. """
        self.onslaught_result_reset()
        self.onslaught_sim()

    def atk_available_armies(self):
        """ Sets the current value of the atk_army_total spinbox. """
        self.atk_total_armies = int(self.ui.atk_army_total.value())

    def def_available_armies(self):
        """ Sets the current value of the def_army_total spinbox. """
        self.def_total_armies = int(self.ui.def_army_total.value())

    def army_total_reset(self):
        """ Resets atk_army_total and def_army_total to 0. """
        self.ui.atk_army_total.setValue(0)
        self.ui.def_army_total.setValue(0)

    def onslaught_result_reset(self):
        """ Resets atk_onslaught_result and def_onslaught_result army loss tallies to 0. """
        self.atk_army_losses = 0
        self.def_army_losses = 0

    def A2D0(self):
        """
        Attacker loses 2 armies.
        Subtracts 2 from current atk army total.
        Adds 2 to current tally of atk army losses.
        """
        self.atk_total_armies -= 2
        self.atk_army_losses += 2

    def A1D0(self):
        """
        Attacker loses 1 army.
        Subtracts 1 from current atk army total.
        Adds 1 to current tally of atk army losses.
        """
        self.atk_total_armies -= 1
        self.atk_army_losses += 1

    def A0D2(self):
        """
        Defender loses 2 armies.
        Subtracts 2 from current def army total.
        Adds 2 to current tally of def army losses.
        """
        self.def_total_armies -= 2
        self.def_army_losses += 2

    def A0D1(self):
        """
        Defender loses 1 army.
        Subtracts 1 from current def army total.
        Adds 1 to current tally of def army losses.
        """
        self.def_total_armies -= 1
        self.def_army_losses += 1

    def A1D1(self):
        """
        Attacker and defender lose 1 army each.
        Subtracts 1 each from current atk and def army totals.
        Adds 1 each to current tallies of atk and def army losses.
        """
        self.atk_total_armies -= 1
        self.atk_army_losses += 1
        self.def_total_armies -= 1
        self.def_army_losses += 1

    def onslaught_sim(self):
        """
        Utilizes the numbers provided by the user in the atk and def army total spinboxes.
        Initiates a cascade of rolls that ends when either of the following conditions is met:
            1. The attacker's total army count = 1
            2. The defender's total army count = 0
        Displays the total army losses for both attacker and defender.
        """

        # 3v2 rolls
        while (self.atk_total_armies >= 3) and (self.def_total_armies >= 2):
            self.onslaught_atk_dice = sorted([randint(1, 6), randint(1, 6), randint(1, 6)])
            self.onslaught_def_dice = sorted([randint(1, 6), randint(1, 6)])
            if (self.onslaught_atk_dice[2] <= self.onslaught_def_dice[1]) and \
                    (self.onslaught_atk_dice[1] <= self.onslaught_def_dice[0]):
                self.A2D0()
            elif (self.onslaught_atk_dice[2] > self.onslaught_def_dice[1]) and \
                    (self.onslaught_atk_dice[1] > self.onslaught_def_dice[0]):
                self.A0D2()
            else:
                self.A1D1()

        # 2v2 rolls
        while (self.atk_total_armies == 3) and (self.def_total_armies == 2):
            self.onslaught_atk_dice = sorted([randint(1, 6), randint(1, 6)])
            self.onslaught_def_dice = sorted([randint(1, 6), randint(1, 6)])
            if (self.onslaught_atk_dice[0] <= self.onslaught_def_dice[0]) and \
                    (self.onslaught_atk_dice[1] <= self.onslaught_def_dice[1]):
                self.A2D0()
            elif (self.onslaught_atk_dice[0] > self.onslaught_def_dice[0]) and \
                    (self.onslaught_atk_dice[1] > self.onslaught_def_dice[1]):
                self.A0D2()
            else:
                self.A1D1()

        # 1v1 rolls
        while (self.atk_total_armies == 2) and (self.def_total_armies == 1):
            self.onslaught_atk_dice = [randint(1, 6)]
            self.onslaught_def_dice = [randint(1, 6)]
            if self.onslaught_def_dice[0] >= self.onslaught_atk_dice[0]:
                self.A1D0()
            else:
                self.A0D1()

        # 1v2 rolls
        while (self.atk_total_armies == 2) and (self.def_total_armies >= 2):
            self.onslaught_atk_dice = [randint(1, 6)]
            self.onslaught_def_dice = sorted([randint(1, 6), randint(1, 6)])
            if (self.onslaught_atk_dice[0] <= self.onslaught_def_dice[0]) or \
                    (self.onslaught_atk_dice[0] <= self.onslaught_def_dice[1]):
                self.A1D0()
            else:
                self.A0D1()

        # 2v1 rolls
        while (self.atk_total_armies == 3) and (self.def_total_armies == 1):
            self.onslaught_atk_dice = sorted([randint(1, 6), randint(1, 6)])
            self.onslaught_def_dice = [randint(1, 6)]
            if (self.onslaught_def_dice[0] >= self.onslaught_atk_dice[0]) and \
                    (self.onslaught_def_dice[0] >= self.onslaught_atk_dice[1]):
                self.A1D0()
            else:
                self.A0D1()

        # 3v1 rolls
        while (self.atk_total_armies >= 4) and (self.def_total_armies == 1):
            self.onslaught_atk_dice = sorted([randint(1, 6), randint(1, 6), randint(1, 6)])
            self.onslaught_def_dice = [randint(1, 6)]
            if (self.onslaught_def_dice[0] >= self.onslaught_atk_dice[0]) and \
                    (self.onslaught_def_dice[0] >= self.onslaught_atk_dice[1]) and \
                    (self.onslaught_def_dice[0] >= self.onslaught_atk_dice[2]):
                self.A1D0()
            else:
                self.A0D1()

        # Display roll results
        self.ui.atk_onslaught_result.setText(f"ATK -{str(self.atk_army_losses)}")
        self.ui.def_onslaught_result.setText(f"DEF -{str(self.def_army_losses)}")

        # Runs army_total_reset function (necessary to prevent previous result from being added to current result)
        self.army_total_reset()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Windows')
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
