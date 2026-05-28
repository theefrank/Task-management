from datetime import datetime
# Define tasks list
tasks = []


def _parse_due_date(due_date):
    """Parse due_date which can be a datetime or ISO string."""
    if isinstance(due_date, datetime):
        return due_date
    if isinstance(due_date, str):
        try:
            return datetime.fromisoformat(due_date)
        except ValueError:
            raise ValueError("due_date must be ISO format string or datetime")
    raise TypeError("due_date must be a datetime or ISO format string")


def add_task(title, description, due_date):
    """Add a task to the global tasks list."""
    if not title:
        raise ValueError("title is required")
    due = _parse_due_date(due_date)
    task = {
        "title": title,
        "description": description,
        "due_date": due,
        "completed": False,
        "created_at": datetime.now(),
    }
    tasks.append(task)
    print("Task added successfully!")
    return task


def mark_task_as_complete(index, tasks=tasks):
    """Mark task at index as complete. Index is 0-based."""
    if not isinstance(index, int):
        raise TypeError("index must be an integer")
    if index < 0 or index >= len(tasks):
        raise IndexError("task index out of range")
    tasks[index]["completed"] = True
    print("Task marked as complete!")
    return tasks[index]


def view_pending_tasks(tasks=tasks):
    """Return list of pending (not completed) tasks."""
    return [t for t in tasks if not t.get("completed")]


def calculate_progress(tasks=tasks):
    """Return completion percentage as int (0-100)."""
    if not tasks:
        return 0
    total = len(tasks)
    completed = sum(1 for t in tasks if t.get("completed"))
    progress = int((completed / total) * 100)
    return progress