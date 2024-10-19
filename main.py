# Load model directly
from transformers import AutoTokenizer, AutoModelForQuestionAnswering

tokenizer = AutoTokenizer.from_pretrained("kranasian/albert_v2_lookup_spending_category")
model = AutoModelForQuestionAnswering.from_pretrained("kranasian/albert_v2_lookup_spending_category")

