
from db.connection import get_connection

class Magazine:
    def __init__(self, id=None, name=None, category=None):
        self.id = id
        self.name = name
        self.category = category

    def save(self):
        with get_connection() as conn:
            cursor = conn.cursor()
            if self.id:
                cursor.execute("UPDATE magazines SET name = ?, category = ? WHERE id = ?", 
                             (self.name, self.category, self.id))
            else:
                cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", 
                             (self.name, self.category))
                self.id = cursor.lastrowid
            conn.commit()
        return self
        
    def articles(self):
        from models.article import Article
        with get_connection() as conn:
            rows = conn.execute("SELECT * FROM articles WHERE magazine_id = ?", (self.id,)).fetchall()
            return [Article._row_to_article(row) for row in rows]

    def contributors(self):
        with get_connection() as conn:
            rows = conn.execute("""
                SELECT DISTINCT a.* FROM authors a
                JOIN articles ar ON a.id = ar.author_id
                WHERE ar.magazine_id = ?
            """, (self.id,)).fetchall()

    def article_titles(self):
        with get_connection() as conn:
            rows = conn.execute("SELECT title FROM articles WHERE magazine_id = ?", (self.id,)).fetchall()
            return [row['title'] for row in rows]

    def contributing_authors(self):
        with get_connection() as conn:
            rows = conn.execute("""
                SELECT a.*, COUNT(ar.id) as article_count
                FROM authors a
                JOIN articles ar ON a.id = ar.author_id
                WHERE ar.magazine_id = ?
                GROUP BY a.id
                HAVING article_count > 2
            """, (self.id,)).fetchall()


