from db.connection import get_connection

class Article:
    def __init__(self, id=None, title=None, author_id=None, magazine_id=None):
        self.id = id
        self.title = title
        self.author_id = author_id
        self.magazine_id = magazine_id

    def save(self):
        conn = get_connection()
        cur = conn.cursor()
        if self.id:
            cur.execute(
                "UPDATE articles SET title=?, author_id=?, magazine_id=? WHERE id=?",
                (self.title, self.author_id, self.magazine_id, self.id)
            )
        else:
            cur.execute(
                "INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)",
                (self.title, self.author_id, self.magazine_id)
            )
            self.id = cur.lastrowid
        conn.commit()
        conn.close()
        return self

    def delete(self):
        conn = get_connection()
        conn.execute("DELETE FROM articles WHERE id=?", (self.id,))
        conn.commit()
        conn.close()

    @classmethod
    def get(cls, id):
        conn = get_connection()
        row = conn.execute("SELECT * FROM articles WHERE id=?", (id,)).fetchone()
        conn.close()
        return cls._from_row(row) if row else None

    @classmethod
    def find_by_title(cls, title):
        conn = get_connection()
        row = conn.execute("SELECT * FROM articles WHERE title=?", (title,)).fetchone()
        conn.close()
        return cls._from_row(row) if row else None

    @classmethod
    def by_author(cls, author_id):
        conn = get_connection()
        rows = conn.execute("SELECT * FROM articles WHERE author_id=?", (author_id,)).fetchall()
        conn.close()
        return [cls._from_row(r) for r in rows]

    @classmethod
    def by_magazine(cls, mag_id):
        conn = get_connection()
        rows = conn.execute("SELECT * FROM articles WHERE magazine_id=?", (mag_id,)).fetchall()
        conn.close()
        return [cls._from_row(r) for r in rows]

    def get_author(self):
        from models.author import Author
        return Author.get(self.author_id)

    def get_magazine(self):
        from models.magazine import Magazine
        return Magazine.get(self.magazine_id)



    def __str__(self):
        return f"[Article #{self.id}] {self.title}"
