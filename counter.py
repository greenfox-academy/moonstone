class count:

  def ages(self, name, birth_year):
    self.name = name
    self.current_year = 2017
    self.birth_year = birth_year
    self.month = 8
    self.age = self.current_year - self.birth_year
    print(self.age)
    print("I borned in the: " + str(self.month)+ "th month in " + str(self.birth_year))
    if self.age > 50:
      print("I am too old for festivals")
        
count_age = count()
count_age.ages("Tamara", 1986)



