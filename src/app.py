from flask import Flask, jsonify, request
app = Flask(__name__)

todos = [
  {"label": "My first task,", "done": False, "id": 1234},
  {"label": "My second task", "done": False, "id": 1235}
]

@app.route('/todos', methods=['GET'])
def hello_world():
  json_text = jsonify(todos)
  return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
  request_body = request.json
  todos.append(request_body)
  print ("Incoming request with the following body", request_body)
  return jsonify(todos)

@app.route('/todos/<int:id>', methods=['DELETE'])
def delete_todo(id):
  print("This is the id to delete:", id)
  del todos["id"]
  return jsonify(todos)

@app.route('/todos/edit/<int:id>', methods=['PUT'])
def put_todo(id):
    print("This is the position to change:", id)
    request_body = request.json
    if 'id' not in request_body:
        return jsonify({'error': 'Missing required field: id'}), 400

    todo_id = request_body['id']
    found_todo = None
    for i, todo in enumerate(todos):
        if todo['id'] == todo_id:
            found_todo = todo
            todos[i] = request_body 
            break

    if not found_todo:
        return jsonify({'error': 'Todo not found'.format(todo_id)}), 404 

    return jsonify(todos), 200  


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)