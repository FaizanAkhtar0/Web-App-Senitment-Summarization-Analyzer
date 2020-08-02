import re
import nltk
import heapq
from Analyzer.models_lib.basic_nlp import NLP
from nltk.tokenize import word_tokenize

class SummarizationAnalyzer:

    def __init__(self):
        self._nlp = NLP()

    def _get_all_word_freq(self, filtered_sentence_list):
        all_word_freq = {}
        for word in word_tokenize(' '.join(filtered_sentence_list)):
            if word not in all_word_freq.keys():
                all_word_freq[word] = 1
            else:
                all_word_freq[word] += 1
        return all_word_freq

    def _get_max_frequency(self, all_word_freq):
        return max(all_word_freq.values())

    def _get_average_freq_per_word(self, all_word_freq, max_freq):
        for word in all_word_freq.keys():
            all_word_freq[word] = (all_word_freq[word] / max_freq)
        return all_word_freq

    def _get_sentence_score_for_average_distribution_per_sentence(self, filtered_sentence_list, average_freq_per_word):
        sentence_scores = {}
        for sent in filtered_sentence_list:
            for word in word_tokenize(sent):
                if word in average_freq_per_word.keys():
                    if len(sent.split(' ')) < 30:
                        if sent not in sentence_scores.keys():
                            sentence_scores[sent] = 1
                        else:
                            sentence_scores[sent] += 1
        return sentence_scores

    def Summarize(self, input_text):
        filtered_sentence_list = self._nlp.make_lower(self._nlp.remove_stopwords(
            self._nlp.remove_special_characters(
                self._nlp.tokenize(input_text, sent_token=True), remove_digits=True)))

        all_word_frequency = self._get_all_word_freq(filtered_sentence_list=filtered_sentence_list)
        max_frequency = self._get_max_frequency(all_word_freq=all_word_frequency)
        average_frequency_per_word = self._get_average_freq_per_word(all_word_freq=all_word_frequency, max_freq=max_frequency)

        sentences_with_scores = self._get_sentence_score_for_average_distribution_per_sentence(
            filtered_sentence_list=filtered_sentence_list, average_freq_per_word=average_frequency_per_word
        )

        return heapq.nlargest(round(len(filtered_sentence_list) * 0.3),
                              sentences_with_scores, key=sentences_with_scores.get)



