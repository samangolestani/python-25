from collections import Counter
import spacy
from spacy.training import Example
from spacy.tokens import Doc
from datasets import load_dataset
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load model and dataset
nlp = spacy.load("en_core_web_trf")
dataset = load_dataset("universal_dependencies", "en_ewt")
test_data = dataset["test"]

# Track gold vs predicted deps
dep_pairs = []

num_sentences = 2077

for data in test_data.select(range(num_sentences)):
    words = data['tokens']
    heads = data['head']
    deps = data['deprel']

    if len(words) != len(heads) or len(words) != len(deps):
        continue

    try:
        pred_doc = nlp(" ".join(words))
        if len(pred_doc) != len(words):
            continue

        for pred_token, gold_dep in zip(pred_doc, deps):
            pred_dep = pred_token.dep_
            dep_pairs.append((gold_dep, pred_dep))

    except Exception as e:
        print(f"Error: {e}")
        continue

# Build confusion matrix
df = pd.DataFrame(dep_pairs, columns=["Gold", "Predicted"])
conf_matrix = pd.crosstab(df["Gold"], df["Predicted"])

# Plot heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues")
plt.title("Dependency Label Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Gold")
plt.tight_layout()
plt.show()

print(df.head())