class MakeChange:
    def __init__(self):
        self.value = self.set_initial_value()
        self.denominations = self.set_denominations()
        print("value = ", self.value, "\tdenominations = ", self.denominations)
        self.coins = self.set_coins()
        print(self.coins)

    def set_initial_value(self):
        value = input("Enter the starting value: ")
        return int(value)

    def set_denominations(self):
        get_new_denomination = input("Enter new denomination or 0 to continue: ")
        list_of_denominations = []
        while get_new_denomination != '0':
            list_of_denominations.append(int(get_new_denomination))
            get_new_denomination = input("Enter new denomination or 0 to continue: ")
        list_of_denominations.sort()
        return list_of_denominations

    def set_coins(self):                #MAIN ALGORITHM
        current_value = self.value
        list_of_coins = []
        index = len(self.denominations) - 1
        current_denomination = self.denominations[index]
        while current_value != 0:
            if current_value >= current_denomination:       #slight change
                list_of_coins.append(current_denomination)
                current_value = current_value - current_denomination    #slight change
            else:
                index = index - 1
                if index < 0:
                    break
                current_denomination = self.denominations[index]
        return list_of_coins


def main():
    test1 = MakeChange()


main()
