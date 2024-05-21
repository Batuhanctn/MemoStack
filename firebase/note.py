from db import Firebase
from user import User


class Note:
    def __init__(self, user_id: str, f: Firebase) -> None:
        self.note_id = ""
        self.user_id = user_id
        self.title = ""
        self.description = ""
        self.ref = f.ref.child("notes")
        self.user = User(user_id, f)

    def create(self):
        self.note_id = self.ref.push(
            {
                "title": self.title,
                "description": self.description,
                "user_id": self.user_id,
            }
        ).key
        return self

    def save(self):
        self.ref.child(self.note_id).set(
            {
                "title": self.title,
                "description": self.description,
                "user_id": self.user_id,
            }
        )
        return self

    def update(self, updates: dict = {}):
        if updates:
            self.title = updates.get("title", self.title)
            self.description = updates.get("description", self.description)
            self.user_id = updates.get("user_id", self.user_id)
        self.save()
        return self

    def get(self):
        note = self.ref.child(self.note_id).get()
        if not note:
            return self
        self.title = note["title"]
        self.description = note["description"]
        self.user_id = note["user_id"]
        return self

    def delete(self):
        self.ref.child(self.note_id).delete()
        self.title = ""
        self.description = ""
        self.user_id = ""
        return self

    def __str__(self):
        return f"{self.title} - {self.description} by {self.user.department} {self.user.fullname}"



    