from datetime import datetime, timedelta

from ..model.data_models import Session, Revision, Memorization
from ..utils.utils import fetch_all_intervals, fetch_completed_intervals, subtract_intervals

def regenerate_daily_revision_parts():
  completed_intervals = fetch_completed_intervals()
  all_intervals = fetch_all_intervals()
  remaining_intervals = subtract_intervals(all_intervals, completed_intervals)
  
  cycle_days = int(input("Enter revision cycle length in days: "))
  total_lines = sum(end - start + 1 for start, end in remaining_intervals)
  lines_per_day = total_lines // cycle_days if cycle_days > 0 else total_lines
  
  today_date = datetime.today()
  session = Session()
  
  daily_chunks = []
  current_chunk = []
  current_count = 0
  
  for start, end in remaining_intervals:
    while start <= end:
      if current_count < lines_per_day:
        chunk_end = min(start + (lines_per_day - current_count) - 1, end)
        current_chunk.append((start, chunk_end))
        current_count += chunk_end - start + 1
        start = chunk_end + 1
      else:
        daily_chunks.append(current_chunk)
        current_chunk = []
        current_count = 0
  
  if current_chunk:
    daily_chunks.append(current_chunk)
  
  for day, chunk in enumerate(daily_chunks):
    quest_date = (today_date + timedelta(days=day)).strftime('%Y-%m-%d')
    for start, end in chunk:
      start_page, start_line = divmod(start - 1, 15)
      end_page, end_line = divmod(end - 1, 15)
      new_quest = Revision(
        is_completed=False,
        is_deprecated=False,
        date=quest_date,
        start_page=start_page + 1,
        start_line=start_line + 1,
        end_page=end_page + 1,
        end_line=end_line + 1
      )
      session.add(new_quest)
  
  session.commit()
  session.close()

def log_new_memorization():
  try:
    start_page = int(input("Enter start page: "))
    start_line = int(input("Enter start line: "))
    end_page = int(input("Enter end page: "))
    end_line = int(input("Enter end line: "))
    
    if not (1 <= start_line <= 15 and 1 <= end_line <= 15):
      raise ValueError("Lines must be between 1 and 15.")

    if (start_page > end_page) or (start_page == end_page and start_line > end_line):
      raise ValueError("Invalid range: start must be before end.")
    
    today_date = datetime.today().strftime('%Y-%m-%d')
    
    session = Session()
    new_memorization = Memorization(
      date=today_date,
      start_page=start_page,
      start_line=start_line,
      end_page=end_page,
      end_line=end_line
    )
    session.add(new_memorization)
    session.commit()
    session.close()
    
    print("Memorization has been recorded in the database.")
    
  except ValueError as e:
    print(f"Invalid input: {e}")
