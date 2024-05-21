from db import Firebase


class User:
    def __init__(self, user_id: str, f: Firebase) -> None:
        self.user_id = user_id
        self.fullname = ""
        self.university = ""
        self.department= ""
        self.username= ""
        self.notes = []
        self.f = f
        self.ref = f.ref.child("user").child(self.user_id)
        if self.ref.get():
            self.get()

    def save(self):
        self.ref.set(
            {
                "fullname": self.fullname,
                "university": self.university,
                "department": self.department,
                "username" :self.username
            }
        )
        return self

    def update(self, updates: dict = {}):
        if updates:
            self.fullname = updates.get("fullname", self.fullname)
            self.department = updates.get("department", self.department)
            self.university = updates.get("university", self.university)
            self.username = updates.get("username", self.username)
        self.save()
        return self

    def get(self):
        user = self.ref.get()
        if not user:
            return self
        self.fullname = user["fullname"]
        self.username = user["username"]
        self.department = user["department"]
        self.university = user["university"]
        notes = self.f.ref.child("notes").get()
        if notes:
            for notes_id in notes:
                notes = notes[notes_id]
                if notes["user_id"] == self.user_id:
                    self.notes.append(notes)
        return self

    def delete(self):
        self.ref.delete()
        self.fullname = ""
        self.department = ""
        self.university = ""
        self.username = ""
        return self
    

    def __str__(self):
        return f"{self.fullname} @ {self.department}, {self.university}"

if __name__ == "__main__":
    f = Firebase()
    f.login("prof@university.edu", "password")
    user = User(f.get_user_id(), f)
    user.fullname = "Bora Canbula"
    user.department = "Computer Engineering"
    user.university = "Manisa Celal Bayar University"
    user.username = "boracan"
    user.save()
    print(user)
    user.update(
        {
            "fullname": "Prof. Dr.",
            "department": "Department of Computer Engineering",
        }
    )
    print(user)
    
