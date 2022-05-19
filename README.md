# DeepTeach
Repository for DeepTeach, the NLP maths problem generator and solver.
## Purpose

The purpose of DeepTeach is to create an NLP model that generates and solves mathematics word questions at a grade school level. The goal is to simplify teachers' jobs and to automate the boring task of coming up with exam questions.
## Model
The model used to both generate and solve the questions is [GPT-3](https://github.com/openai/gpt-3) by OpenAI.

To generate the questions, a GPT-3 model was fine tuned to create appropriate questions.
### Data
The data used to fine-tune the generating model was taken from the OpenAI [Grade School Math](https://github.com/openai/grade-school-math) dataset. The dataset was pre-split into a train and a test set. The data consisted of around 9 800 grade school math questions and answers.

To generate questions, I wasn't interested in the answers, so the data was re-formatted as pairs of `prompt`s and `completion`s, with the prompts being `"Create a mathematics question"` and the completions being the questions. This was done with the script `format_data.py` from `/dataset`, with the original and formatted data also being present there.
### Fine-tuning
To fine-tune the generating model, the [OpenAI guide to fine-tuning](https://beta.openai.com/docs/guides/fine-tuning) was followed.

The base model used was the OpenAI GPT-3 Ada model, the smallest, fastest and cheapest model available. To start fine-tuning a test model, the command `openai api fine_tunes.create -t .\dataset\train.jsonl -m ada --suffix "deepteach test" ` was used.
