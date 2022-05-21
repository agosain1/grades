from statistics import mean
clas = input('What class? ')
def calcFrenchGrade():
    my_grades = [
	"29/45",
	"45/50",
	"29/35",
	"85/100",
    "90/100",
    "100/100",
    "100/100"
	]
    project_grade = 0.9551
    homework_grade = 1
    your_scores = []
    max_scores = []
    newScore = input('Enter a new grade: ')
    for item in my_grades:
        item = item.split("/")
        your_scores.append(int(item[0]))
        max_scores.append(int(item[1]))
    newScore = newScore.split("/")
    your_scores.append(int(newScore[0]))
    max_scores.append(int(newScore[1]))
    newTGrade = (sum(your_scores))/(sum(max_scores))
    output = ((project_grade * 0.2) + (homework_grade * 0.2) + (newTGrade * 0.4))/0.8
    print("new grade = " + str(100 * output))
    a = float(output) * 0.8
    final = 0.895 - a
    print("grade needed on final = " + str(final * 500))

def calcMathGrade():
    test_grades = [
        28/26, 32/31, 27/28
    ]
    final_grade = 98/100
    newScore = input('Enter a new grade: ')
    newScore = newScore.split('/')
    newScore = float(newScore[0]) / float(newScore[1])
    test_grades.append(newScore)
    print(70 * mean(test_grades) + 15 * final_grade + 15)

def calcScienceGrade():
    my_grades = [
        "18.5/19",
        "16/20",
        "6.5/9.5",
        "9/9.5",
        "8.25/10",
        "8.75/9",
        "10/10",
        "9.5/10",
        "8.5/9",
        "10/10",
        "38.5/43",
        "36.75/46",
        "45.5/56"
    ]
    project_grade = 1
    homework_grade = 1
    participation_grade = 0.8
    your_scores = []
    max_scores = []
    newScore = input('Enter a new grade: ')
    for item in my_grades:
        item = item.split("/")
        your_scores.append(float(item[0]))
        max_scores.append(float(item[1]))
    newScore = newScore.split("/")
    your_scores.append(float(newScore[0]))
    max_scores.append(float(newScore[1]))
    newTGrade = (sum(your_scores)) / (sum(max_scores))
    output = str(((project_grade * 0.25) + (homework_grade * 0.1) + (newTGrade * 0.4) + (participation_grade * 0.05)) / 0.8)
    print("new grade = " + output)

def calcEnglishGrade():
    my_grades = [
        "5/5",
        "10/10",
        "5/5",
        "5/5",
        "15/16",
        "5/5",
        "14/14",
        "16/16",
        "5/5",
        "12/12",
        "18/18",
        "16/16",
        "13/14",
        "16/16",
        "10/10",
        "16/16",
        "12/12",
        "10/10",
        "12/12",
        "12/15",
        "13/16",
        "12/12"
    ]
    essay_grade = 1
    quiz_grade = 1
    participation_grade = 1
    your_scores = []
    max_scores = []
    newScore = input('Enter a new grade: ')
    for item in my_grades:
        item = item.split("/")
        your_scores.append(float(item[0]))
        max_scores.append(float(item[1]))
    newScore = newScore.split("/")
    your_scores.append(float(newScore[0]))
    max_scores.append(float(newScore[1]))
    newTGrade = (sum(your_scores)) / (sum(max_scores))
    output = str(100 * ((quiz_grade * 0.1) + (essay_grade * 0.2) + (newTGrade * 0.6) + (participation_grade * 0.1)))
    print("new grade = " + output)

if clas.lower() == 'french':
    calcFrenchGrade()
elif clas.lower() == 'math':
    calcMathGrade()
elif clas.lower() == 'science':
    calcScienceGrade()
elif clas.lower() == 'english':
    calcEnglishGrade()
