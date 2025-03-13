from ..model.data_models import Session, Revision, Memorization

def fetch_completed_intervals():
  session = Session()
  quests = session.query(Revision).filter_by(is_completed=True, is_deprecated=False).all()
  intervals = []
  for q in quests:
    intervals.append(( (q.start_page - 1) * 15 + q.start_line, (q.end_page - 1) * 15 + q.end_line ))
    q.is_deprecated = True
  
  session.commit()
  session.close()
  return merge_intervals(intervals)

def fetch_all_intervals():
  session = Session()
  memorization_entries = session.query(Memorization).all()
  intervals = [( (m.start_page - 1) * 15 + m.start_line, (m.end_page - 1) * 15 + m.end_line ) for m in memorization_entries]
  session.close()
  return merge_intervals(intervals)

def merge_intervals(intervals):
  intervals.sort()
  merged = []
  for start, end in intervals:
    if merged and merged[-1][1] >= start:
      merged[-1] = (merged[-1][0], max(merged[-1][1], end))
    else:
      merged.append((start, end))
  return merged

def subtract_intervals(all_intervals, completed_intervals):
  remaining_intervals = []
  for start, end in all_intervals:
    for c_start, c_end in completed_intervals:
      if c_end < start or c_start > end:
        continue  # No overlap
      if c_start <= start and c_end >= end:
        start = end  # Fully covered
        break
      if c_start <= start:
        start = c_end + 1
      elif c_end >= end:
        end = c_start - 1
      else:
        remaining_intervals.append((start, c_start - 1))
        start = c_end + 1
    if start <= end:
      remaining_intervals.append((start, end))
  return merge_intervals(remaining_intervals)
