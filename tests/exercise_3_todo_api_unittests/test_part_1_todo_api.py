from unittest import TestCase
from exercise_3_todo_api.part_1_todo.part_1_todo import db, app, Todo


class Test(TestCase):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Parana1168!!@localhost:3306/demo'
    app.config["TESTING"] = True
    client = app.test_client()

    def test_setUp(self):
        db.create_all()

    def test_index_status(self):
        tester = app.test_client(self)
        response = tester.get("/")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_todos_status(self):
        tester = app.test_client(self)
        response = tester.get("/todos")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_show_todos(self):
        response = self.client.get('/todos')
        self.assertEqual(response.status_code, 200)
        assert response.request.path == '/todos'

    def test_add_todo(self):
        todo_test = Todo('grocery',	'buy banana', '2022-02-01', 'Undone', '')
        db.session.add(todo_test)
        db.session.commit()

    def test_update_todo(self):
        response = self.client.post('/todos/<int:todo_id>')
        self.assertEqual(response.status_code, 302)

    def test_delete_todo(self):

        response = self.client.post('/todos/<int:todo_id>/delete')
        self.assertEqual(response.status_code, 302)

    def test_tearDown(self):
        db.session.remove()
        db.drop_all()
