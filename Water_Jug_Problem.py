class Water_jug_Puzzle:
    def __init__(self):
        self.four = 0  # 4 liter jug
        self.three = 0  # 3 liter jug

    def rule_1(self):
        # Fill 3 liter jug completely from faucet
        if self.three < 3:
            self.three = 3
            return True
        return False

    def rule_2(self):
        #Fill 4 liter jug completely from faucet
        if self.four < 4:
            self.four = 4
            return True
        return False

    def rule_3(self):
        # Empty 4 liter jug
        if self.four >= 0:
            self.four = 0
            return True
        return False

    def rule_4(self):
        # Empty 3 liter jug 
        if self.three >= 0:
            self.three = 0
            return True
        return False

    def rule_5(self):
        # Fill 4 liter jug from 3 liter jug 
        if self.four < 4:
            if self.four == 0:
                self.four += self.three
                self.three = 0
                return True
            else:
                self.three -= (4 - self.four)
                self.four = 4
            return True
        else:
            return False

    def rule_6(self):
        # Fill 3 liter jug from 4 liter jug 
        if self.three < 3:
            if self.three == 0:
                self.four -= self.three
                self.three = 3
                return True
            else:
                self.four -= (3 - self.three)
                self.three = 3
            return True
        else:
            return False

# Driver Code
if __name__ == '__main__':
    myJug = Water_jug_Puzzle()
    print(f'Initial State: ({myJug.four}, {myJug.three})')
    while(myJug.four != 2):
        input_rule = int(input("Enter rule: "))
        if input_rule == 0:
            break
        elif input_rule == 1:
            steps = myJug.rule_1()
        elif input_rule == 2:
            steps = myJug.rule_2()
        elif input_rule == 3:
            steps = myJug.rule_3()
        elif input_rule == 4:
            steps = myJug.rule_4()
        elif input_rule == 5:
            steps = myJug.rule_5()
        elif input_rule == 6:
            steps = myJug.rule_6()
        else:
            print('Invalid rule !')
            continue

        if not steps:
            print('Choose another rule!')
        print(f'Current State: ({myJug.four}, {myJug.three})')
print('You have solved the puzzle !')