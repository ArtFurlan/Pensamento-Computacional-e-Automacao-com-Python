from datetime import date

class Lead:
    def __init__(self, name, company, email):
        self.name = name
        self.company = company
        self.email = email
        self.stage = "novo"
        self.created = date.today().isoformat()

    def to_dict(self):
        return {
            "name": self.name,
            "company": self.company,
            "email": self.email,
            "stage": self.stage,
            "created": self.created
        }
