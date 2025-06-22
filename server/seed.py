from server.app import app
from server.extensions import db
from server.models.guest import Guest
from server.models.episode import Episode

with app.app_context():
    g1 = Guest(name="Tjay Earl", occupation="Software Developer")
    g2 = Guest(name="John Doe", occupation="Musician")
    e1 = Episode(date="2024-06-01", number=1)
    e2 = Episode(date="2024-06-02", number=2)

    db.session.add_all([g1, g2, e1, e2])
    db.session.commit()
    print("✅ Database seeded")
