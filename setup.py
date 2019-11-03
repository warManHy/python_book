# coding: utf-8
import unittest

class Question():
    def __init__(self, question):
        self.question = question
        self.responses = []
    def show_question(self):
        print question
    def store_response(self, new_response):
        self.responses.append(new_response)
    def show_results(self):
        for i in self.responses:
            print '_' + i


class TestSetUp(unittest.TestCase):
    """ 测试类 """
    def setUp(self):
        """
        创建一个调查对象和一组答案，供使用的测试方式使用
        """
        question = "this is a question"
        self.question = Question(question)
        self.responses = ['hanyan','yan']
    def test_store_responses(self):
        self.question.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.question.responses)
    def test_store_two_responses(self):
        self.question.store_response(self.responses)
        self.assertIn(self.responses, self.question.responses)

unittest.main()


