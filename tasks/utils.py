def generate_gist_content(project):
    content = f"# {project.title}\n\n"
    completed_todos = project.todos.filter(status=True).count()
    total_todos = project.todos.count()
    content += f"**Summary:** {completed_todos} / {total_todos} completed.\n\n"
    content += "**Pending Todos:**\n"
    for todo in project.todos.filter(status=False):
        content += f"- [ ] {todo.description}\n"
    content += "\n**Completed Todos:**\n"
    for todo in project.todos.filter(status=True):
        content += f"- [x] {todo.description}\n"
    return content

def save_gist_locally(title, content):
    filename = f"{title}.md"
    with open(filename, 'w') as file:
        file.write(content)
