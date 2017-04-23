# hackcu_alteryx_challenge

2017 HackCU Alteryx Encryption Challenger

Solution by:
Cameron Taylor
Peter Huynh
Jackson Roberts
(Steven) Jace Conflenti

# Why this challenge was impossible.

After cracking the initial substitution cypher using a dictionary attack, the real challenge began: decyphering a language used by elementary schoolers.

Pig latin has a lot of ambiguous situations. For example, "swarm" codes to "armsway". However, "warms" also encodes to "armsway". Additionally, the encoding method used the Alteryx to create the encoded text jumbled the order of any word containing punctuation characters.

Even when correctly taking consonant clusters into account, the obstacle of ambiguity.

One method used for the words "wings" and "swings" was to always move the consonant cluster to the beginning. However, this caused the phrase "intersway" (winter) to incorrectly decode to "swinter".

We got close, and correctly identified the text as the complete works of Shakespeare. However, fully decoding the pig latin text with an algortithm proved to be undoable short of using TensorFlow to recognize context and decode accordingly.

