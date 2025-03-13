from datetime import datetime

from ..model.data_models import Session, Revision

def get_daily_revision():
    today_date = datetime.today().strftime('%Y-%m-%d')
    session = Session()
    quests = session.query(Revision).filter_by(date=today_date).all()
    print(f"Daily Revision for {today_date}: ")
    for quest in quests:
      print(f"\tReview from {quest.start_page}:{quest.start_line} to {quest.end_page}:{quest.end_line}.")
