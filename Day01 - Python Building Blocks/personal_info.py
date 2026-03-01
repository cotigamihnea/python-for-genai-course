from dataclasses import dataclass

@dataclass
class Person:
    full_name: str
    age: int
    height_m: float
    favorite_language: str
    years_experience: int
    learning_python: bool

    def display(self):
        print("=== Personal Information ===")
        print(f"Name: {self.full_name} ({type(self.full_name)})")
        print(f"Age: {self.age} ({type(self.age)})")
        print(f"Height: {self.height_m} m ({type(self.height_m)})")
        print(f"Favourite programming language: {self.favorite_language} ({type(self.favorite_language)})")
        print(f"Years of experience: {self.years_experience} ({type(self.years_experience)})")
        print(f"Currently learning Python: {self.learning_python} ({type(self.learning_python)})")


if __name__ == "__main__":
    # example values - replace these with your actual information
    me = Person(
        full_name="Mihnea Example",
        age=30,
        height_m=1.75,
        favorite_language="Python",
        years_experience=5,
        learning_python=True,
    )
    me.display()
