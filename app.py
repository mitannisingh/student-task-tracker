from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []


@app.route("/")
def home():
    return render_template("index.html", tasks=tasks)


@app.route("/add", methods=["POST"])
def add_task():
    title = request.form.get("title")

    if title:
        task = {
            "id": len(tasks) + 1,
            "title": title,
            "completed": False
        }
        tasks.append(task)

    return redirect(url_for("home"))


@app.route("/complete/<int:task_id>")
def complete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = not task["completed"]
            break

    return redirect(url_for("home"))


@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            break

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)