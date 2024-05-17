# bio_mqm_eval

### Study on GPT-4-Turbo's Accuracy for Sentence-Level Translation of Biomedical Literature

**Language Pairs:**
- English to Portuguese (en2pt)
- Portuguese to English (pt2en)
- English to Spanish (en2es)
- Spanish to English (es2en)
- English to Russian (en2ru)
- Russian to English (ru2en)
- English to Chinese (en2zh)
- Chinese to English (zh2en)
- English to French (en2fr)
- French to English (fr2en)
- English to German (en2de)
- German to English (de2en)

**Folders:**
- **orig_data:** Contains the original JSON files from the MQM Database
- **prl_data:** Contains parallel data for the language pairs
- **evaluation_files:** Includes BLEU, CHRF, and TER scores for individual sentences
- **result_files:** Contains translations by Deepl, Google Translate, and GPT-4-Turbo API

**Dataset Authors:**
@article{zouhar2024finetuned,
      title={Fine-Tuned Machine Translation Metrics Struggle in Unseen Domains},
      author={Vilém Zouhar and Shuoyang Ding and Anna Currey and Tatyana Badeka and Jenyuan Wang and Brian Thompson},
      year={2024},
      eprint={2402.18747},
      archivePrefix={arXiv},
      journal={arXiv preprint arXiv:2402.18747},
      url={https://arxiv.org/abs/2402.18747}
}
