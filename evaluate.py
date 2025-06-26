import sacrebleu

def compute_bleu(reference_file, hypothesis_file):
    with open(reference_file, 'r', encoding='utf-8') as ref_file:
        references = ref_file.readlines()

    with open(hypothesis_file, 'r', encoding='utf-8') as hyp_file:
        hypotheses = hyp_file.readlines()

    bleu = sacrebleu.corpus_bleu(hypotheses, [references])
    return bleu.score
