# Day 27: NLP Modeling and Transformer Fundamentals — Interview Notes

## 1. What is NLP?

Natural Language Processing (NLP) is a field of AI that enables computers to process, understand, and generate human language.

Examples:
- Sentiment analysis
- Spam detection
- Text classification
- Machine translation
- Question answering
- Chatbots

## 2. What is Text Classification?

Text classification assigns predefined categories or labels to text.

Examples:
- Positive / Negative sentiment
- Spam / Not Spam
- Sports / Politics / Technology

In this project, text classification is used to predict sentiment.

## 3. What is an RNN?

A Recurrent Neural Network (RNN) is a neural network designed to process sequential data.

Key characteristics:
- Processes tokens sequentially.
- Maintains a hidden state.
- Uses information from previous steps.

Limitations:
- Can suffer from vanishing gradients.
- May struggle with long-range dependencies.
- Sequential processing limits parallelization.

## 4. What is a Transformer?

A Transformer is a neural network architecture based primarily on attention mechanisms.

Key characteristics:
- Uses self-attention to model relationships between tokens.
- Can process tokens in parallel during training.
- Captures relationships between distant tokens more effectively than basic RNNs.

## 5. RNN vs Transformer

| RNN | Transformer |
|---|---|
| Sequential processing | Parallel processing during training |
| Uses recurrent hidden states | Uses attention mechanisms |
| Can struggle with long dependencies | Better at modeling long-range relationships |
| Processes tokens step by step | Processes sequence representations using attention |

## 6. What is Attention?

Attention allows a model to focus on relevant parts of an input sequence when processing a token or producing an output.

It helps the model identify relationships between different tokens.

## 7. What is Self-Attention?

Self-attention allows each token in a sequence to calculate how much attention it should pay to other tokens in the same sequence.

It helps capture contextual relationships between words.

## 8. What are Query, Key, and Value?

Self-attention uses three representations:

- **Query (Q):** Represents what a token is looking for.
- **Key (K):** Represents what a token can be matched against.
- **Value (V):** Contains the information that contributes to the output.

Attention scores are calculated using Query and Key representations. These scores are used to create a weighted combination of Value representations.

## 9. What is Positional Encoding?

Self-attention does not inherently encode token order.

Positional information is added to token representations so the model can understand the position and sequence of words.

## 10. What are Encoder and Decoder?

**Encoder:**
- Processes the input sequence.
- Builds contextual representations.

**Decoder:**
- Generates output sequences.
- Uses previously generated tokens and relevant encoded information, depending on the architecture.

Some Transformer models use only an encoder or only a decoder.

## 11. What is a Pretrained Model?

A pretrained model is a model that has already learned useful patterns from a large training dataset.

It can be reused for downstream tasks rather than training an entirely new model from scratch.

## 12. What is Transfer Learning?

Transfer learning means using knowledge learned from one task or dataset to improve performance on another task.

In NLP, pretrained models are commonly adapted for specific tasks.

## 13. What is Fine-Tuning?

Fine-tuning is the process of continuing the training of a pretrained model on task-specific data.

For example, a pretrained language model can be fine-tuned on labeled positive and negative reviews.

**Important:** This Day 27 project uses a model that has already been fine-tuned for sentiment analysis. It performs inference; it does not fine-tune the model.

## 14. What is Inference?

Inference is the process of using a trained model to make predictions on new input data.

In this project, inference means passing text to the pretrained DistilBERT classifier and receiving a sentiment label and score.

## 15. What is DistilBERT?

DistilBERT is a smaller, faster Transformer-based language model derived from BERT using knowledge distillation.

It retains many useful language-understanding capabilities while reducing model size and computational requirements.

## 16. What is BERT?

BERT stands for Bidirectional Encoder Representations from Transformers.

It is an encoder-based Transformer model that learns contextual representations using both left and right context.

## 17. BERT vs GPT

| BERT | GPT |
|---|---|
| Encoder-based architecture | Decoder-based architecture |
| Commonly used for language understanding | Commonly used for text generation |
| Uses bidirectional context | Uses causal, left-to-right context |
| Suitable for classification and extraction | Suitable for generation and completion |

## 18. What is a Hugging Face Pipeline?

A Hugging Face pipeline provides a convenient high-level API for performing common ML tasks.

For sentiment analysis:

```python
from transformers import pipeline

classifier = pipeline(
    task="sentiment-analysis",
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english"
)

result = classifier("I love learning Python.")

print(result)
```

The pipeline handles several steps, including tokenization, model inference, and post-processing.

## 19. What is Tokenization?

Tokenization converts input text into smaller units called tokens.

A tokenizer also converts tokens into numerical IDs that a model can process.

The tokenizer must be compatible with the selected pretrained model.

## 20. What does the Sentiment Model Return?

The model returns:
- `label`: predicted sentiment category.
- `score`: the model's reported confidence score for that prediction.

A high score does not guarantee that the prediction is correct.

## 21. Project Architecture

The Day 27 application follows this flow:

1. Import the Hugging Face pipeline.
2. Create a pretrained sentiment classifier.
3. Accept input text.
4. Validate the input.
5. Pass valid text to the classifier.
6. Receive the prediction.
7. Return the sentiment label and score.

## 22. Project-Based Interview Questions

### Q1. Why did you use DistilBERT?

**Answer:** I used DistilBERT because it is a smaller and faster Transformer-based model derived from BERT. It provides useful language-understanding capabilities with lower computational requirements.

### Q2. Did you train the model yourself?

**Answer:** No. I used a pretrained DistilBERT model that was already fine-tuned for binary sentiment classification. My implementation focuses on inference and input validation.

### Q3. How did you handle invalid input?

**Answer:** I used input validation in the prediction function. Non-string inputs raise TypeError, while empty or whitespace-only strings raise ValueError.

### Q4. Why use a function to create the classifier?

**Answer:** Separating classifier creation into its own function improves code organization and allows the same classifier to be reused for multiple predictions.

### Q5. Why did you use CPU inference?

**Answer:** CUDA was unavailable in my environment, so I explicitly configured the pipeline to use the CPU. The model still executed successfully.

### Q6. What is the difference between training and inference?

**Answer:** Training adjusts model parameters using data. Inference uses an already-trained model to generate predictions without updating its parameters.

### Q7. Is the confidence score always reliable?

**Answer:** No. The score is the model's reported confidence for its prediction. It should not automatically be treated as a calibrated probability of correctness.

## 23. Key Takeaways

- Understand the fundamentals of NLP modeling.
- Understand the differences between RNNs and Transformers.
- Understand attention and self-attention.
- Understand Query, Key, and Value.
- Understand pretrained models and fine-tuning.
- Use Hugging Face pipelines for NLP inference.
- Build reusable prediction functions with input validation.