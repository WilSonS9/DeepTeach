import json

with open('./test_original.jsonl', 'r') as json_file:
    json_list = list(json_file)

l_test = []

for json_str in json_list:
    result = json.loads(json_str)
    new_dict = {}
    new_dict['prompt'] = 'Create a mathematics question'
    new_dict['completion'] = result['question']
    l_test.append(new_dict)

with open('./train_original.jsonl', 'r') as json_file:
    json_list = list(json_file)

l_train = []

for json_str in json_list:
    result = json.loads(json_str)
    new_dict = {}
    new_dict['prompt'] = 'This is a mathematics question:\n'
    new_dict['completion'] = result['question']
    l_train.append(new_dict)

f = open("test.jsonl", "a")  # append mode
for item in l_test:
    f.write(json.dumps(item) + '\n')
f.close()

f = open("train.jsonl", "a")  # append mode
for item in l_train:
    f.write(json.dumps(item) + '\n')
f.close()