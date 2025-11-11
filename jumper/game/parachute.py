
class Parachute:
    """The role of this class is to show the parachute picture
    based on how well the user responds correctly"""

    def __init__(self):
        """constructor: fragment of lines, then the lines are stored in the list line with the order of the picture"""

        self._line1 = " / \\ "
        self._line2 = " /!\\ "
        self._line3 = "  o  "
        self._line4 = " \\ / "
        self._line5 = "\\   /"
        self._line6 = " ___ "
        self._line7 = "/   \\ "
        self._line8 = " ___ "
        self._line = [self._line8, self._line7, self._line6, self._line5, self._line4, self._line3, self._line2, self._line1] 

    def _show(self, uncorrect_answer_count):
        """
            It shows the fragments of the parachute based the uncorrect_answer_count
            For each incorrect answer, one fragment of the parachute will be removed from the top to the bottom
            when the uncorrect_answer_count is equal to 3, it will be game over and the self._line3 will turns into "  x  "
        """

        if uncorrect_answer_count == 3:
            self._line[5] = "  x  "
        for i in range(8):
            if i <= (7 - uncorrect_answer_count):
                continue
            print(self._line[i])

            


