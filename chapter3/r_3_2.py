# The number of operations executed by algorithms A and B is 8*n*log(n) and
# 2*n^2, respectively. Determine n0 such that A is better than B for n ≥ n0.

# Algorithm A performs
# 8 n log n
# operations and algorithm B performs
# 2 n²
# operations, so A is faster when:
#
# [
# 8*n*log(n) <= 2*n^2
# ]
#
# This is the correct condition to solve for (n_0).
#
# You can simplify the inequality:
#
# [
# 8n \log n \le 2n^2
# ]
#
# Divide both sides by (2n) (valid for (n > 0)):
#
# [
# 4 \log n \le n
# ]
#
# So the task reduces to finding the smallest (n) such that:
#
# 4 \log n \le n
#
# The exact value depends on the logarithm base (typically base 2 in algorithm analysis).
# Testing small values (base 2):
#
# | n  | 4 log₂ n | n ≥ 4 log₂ n? |
# | -- | -------- | ------------- |
# | 8  | 12       | no            |
# | 16 | 16       | equal         |
# | 17 | 16.09    | yes           |
#
# Therefore:
#
# * (n_0 = 16) is the crossover point where both algorithms are equal
# * For all (n > 16), algorithm A is asymptotically better than B
#
# So your setup and inequality are correct; you only need to solve or approximate the threshold value of (n).
