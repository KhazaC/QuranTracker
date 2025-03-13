from ..model.data_models import Session, Revision

def clear_uncompleted_revisions():
  session = Session()
  quests = session.query(Revision).filter_by(is_completed=False).all()
  for quest in quests:
    session.delete(quest)
  session.commit()
  session.close()
