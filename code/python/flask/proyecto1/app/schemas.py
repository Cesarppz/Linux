from marshmallow import Schema 
from marshmallow import fields
from marshmallow.validate import Length

class TaskSchema(Schema):
    class Meta:
        fields = ('title',
                  'id',
                  'Description',
                  'deadline'
        )


class ParamsTaskSchema(Schema):
    title    = fields.Str(required=True, valiadate=Length(max=50))
    text     =  fields.Str(required=True)
    deadline = fields.DateTime(required=True)


task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)

params_task_schema = ParamsTaskSchema()


