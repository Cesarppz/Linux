import unittest

import json
import requests

from app.models import db
from app import create_app
from config import config
from app.models.task import Task


class TestApi(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        environment = config['test']
        cls.app = create_app(environment)
        cls.client = cls.app.test_client()

        cls.content_type = 'application/json'
        cls.path = 'http://localhost:5000/api/v1/tasks'

        # with cls.app.app_context():

        #     list_of_task = [
        #     Task(title='Title 1', text='Description 1', deadline='2019-12-12 12:00:00'),
        #     Task(title='Title 2', text='Description 2', deadline='2019-12-30 11:45:00'),
        #     Task(title='Title 3', text='Description 3', deadline='2022-12-12 18:30:00')

        #     ]

        #     for i in list_of_task:
        #         db.session.add(i)

        #     # db.session.add(Task(title='Title 1', text='Description 1', deadline='2019-12-12 12:00:00'))
        #     db.session.commit()



    # def tearDown(self):
    #     pass
    #     # with self.app.app_context():
    #     #     db.drop_all()


    # def test_good_testing(self):
    #     self.assertEquals(1,1)


    def test_request(self):
        response = self.client.get(path=self.path)
        self.assertEqual(response.status_code, 200)


    def test_first_id(self):
        path = self.path + '/1'
        response = self.client.get(path=path, content_type=self.content_type)
        data = json.loads(response.data.decode('utf-8'))
        task_id = data['data']['id']
        self.assertEqual(task_id, 1)

    
    def test_not_found(self):
        not_found_path = self.path + '/500'
        response = self.client.get(path=not_found_path)
        self.assertEqual(response.status_code, 404)

    
    def test_update(self):
        data_put = {'title':'Nueva title [test module]'}
        path = self.path + '/1'
        response = self.client.put(path=path, content_type=self.content_type, data=json.dumps(data_put))
        self.assertEqual(response.status_code, 200)

        data = json.loads(response.data.decode('utf-8'))
        title = data['data']['title']
        self.assertEqual(title, data_put['title'])

    
    # def test_delete(self):
    #     path = self.path + '/6'
    #     response = self.client.delete(path=path, content_type=self.content_type)
    #     self.assertEqual(response.status_code,200)

    #     response_get = self.client.get(path=path, content_type=self.content_type)
    #     self.assertAlmostEqual(response_get.status_code, 404)



if __name__ == '__main__':
    unittest.main()