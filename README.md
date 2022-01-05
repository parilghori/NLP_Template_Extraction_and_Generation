# NLP_Template_Extraction_and_Generation

Phase 1: 
For this task, we chose the TriviaQA dataset. The TriviaQA dataset sources questions from several quiz-league websites as well as web search results and Wikipedia. The dataset is formatted with the fields: dataset, question, answers, positive_ctxs, negative_ctxs, hard_negative_ctxs. For our purpose, we focused on the question field when producing our templates.

To create the initial templates for phase 1(Question with masked entity), we took advantage of the fact that our dataset contained ready-made questions. We used space along with the en_core_web_lg model to transform each question into a template by selecting the named entities in the question and masking them. We choose en_core_web_lg over other models because of its superior performance. This gave us our 100 seed templates for use in the next phase.

We had done clustering to excludes the similar templates. 

Phase 2: 
We have trained classification model BERT, which takes as an
input {[CLS] text [SEP] template} and a linear layer takes as an input
the [CLS] representation and outputs a score. We have run that model
for every template and select the template that has the highest score.
We have used pre-trained ‘bert-base-uncased’ model and AdamW
optimizer to extract the template.

Phase 3:
Training script and pre-trained model for a question generation
algorithm using TriviaQA dataset and T5 text-to-text transformer model.
- Input: The input to our module is context and question template.
- Output : The output will be Question generated from the above input.
We have trained T5-model from hugging face’s transformer to generate
questions.T5 is a new transformer model from Google that is trained in
an end-to-end manner with text as input and modified text as output.
We have implemented Beam Search Decoding and Greedy Decoding to
generate most likely sequence of words(Question). In the output file T5-
Question1 are questions generated using Beam Search Decoding while
T5-Question2 are questions generated using Greedy Decoding.

BLEU Score:

We have compare the generated question using Seq2Seq model with the
actual question using BLEU score. We got the 0.507 average BLEU
score for 10 questions dataset.
