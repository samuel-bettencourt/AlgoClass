
class Sequences:
    def __init__(self):
        self.first_sequence = input("ENTER FIRST CHARACTER STRING: ")
        self.second_sequence = input("ENTER SECOND CHARACTER STRING: ")
        self.first_array = list(self.first_sequence)
        self.second_array = list(self.second_sequence)
        self.gap_cost = int(input("ENTER THE GAP COST(int): "))
        self.mismatch_cost = int(input("ENTER THE MISMATCH COST(int): "))
        rows = len(self.first_array)+1
        cols = len(self.second_array)+1
        self.scores = []
        for i in range(rows):
            self.scores += [[0] * cols] #matrix holds subproblems

        for i in range(rows):
            self.scores[i][0] = 0

        for j in range(cols):
            self.scores[i][0] = 0
        rounds_scores = [0, 0, 0]
        for i in range(rows-1):
            for j in range(cols-1):
                if self.first_array[i] == self.second_array[j]:
                    rounds_scores[0] = self.scores[i][j] + 1
                else:
                    rounds_scores[0] = self.scores[i][j] - self.mismatch_cost
                rounds_scores[1] = self.scores[i][j+1] - self.gap_cost
                rounds_scores[2] = self.scores[i+1][j] - self.gap_cost
                round_max = max(rounds_scores)
                self.scores[i+1][j+1] = round_max   #the diagnal is result of highest score of surrounding entries
        print("\n\n\n")
        for row in self.scores:     #print 2d matrix of all scores
            print(row)
        self.get_optimal()          #trace back through the matrix from bottom right to top left
        print("\n\n")

    def get_optimal(self):
        i = len(self.first_array)
        j = len(self.second_array)
        first = []
        second = []
        while i > 0 and j > 0:
            current_score = self.scores[i][j]
            previous_i_j = self.scores[i-1][j-1]
            previous_i = self.scores[i-1][j]
            previous_j = self.scores[i][j-1]
            if current_score == previous_i_j + 1:       #then there was a match
                first.append(self.first_array[i-1])
                second.append(self.second_array[j-1])
                i -= 1
                j -= 1
            elif current_score == previous_i_j - self.mismatch_cost:
                first.append(self.first_array[i - 1])
                second.append(self.second_array[j - 1])
                i -= 1
                j -= 1
            elif current_score == previous_j - self.gap_cost:
                first.append("-")
                second.append(self.second_array[j-1])
                j -= 1
                i -= 1
            elif current_score == previous_i - self.gap_cost:
                first.append(self.first_array[i-1])
                second.append("-")
                i -= 1
                j -= 1

        if i > 0:
            while i > 0:
                first.append(self.first_array[i-1])
                second.append("-")
                i -= 1
        elif j > 0:
            while j > 0:
                first.append("-")
                second.append(self.second_array[j-1])
                j -= 1
        first = "".join(first)[::-1]        #converts to string and reverses the order of characters
        second = "".join(second)[::-1]
        print("\t", first, "\n\t", second)


def main():
    test1 = Sequences()


main()
