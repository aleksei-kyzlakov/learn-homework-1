"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""
school_stats = [{'school_class': '4a', 'scores': [3,4,4,5,2]},
{'school_class': '4б', 'scores': [4,4,4,4,4]},
{'school_class': '4в', 'scores': [5,4,4,5,5,1]},
{'school_class': '4г', 'scores': [3,4,3,4,3]},
{'school_class': '4д', 'scores': [4,4,4,5]},
{'school_class': '4е', 'scores': [3,5,4,5,3]},
{'school_class': '4ж', 'scores': [2,2,2]},
{'school_class': '4з', 'scores': [3,4,4,5,2,4,4,3]}]


def avg(student_scores):
  scores_sum = 0
  for score in student_scores:
    scores_sum += score
  return scores_sum / len(student_scores)

def main():
    school_scores = []

    for i in range(len(school_stats)):
      school_scores.append(avg(school_stats[i]['scores'])) # наполняем список по школе средними оценками классов
      print(school_stats[i]['school_class'] + " " + str(school_scores[i])) # выводим средние оценки для классов
    
    print("Средняя оценка по школе " + str(avg(school_scores))) # выводим среднюю оценку по школе
   
if __name__ == "__main__":
    main()
