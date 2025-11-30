from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

text="""
Information Retrieval is a field concerned with searching for relevant
documeents within a large dataset. Text summarization is the process of
reducing a document's lenght while maintaining its main points. Extractive
methods identify and extract key sentences, while abstractive methods
generate summaries in their own words.
"""

parser=PlaintextParser.from_string(text,Tokenizer("english"))

summarizer=LsaSummarizer()
summary=summarizer(parser.document,2)

for sentence in summary:
    print(sentence)
