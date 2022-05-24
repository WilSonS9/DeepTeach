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

The stop sequence `?` is used, meaning that the model will stop generating tokens after it has generated a question mark. This is to prevent it from rambling on and creating nonsense questions, which occured when this was neglected. The suffix `Explain all steps of your solution.` is appended to the end of each question to encourage the answering model to motivate their answers.

Afterwards, the more powerful OpenAI GPT-3 DaVinci model is fed the generated question and answers it. A JSON object is also created, containing both the question and the generated answer.
#### Examples
Example question (generated):
```
A warehouse has 40 boxes with the same contents. Each box contains an equal number of 40 packages and each package contains an equal number of 16 bottles. How many bottles are in the warehouse? Explain all steps of your solution.
```

Example answer (generated):

```
There are 40 boxes, each with 40 packages, each with 16 bottles.

40 x 40 x 16 = 25,600 bottle
```
