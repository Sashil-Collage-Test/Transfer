documents={
    1:"apple banana orange",
    2:"apple banana",
    3:"banana orange",
    4:"apple"
}

def build_index(docs):
    index={}
    for doc_id, text in docs.items():
        for term in set(text.split()):
            index.setdefault(term,set()).add(doc_id)
    return index

def boolean_and(operands,index):
    if not operands:
        return list(range(1,len(documents)+1))
    result=index.get(operands[0],set())
    for term in operands[1:]:
        result&=index.get(term,set())
    return list(result)

def boolean_or(operands,index):
    result=set()
    for term in operands:
        result|=index.get(term,set())
    return list(result)

def boolean_not(operand,index,total_docs):
    all_docs_set=set(range(1,total_docs+1))
    return list(all_docs_set-index.get(operand,set()))

inverted_index=build_index(documents)

query1=["apple","banana"]
query2=["apple","orange"]
query3="orange"

result1=boolean_and(query1,inverted_index)
result2=boolean_or(query2,inverted_index)
result3=boolean_not(query3,inverted_index,len(documents))

print("Documents containing 'apple' AND 'banana':",result1)
print("Documents containing 'apple' OR 'orange':",result2)
print("Documents NOT containing 'orange':",result3)
print("Performed by 10_Shashikant")
