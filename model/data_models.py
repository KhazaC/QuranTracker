from sqlalchemy import create_engine, Column, Integer, Boolean, String
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()
engine = create_engine("sqlite:///quests.db")
Session = sessionmaker(bind=engine)

class Revision(Base):
  __tablename__ = "quests"
  id = Column(Integer, primary_key=True, autoincrement=True)
  is_completed = Column(Boolean, nullable=False)
  is_deprecated = Column(Boolean, nullable=False)
  date = Column(String, nullable=False)
  start_page = Column(Integer, nullable=False)
  start_line = Column(Integer, nullable=False)
  end_page = Column(Integer, nullable=False)
  end_line = Column(Integer, nullable=False)

class Memorization(Base):
  __tablename__ = "memorization"
  id = Column(Integer, primary_key=True, autoincrement=True)
  date = Column(String, nullable=False)
  start_page = Column(Integer, nullable=False)
  start_line = Column(Integer, nullable=False)
  end_page = Column(Integer, nullable=False)
  end_line = Column(Integer, nullable=False)

def initialize_db():
  Base.metadata.create_all(engine)
