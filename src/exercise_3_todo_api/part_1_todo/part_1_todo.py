from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import pymysql


app = Flask(__name__, template_folder="template")
pymysql.install_as_MySQLdb()  # OJO ESTO
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Parana1168!!@localhost:3306/demo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['EXPLAIN_TEMPLATE_LOADING'] = True
db = SQLAlchemy(app)


class Todo(db.Model):
    todo_id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String(30), nullable=False)
    kind_id = db.Column(db.Integer, db.ForeignKey('kind.kind_id'), nullable=False)
    kind = db.relationship("Kind", back_populates="Todo")
    deadline = db.Column(db.String(30))
    status = db.Column(db.String(15))
    comment = db.Column(db.String(200))

    def __repr__(self):
        return '%s, %s, %s, %s, %s' % (self.title, self.kind, self.deadline, self.status, self.comment)


class Kind(db.Model):
    kind_id = db.Column(db.Integer, primary_key=True, nullable=False)
    kind = db.Column(db.String(30), nullable=False, unique=True)
    Todo = db.relationship("Todo", back_populates="kind")

    def __repr__(self):
        return '%s' % self.kind


def validate_todo(todo):
    errors = {}
    if todo.kind_id == '':
        errors['kind'] = "Please fill out this field."
    if len(todo.kind_id) > 30:
        errors['title'] = "Sorry, 30 characters max."
    if todo.title == '':
        errors['title'] = "Please fill out this field."
    if len(todo.title) > 30:
        errors['title'] = "Sorry, 30 characters max."
    return errors


@app.errorhandler(404)
def invalid_route(e):
    return render_template('error.html', e=e)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/kinds', methods=['POST'])
def add_kind():

    kind = request.form.get("new_kind")
    new_kind = Kind(kind=kind)
    kinds = Kind.query.all()
    kinds_list = [str(kind) for kind in kinds]
    if kind not in kinds_list:
        db.session.add(new_kind)
    db.session.commit()
    return redirect("/form")


@app.route('/form', methods=['GET'])
def form():

    kinds = Kind.query.all()
    return render_template('form.html', kinds=kinds)


@app.route('/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    todo = Todo.query.get(todo_id)
    kinds = Kind.query.all()
    if todo is None:
        return redirect('/error')
    else:
        return render_template('form.html', title=todo.title, kinds=kinds, deadline=todo.deadline,
                               status=todo.status, comment=todo.comment, todo_id=todo.todo_id)


@app.route('/todos/<int:todo_id>', methods=['POST'])
def update_todo(todo_id):
    todo = Todo.query.get(todo_id)
    if todo is None:
        return redirect('/error')
    else:
        todo.kind_id = request.form.get("kind")
        todo.title = request.form.get("title")
        todo.deadline = request.form.get("deadline")
        todo.status = request.form.get("status")
        todo.comment = request.form.get("comment")

        errors = validate_todo(todo)
        if errors:
            kinds = Kind.query.all()
            return render_template('form.html', title=todo.title, kind_id=todo.kind_id, deadline=todo.deadline,
                                   status=todo.status, comment=todo.comment, todo_id=todo.todo_id,
                                   errors=errors, kinds=kinds)
        try:

            db.session.commit()
            return redirect("/todos")
        except Exception as e:
            return f"There was an error adding data: {e}"


@app.route('/todos/new', methods=['POST'])
def add_todo():
    kind_id = request.form.get("kind")
    title = request.form.get("title")
    deadline = request.form.get("deadline")
    status = request.form.get("status")
    comment = request.form.get("comment")
    new_todo = Todo(title=title, kind_id=kind_id, deadline=deadline, status=status, comment=comment)
    errors = validate_todo(new_todo)
    if errors:
        kinds = Kind.query.all()
        return render_template('form.html', title=title, kind_id=kind_id, deadline=deadline, status=status,
                               comment=comment, errors=errors, kinds=kinds)
    try:
        db.session.add(new_todo)
        db.session.commit()
        return redirect("/todos")
    except Exception as e:
        return f"There was an error adding data: {e}"


@app.route('/todos', methods=['GET'])
def show_todos():
    try:
        todos = list(Todo.query.order_by(Todo.deadline))
        return render_template('todos.html', todos=todos)
    except Exception as e:
        return render_template('error.html', error=e)


@app.route('/todos/<int:todo_id>/delete', methods=['GET', 'POST'])
def delete_todo(todo_id):
    todo = Todo.query.get(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return redirect("/todos")


@app.route('/todos/<int:todo_id>/status', methods=['GET', 'POST'])
def change_status(todo_id):
    todo = Todo.query.get(todo_id)
    if todo.status == 'Pending':
        todo.status = 'Done'
        db.session.commit()
    return redirect("/todos")


@app.route('/todos/delete', methods=['GET', 'POST'])
def delete_todos():
    db.session.query(Todo).delete()
    db.session.commit()
    return redirect("/todos")


if __name__ == '__main__':
    app.run(debug=True)
