from flask import Flask, jsonify, request
app = Flask(__name__)

todos = [
  {"label": "My first task,", "done": False, "id": 1},
  {"label": "My second task", "done": False, "id": 2}
]

@app.route('/todos', methods=['GET'])
def get_todos():
  json_text = jsonify(todos)
  print(json_text)
  return jsonify(json_text)

@app.route('/todos', methods=['POST'])
def add_new_todo():
  request_body = request.json
  todos.append(request_body)
  print ("Incoming request with the following body", request_body)
  return jsonify(todos)

@app.route('/todos/<int:index>', methods=['DELETE'])
def delete_todo(index):
  global todos
  print("This is the index to delete:", index)
  del todos[index]
  return jsonify(todos)

@app.route('/todos/edit/<int:index>', methods=['PUT'])
def update_todo(index):
    global todos
    request_body = request.json
    todos[index] = request_body
    return jsonify(todos)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)