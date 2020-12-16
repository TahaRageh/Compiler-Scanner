class Scanner:

    def __init__(self, specialSymbols=None, reservedWords=None):
        if reservedWords is None:
            self.reservedWords = ["if", "then", "else", "end", "repeat",
                                  "until", "read", "write"]

        if specialSymbols is None:
            self.specialSymbols = ["+", "-", "*", "/", "=",
                                   "<", "(", ")", ";"]
        self.number = "0123456789"
        self.identifier = "abcdefghijklmnopqrstuvwxyz"
        self.value = ""
        self.type = ""
        self.currentState = 1
        self.Position = 0
        self.token = []

# here must send input file as a string then make for loop " for character in file "
    def takeToken(self, file):
      for char in file :
        if self.currentState == 1:  # start state
            if char == "{":
                self.currentState = 2
            elif char == ":":
                self.type = "ASSIGNMENT"
                self.currentState = 3
            elif char in self.number:
                self.type = "NUMBER"
                self.value = self.value + char
                self.currentState = 5
            elif char in self.identifier:
                self.type = "IDENTIFIER"
                self.value = self.value + char
                self.currentState = 4
            elif char in self.specialSymbols:
                self.type = " SPECIAL SYMBOL"
                self.value = self.value + char
                self.currentState = 6


        elif self.currentState == 2:  # INCOMMENT state
            if char == "}":
                self.currentState = 1
                self.value = ""
            else : self.currentState = 2


        elif self.currentState == 3:  # INASSIGN state
            if char == "=":
                self.value = ":="
                self.currentState = 6


        elif self.currentState == 4:  # INID state
            if char in self.identifier:
                self.value += char
                if self.value in self.reservedWords:
                    self.currentState = 6
                    self.type = "RESERVED WORD"
            elif char in self.number:
                self.currentState = 4
                self.value += char
            else : self.currentState = 6


        elif self.currentState == 5:  # INNUM state
            if char in self.number:
                self.value += char
            else:
                self.currentState = 6



        if  self.currentState == 6:  # final state
            self.token.append(self.value + "," + self.type)
            self.currentState = 1
            self.value = ""
      print(self.token)


Taha = Scanner()
Taha.takeToken("read x; \n ;")