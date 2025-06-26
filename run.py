from evaluate import compute_bleu

bleu_score = compute_bleu("data/reference.txt", "data/hypothesis.txt")
print(f"BLEU Score: {bleu_score:.2f}")
