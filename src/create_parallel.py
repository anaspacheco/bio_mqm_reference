import os
import csv 
import json

'''
The corpus is a courtesy of the authors of the paper: 
@article{zouhar2024finetuned,
      title={Fine-Tuned Machine Translation Metrics Struggle in Unseen Domains},
      author={Vilém Zouhar and Shuoyang Ding and Anna Currey and Tatyana Badeka and Jenyuan Wang and Brian Thompson},
      year={2024},
      eprint={2402.18747},
      archivePrefix={arXiv},
      journal={arXiv preprint arXiv:2306.07899},
      url={https://arxiv.org/abs/2402.18747}
}
'''

LANGUAGE_CODES = {
    "1":"en",
    "2":"pt",
    "3":"de",
    "4": "es", 
    "5": "fr",
    "6": "zh",
    "7": "ru",
}

def main():
    print("Welcome! To create the parallel corpora, please choose (1) source and (2) target languages")
    src = input("Choose source language:\n(1)english\n(2)portuguese\n(3)german\n(4)spanish\n(5)french\n(6)chinese\n(7)russian\n>").lower()
    if src not in LANGUAGE_CODES:
        raise ValueError("Invalid source language.")
    trg = input("Choose target language:\n(1)english\n(2)portuguese\n(3)german\n(4)spanish\n(5)french\n(6)chinese\n(7)russian\n>").lower()
    if trg not in LANGUAGE_CODES:
        raise ValueError("Invalid target language.")
    elif src == trg:
        raise ValueError("Source and target languages must be different.")
    elif src != "1":
        if trg != "1":
            raise ValueError("One of the languages must be English.")
    
    filename = f"reference_{LANGUAGE_CODES[src]}2{LANGUAGE_CODES[trg]}.json"
    with open(f"../orig_data/{filename}", "r") as f:
        prev_sent = ""
        data = json.load(f) 
        sent_id = 0
        for item in data:
            errors = item.get("target_errors", [])
            if any(error["severity"] != "Critical" for error in errors) and item["source"] != prev_sent:
                sent_id += 1
                src_sentence = item["source"]
                trg_sentence = item["target"]
                with open(f"../prl_data/{LANGUAGE_CODES[src]}2{LANGUAGE_CODES[trg]}/{LANGUAGE_CODES[src]}.txt", "a", encoding="utf-8") as f_src:
                    f_src.write(f"{sent_id}\t{src_sentence}\n")
                with open(f"../prl_data/{LANGUAGE_CODES[src]}2{LANGUAGE_CODES[trg]}/{LANGUAGE_CODES[trg]}.txt", "a", encoding="utf-8") as f_trg:
                    f_trg.write(f"{sent_id}\t{trg_sentence}\n")
                prev_sent = item["source"]
            if sent_id == 100:
                break

if __name__ == "__main__":
    main()
