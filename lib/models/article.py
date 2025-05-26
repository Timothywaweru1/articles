# lib/models/article.py
from db.connection import get_connection

class Article:
    def __init__(self, id=None, title=None, author_id=None, magazine_id=None):
        self.id = id
        self.title = title
        self.author_id = author_id
        self.magazine_id = magazine_id

    def save(self):
        with get_connection() as conn:
            cursor = conn.cursor()
            if self.id:
                cursor.execute("""
                    UPDATE articles 
                    SET title = ?, author_id = ?, magazine_id = ? 
                    WHERE id = ?
                """, (self.title, self.author_id, self.magazine_id, self.id))
            else:
                cursor.execute("""
                    INSERT INTO articles (title, author_id, magazine_id) 
                    VALUES (?, ?, ?)
                """, (self.title, self.author_id, self.magazine_id))
                self.id = cursor.lastrowid
            conn.commit()
        return self

    def delete(self):
        with get_connection() as conn:
            conn.execute("DELETE FROM articles WHERE id = ?", (self.id,))
            conn.commit()

    @classmethod
    def find_by_id(cls, id):
        with get_connection() as conn:
            row = conn.execute("SELECT * FROM articles WHERE id = ?", (id,)).fetchone()
            return cls._row_to_article(row) if row else None

    @classmethod
    def find_by_title(cls, title):
        with get_connection() as conn:
            row = conn.execute("SELECT * FROM articles WHERE title = ?", (title,)).fetchone()
            return cls._row_to_article(row) if row else None

    @classmethod
    def find_by_author(cls, author_id):
        with get_connection() as conn:
            rows = conn.execute("SELECT * FROM articles WHERE author_id = ?", (author_id,)).fetchall()
            return [cls._row_to_article(row) for row in rows]

    @classmethod
    def find_by_magazine(cls, magazine_id):
        with get_connection() as conn:
            rows = conn.execute("SELECT * FROM articles WHERE magazine_id = ?", (magazine_id,)).fetchall()
            return [cls._row_to_article(row) for row in rows]

    def author(self):
        from models.author import Author
        return Author.find_by_id(self.author_id)

    def magazine(self):
        from models.magazine import Magazine
        return Magazine.find_by_id(self.magazine_id)



    def __repr__(self):
        return f"<Article id={self.id}, title='{self.title}'>"