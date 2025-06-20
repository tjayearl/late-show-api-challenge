from server.app import app, db
from server.models.guest import Guest
from server.models.episode import Episode
from server.models.appearance import Appearance

with app.app_context():
    db.drop_all()
    db.create_all()

    guest1 = Guest(name="Tom Cruise", occupation="Actor")
    guest2 = Guest(name="Oprah Winfrey", occupation="Host")
    
    episode1 = Episode(number=101)
    episode2 = Episode(number=102)

    db.session.add_all([guest1, guest2, episode1, episode2])
    db.session.commit()

    app1 = Appearance(rating=4, guest_id=guest1.id, episode_id=episode1.id)
    app2 = Appearance(rating=5, guest_id=guest2.id, episode_id=episode2.id)

    db.session.add_all([app1, app2])
    db.session.commit()
    print("✅ Seed complete")
