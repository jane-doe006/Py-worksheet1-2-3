def addtask(tasks):
    t = input("Enter task: ")
    tasks.append(t)

def viewtasks(tasks):
    for i, t in enumerate(tasks):
        print(f"{i}: {t}")

def deletetask(tasks):
    idx = input("Enter task index to delete: ")
    if idx.isdigit():
        idx = int(idx)
        if 0 <= idx < len(tasks):
            tasks.pop(idx)
            return
    print("Invalid index.")

def todo_app():
    tasks = []
    while True:
        op = input("Options: add/view/delete/exit: ").strip().lower()
        if op == 'add':
            addtask(tasks)
        elif op == 'view':
            viewtasks(tasks)
        elif op == 'delete':
            deletetask(tasks)
        elif op == 'exit':
            break

todo_app()