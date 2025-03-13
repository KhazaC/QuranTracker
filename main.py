from .model.data_models import initialize_db
from .api.create import log_new_memorization, regenerate_daily_revision_parts
from .api.update import mark_daily_revision_completed
from .api.retrieve import get_daily_revision
from .api.delete import clear_uncompleted_revisions

def conduct_action():
  choice = input("Enter your choice: ")

  match choice:
    case "1":
      get_daily_revision()
    case "2":
      mark_daily_revision_completed()
    case "3":
      log_new_memorization()
    case "4":
      regenerate_daily_revision_parts()
    case "5":
      clear_uncompleted_revisions()

def print_menu():
  print("Choose an option:")
  print("1 - What do I need to Revise today?")
  print("2 - Mark daily revision completed.")
  print("2 - Log New Memorization.")
  print("3 - Regenerate daily revision parts.")
  print("5 - Clear uncompleted daily revisions.")

def main():
  initialize_db()
  print_menu()
  conduct_action()

if __name__ == "__main__":
  main()
