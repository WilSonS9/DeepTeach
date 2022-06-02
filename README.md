# DeepTeach
Repository for DeepTeach, the NLP maths problem generator and solver.
## Purpose

The purpose of DeepTeach is to create an NLP model that generates and solves mathematics word questions at a grade school level. The goal is to simplify teachers' jobs and to automate the boring task of coming up with exam questions.
## Model
The model used to both generate and solve the questions is [GPT-3](https://github.com/openai/gpt-3) by OpenAI.

To generate the questions, a GPT-3 model was fine tuned to create appropriate questions.
### Data
The data used to fine-tune the generating model was taken from the OpenAI [Grade School Math](https://github.com/openai/grade-school-math) dataset. The dataset was pre-split into a train and a test set. The data consisted of around 9 800 grade school math questions and answers.

To generate questions, I wasn't interested in the answers, so the data was re-formatted as pairs of `prompt`s and `completion`s, with the prompts being `"This is a mathematics question:\n"` and the completions being the questions. This was done with the script `format_data.py` from `/dataset`, with the original and formatted data also being present there.
### Fine-tuning
To fine-tune the generating model, the [OpenAI guide to fine-tuning](https://beta.openai.com/docs/guides/fine-tuning) was followed.

The base model used was the OpenAI GPT-3 Ada model, the smallest, fastest and cheapest model available. To start fine-tuning a test model, the command `openai api fine_tunes.create -t .\dataset\train.jsonl -m ada --suffix "deepteach test" ` was used.

Another model with the OpenAI GPT-3 Curie model was fine tuned, but the results were not much better than the ones from the Ada-based model, and as it was a lot more expensive this was abandoned.
### Generation
To generate a question and an answer, the script `generate_question.py` can be run. The script uses the fine-tuned model to create a new question by being prompted with `"This is a mathematics question:\n"`.

The stop sequence `?` is used, meaning that the model will stop generating tokens after it has generated a question mark. This is to prevent it from rambling on and creating nonsense questions, which occured when this was neglected. The suffix `Explain all steps of your solution.` is appended to the end of each question to encourage the answering model to motivate its answers.

Afterwards, the more powerful OpenAI GPT-3 DaVinci model is fed the generated question and answers it. A JSON object is also created, containing both the question and the generated answer.

### Prompt engineering

The phrase `"Let's think step by step."` is added to the end of the question after a newline. This is the start of the answer to the question, and it further encouraged the model to explain its thinking and increased its accuracy. To illustrate this, the question `"Ludvig Bylund has 1800 cows and half as many pigs on his farm. How many animals does Bylund have in total?"` was given to the model.

Without the phrase:
```
Bylund has 2,300 animals in total.
```

With the phrase:
```
Let's think step by step.
 We can start by finding the number of cows, which is 1800. To find the number of pigs, we can divide 1800 by 2 to get 900. Now we can add 1800 
+ 900 to get the total number of animals, which is 2700.
```

As we can see, the answer quality is improved by prefixing the answer with the phrase.
### Examples
Example question (generated):
```
Mr. Anderson is counting his fish. He has 20 barracuda, 25 sturgeon, 60 bluegill and 70 perch. If Mr. Anderson catches all the fish, how many fish does he have? Explain all steps of your solution.
```

Example answer (generated):

```
Let's think step by step.


Mr. Anderson has 20 barracuda, 25 sturgeon, 60 bluegill and 70 perch.

To find out how many fish Mr. Anderson has in total, we need to add up the number of fish he has for each type.


So, if Mr. Anderson catches all the fish, he would have 175 fish in total.
```

### Usage
To generate a question and solution, run the script `generate_question.py`. Here, four arguments can be provided: `-p`, `-q`, `-g` and `-a`.

The argument `-p` can be used to provide an initial prompt to the question. For example, if the script is run with the command `generate_question.py -p "Ludvig Bylund"`, the question will begin with `Ludvig Bylund`. The rest will be automatically generated.

The argument `-q` can be used to provide an entire question to be answered. If this argument is provided, no question will be generated, and solely an automatically generated solution will be provided. If neither this or the `-p` argument is given, the entire question will be generated automatically.

The arguments `-g` and `-a` are used to provide temperatures for the generation of the question and the solution respectively. A higher temperature will create a more random and chaotic result, and a lower temperature will make the model more determenistic and increase the chances of the model becoming repetitive. If these arguments are not provided, the default value of `0.7` will be used.
