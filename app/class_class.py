#should be improved
class class_class:

  level        = 0
  klasse       = 0
  subklasse    = 0
  classtype    = 0

  
  def __init__(self, name):
    self.name =name
    return
    
  def level_up(self, character):
    self.level +=1
    if self.classtype:
      character.special_level_up(classtype)
   
    character.add_feature(self.get_features(klasse, self.level))


  def get_features(klasse, level):
     #TODO find a good tepresentation for a class and features
     pass


  def __str__(self):
    return f"{name} level {level}"














    
