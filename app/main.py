class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        current_person = Person.people[person["name"]]
        if "wife" in person and person["wife"]:
            spouse = Person.people.get(person["wife"])
            if spouse:
                current_person.wife = spouse
                spouse.husband = current_person
        elif "husband" in person and person["husband"]:
            spouse = Person.people.get(person["husband"])
            if spouse:
                current_person.husband = spouse
                spouse.wife = current_person
    return person_list
