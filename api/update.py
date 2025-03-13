from datetime import datetime

from ..model.data_models import Session, Revision

def mark_daily_revision_completed():
  session = Session()
  today_date = datetime.today().strftime('%Y-%m-%d')
  quests = session.query(Revision).filter_by(date=today_date).all()
  for quest in quests:
      quest.is_completed = True
  session.commit()
  session.close()
