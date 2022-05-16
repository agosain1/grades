def calcFrenchGrade(newTScore):
	grades = [
	"29/45",
	"45/50",
	"29/35",
	"85/100"
	]
	project_grade = 0.9551
	homework_grade = 1
	your_scores = []
	max_scores = []
	for item in grades:
	    item = item.split("/")
	    your_scores.append(int(item[0]))
	    max_scores.append(int(item[1]))
	newTScore = newTScore.split("/")
	your_scores.append(int(newTScore[0]))
	max_scores.append(int(newTScore[1]))
	newTGrade = (sum(your_scores))/(sum(max_scores))
	return(((project_grade * 0.2) + (homework_grade * 0.2) + (newTGrade * 0.4))/0.8)


your_grade = "290/300"
print("new grade = " + str(calcFrenchGrade(your_grade)))
a = calcFrenchGrade(your_grade) * 0.8
final = 0.895 - a
print("grade needed = " + str(final / 0.2))

