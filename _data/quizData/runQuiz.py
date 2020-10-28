import yaml
from pprint import pprint
import argparse
from enum import Enum
from typing import Dict, List, Union


class QuestionType(Enum):
    FREE_RESPONSE = 0
    MULTIPLE_CHOICE = 1
    MATCHING = 2
    UNKNOWN = 3


QuestionTypeDict = {
    'FREE RESPONSE': QuestionType.FREE_RESPONSE,
    'MATCHING': QuestionType.MATCHING,
    'MULTIPLE CHOICE': QuestionType.MULTIPLE_CHOICE,
}

QuestionTypeDictReversed = {v: k for k, v in QuestionTypeDict.items()}


class Question:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return f"""{self.getTitle()}
Type: {self.getQuestionType().name}"""

    def getTitle(self) -> str:
        return self.data['title']

    def getQuestionTypeRaw(self) -> str:
        return self.data['type']

    def getQuestionType(self) -> QuestionType:
        if self.getQuestionTypeRaw().upper() in QuestionTypeDict:
            return QuestionTypeDict[self.getQuestionTypeRaw().upper()]

        return QuestionType.UNKNOWN


class QuestionBank():
    def __init__(self, questions: List[Question] = []):
        self.questions = questions

    def add_question(self, question: Question):
        self.questions.append(question)


# Initialize parser
parser = argparse.ArgumentParser()

# Adding optional argument
parser.add_argument("-f", "--file", required=True, help="Quiz datafile")

# Read arguments from command line
args = parser.parse_args()

print("Using quiz file " + args.file)

with open(args.file) as f:
    quizYaml = yaml.load(f, Loader=yaml.UnsafeLoader)

questionBank = QuestionBank()

for qnum in quizYaml['questions']:
    question = Question( data= quizYaml['questions'][qnum])
    questionBank.add_question(question)
    print(question)

exit(0)
