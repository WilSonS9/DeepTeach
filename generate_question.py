import openai

print()

res = openai.Completion.create(
    # model='ada:ft-abb-gymnasiet:deepteach-test-v2-2022-05-19-11-47-11',
    model='curie:ft-abb-gymnasiet:deepteach-test-v3-2022-05-20-08-55-07',
    prompt='This is a mathematics question:\n',
    max_tokens=100,
    temperature=0.9,
    stop='?')
# print(res)

question = res['choices'][0]['text'] + '? Explain all steps of your solution.'
print(question)

res = openai.Completion.create(
    model='text-davinci-002',
    prompt=question,
    max_tokens=100,
    temperature=0.7)
# print(res)

solution = res['choices'][0]['text']
print(solution)

output = {'question': question, 'solution': solution}

print()
print()

print(output)

print()