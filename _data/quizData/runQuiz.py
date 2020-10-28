import yaml
from pprint import pprint
import argparse
from enum import Enum
from typing import Dict, List, Union

class Question():
    def __init__(self, data):
        self.data=data




class QuestionType(Enum):
    FREE_RESPONSE = 0
    MULTIPLE_CHOICE = 1
    MATCHING = 2
    UNKNOWN = 3

@staticmethod
def questionTypeFromName(s:str):
    pass


def getQuestionKey(question: Dict[str, Union[str, List, Dict]]) -> str:
    return list(question.keys())[0]

# Initialize parser
parser = argparse.ArgumentParser()

# Adding optional argument
parser.add_argument("-f", "--file", required=True, help="Quiz datafile")

# Read arguments from command line
args = parser.parse_args()

print("Using quiz file " + args.file)


with open(args.file) as f:
    quizYaml = yaml.load(f, Loader=yaml.SafeLoader)

for qnum in quizYaml['questions']:
    question=quizYaml['questions'][qnum]
    # pprint(question)
    print(question)
    qname = getQuestionKey(question)

    print()