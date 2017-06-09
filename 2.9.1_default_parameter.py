# THIS CODE IS PARAMETER ()
def studentScore(name, score):
    print(name, "Scored ", score, " Marks")


studentScore("suranjan", 80)
studentScore("Mrunmayi", 95)


# THIS CODE IS FOR DEFAULT PARAMETER()
# THIS IS USED BECZ IF IM DATABASE THER IS NO VALUE SO IT WILL BE NULL AND I WILL SHOW ERROR SO THAT WHY WE USED DEFAULT PARAMETER
print("***DEFAULT PARAMETER()***")


def Studentscore(name="suranjan", score=75):
    print(name, "Scored ", score, " Marks")

Studentscore()
Studentscore("Mrunmayi")
Studentscore(score=55)
