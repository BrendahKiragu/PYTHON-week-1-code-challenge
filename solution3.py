#  sorts the list of tuples by age in ascending order.
def sort_by_age(sample_tuple):
      return sorted(sample_tuple, key=lambda a: a[1])

print(sort_by_age([('bree', 5), ('mark', 3), ('james', 1)]))


#  sorts the list of tuples by age in ascending order.
def merge_dicts(dict1, dict2):
    merged_dict = {**dict1, **dict2}
    return merged_dict

print(merge_dicts({'name':'bree'}, {'occupation': 'devops'}))


# creates class Car with a attributes a method that prints the car details
class Car:
     def __init__(self, make_received, model_received, year_received):
          self.make = make_received
          self.model = model_received
          self.year = year_received

     def display_info(self):
          print(f"This is a {self.make} {self.model} from the year {self.year}.")

lexus = Car('Jeep', "Wagoneer", 2022)
lexus.display_info()
