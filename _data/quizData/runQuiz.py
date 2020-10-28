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
        self.answered = False
        self.answer = None
        self.correct = False

    def ask(self):
        """Ask an answer to stdin and store results in myself."""
        if self.getQuestionType() == QuestionType.FREE_RESPONSE:
            print("Todo implement asking user to answer FREE_RESPONSE question")
            x = input(" > ")

            print('u said ' + x)

        if self.getQuestionType() == QuestionType.MATCHING:
            print("Todo implement asking user to answer MATCHING question")

        if self.getQuestionType() == QuestionType.MULTIPLE_CHOICE:
            print("Todo implement asking user to answer MULTIPLE_CHOICE question")

        if self.getQuestionType() == QuestionType.UNKNOWN:
            print("lol you need to fix this question:")
            print(self)

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

    def run_quiz(self):
        for question in self.questions:
            if not question.answered:
                question.ask()


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
    questionData = quizYaml['questions'][qnum]
    question = Question(data=questionData)
    questionBank.add_question(question)
    # print(question)

questionBank.run_quiz()

exit(0)
