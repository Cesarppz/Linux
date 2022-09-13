from flask import Blueprint
from flask import jsonify

from flask import request

from .response import response, not_found, bad_request
from .models.task import Task

from .schemas import task_schema, tasks_schema, params_task_schema

api_v1 = Blueprint('api', __name__, url_prefix='/api/v1')


def set_task(function):
    def wrapper( **kwargs):
        id = kwargs.get('id', 0)
        task = Task.query.filter_by(id=id).first() 

        if task is None:
            return not_found()

        return function(task)

    wrapper.__name__ = function.__name__
    return wrapper

@api_v1.route('/tasks',methods=['GET'])
def tasks():
    page = int(request.args.get('page', 1))
    order = request.args.get('order', 'asc')

    tasks = Task.get_by_page(page, order)

    return response(
        tasks_schema.dump(tasks)
       #[task.serialize() for task in tasks]
    )


@api_v1.route('/tasks/<id>', methods=['GET'])
@set_task
def task(task):

    return response(
        task_schema.dump(task)
        # task.serialize()  #Es otro metodo que se puede usar
    )


@api_v1.route('/tasks', methods=['POST'])
def create_task():
    json = request.get_json(force=True)

    error = params_task_schema.validate(json)
    if error:
        print(error)
        return bad_request()

    task = Task.new(title=json['title'], text=json['text'], deadline=json['deadline'])
    
    if task.save():
        return response(task_schema.dump(task))
    else:
        bad_request()



@api_v1.route('/tasks/<id>', methods=['PUT'])
@set_task
def upadate_task(task):

    json = request.get_json(force=True)

    task.title = json.get('title', task.title)
    task.description = json.get('Description', task.text)
    task.deadline   = json.get('deadline',task.deadline)

    if task.save():
        return response(task_schema.dump(task))

    return bad_request()

@api_v1.route('/tasks/<id>', methods=['DELETE'])
@set_task
def delete_task(task):

    if task.delete():
        return response(task_schema.dump(task))
    
    return bad_request()