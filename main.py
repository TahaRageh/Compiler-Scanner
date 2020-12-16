
   # list or enum or map or set
   #{ if , then , else , end , repeat , until , read , write }

   # list or enum or map or set
   #{  {+,PLUS} , {-,MINUS} , {*, MULTIPLICATION} , {/,DIVIOSION} , {=,EQUAL} , {<,COMPARE less than } , {>,COMPARE less than} ,
   #{ ( , left Bracket} , { ) , Right bracket } , { ; , Semicolon} , { := , Assign } }

f = open("Tiny Code.txt", "r")

ALL_Statements = f.read()
# Bonus : Try to accept input from file

#no_of_semicolon = ALL_Statements.count(";")
#SEPE_STAT = ALL_Statements.split(";" , no_of_semicolon-1 )

# Here must be for loop to detect every token in Each seperated Statement

#print(ALL_Statements)
SEPE_STAT = ALL_Statements.split("\n")
print(SEPE_STAT )

"""
f = open("Tokens.txt", "w+")
for statement in SEPE_STAT :
   words = statement.split()
   for string in words :
      f.write( Scanner.takeToken(string) )
      f.write("\n")

"""
