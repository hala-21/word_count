# Word Frequency Counter (Python)

## Overview

This project is a **simple word-frequency counter** written in Python. It reads a text file (`story.txt`), splits the text into words, and counts how many times each word appears.

This code was created **purely as a practice project** while studying the Udemy course:
**Python for Programmers – IBM Skills Network**
[https://ibm-learning.udemy.com/course/python-for-programmers/learn/lecture/5408280#overview](https://ibm-learning.udemy.com/course/python-for-programmers/learn/lecture/5408280#overview)

The goal is learning core Python concepts, not building a production-ready NLP system.

---

## What the Code Does

1. Opens a text file using UTF-8 encoding (with error handling)
2. Reads and splits the text into words
3. Creates a dictionary where:

   * **Key** → a word
   * **Value** → number of times the word appears
4. Prints the resulting dictionary

---

## Concepts Practiced

* File handling using `with open()`
* String processing with `.split()`
* Dictionaries and key–value pairs
* Conditional logic (`if / else`)
* Iteration over lists
* Basic frequency-count algorithm

---

## Real-Life Applications

This exact logic is used in:

* Natural Language Processing (NLP) preprocessing
* Search engines (term frequency)
* Log and event analysis
* Text analytics and AI pipelines

---

## Limitations (Intentional)

* Case-sensitive word counting
* Punctuation is not removed
* Entire file is loaded into memory

These limitations are acceptable for a **learning-focused exercise**.

---

## Possible Improvements

* Convert words to lowercase for normalization
* Remove punctuation before counting
* Use `collections.Counter` for cleaner code
* Process large files line-by-line
* Export results to a file (CSV or JSON)

---

## Summary

* Purpose: **Practice Python fundamentals**
* Focus: File I/O, dictionaries, loops
* Context: **IBM – Python for Programmers (Udemy)**
* Outcome: Understanding how word-frequency counting works

---

## References

* Python File Handling (Official Docs)
  [https://docs.python.org/3/tutorial/inputoutput.html](https://docs.python.org/3/tutorial/inputoutput.html)
* Python Dictionaries
  [https://docs.python.org/3/tutorial/datastructures.html#dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
* IBM Skills Network – Python for Programmers
  [https://www.udemy.com/course/python-for-programmers/](https://www.udemy.com/course/python-for-programmers/)

---

**Author:** Practice project by Hala Abdeen
