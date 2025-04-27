# Inclusion-Exclusion Principle

The **Principle of Inclusion-Exclusion** (PIE) is a fundamental concept in combinatorics and set theory.
It helps in **accurately counting** the number of elements in the **union of multiple sets** by correcting for **overcounting**.

---

## Motivation (Mathematical Idea)

When adding the sizes of multiple sets, elements that belong to more than one set are **counted multiple times**.
Thus, to find the correct size of the union:

- **Include** sizes of individual sets.
- **Exclude** sizes of pairwise intersections (elements counted twice).
- **Include again** triple intersections (because they were excluded multiple times).
- And so on, **alternating** between addition and subtraction.

---

## Mathematical Formulas

For 2 sets A and B:  
$|A \cup B| = |A| + |B| - |A \cap B|$

For 3 sets A, B, and C:  
$|A \cup B \cup C| = |A| + |B| + |C| - (|A \cap B| + |B \cap C| + |C \cap A|) + |A \cap B \cap C|$

General form for n sets:  
$\left| \bigcup_{i=1}^{n} A_i \right| = \sum_{i} |A_i| - \sum_{i<j} |A_i \cap A_j| + \sum_{i<j<k} |A_i \cap A_j \cap A_k| - \cdots + (-1)^{n+1} |A_1 \cap A_2 \cap \cdots \cap A_n|$


---

## Logical Interpretation

In **logic**, PIE corresponds to operations on **Boolean expressions**:

- **Set union** $A \cup B$ corresponds to logical **OR** $A \lor B$.
- **Set intersection** $A \cap B$ corresponds to logical **AND** $A \land B$.

Thus, when we want to find how many elements satisfy "**$A$ OR $B$ OR $C$**", PIE tells us:

- Add the number satisfying **$A$**, **$B$**, and **$C$** individually.
- Subtract those satisfying **both** (like $A \land B$, $B \land C$, $C \land A$).
- Add back those satisfying **all three** ($A \land B \land C$).

---

## Key Takeaways

- **Mathematically**, PIE corrects overcounting when sets overlap.
- **Logically**, PIE models how **OR** conditions in Boolean expressions behave.
- **Alternate between adding and subtracting** based on how many sets are intersecting.

## Questions: 
- LeetCode 2654 - Minimum Number of Operations to Make All Array Elements Equal to 1
- LeetCode 898 - Bitwise ORs of Subarrays
- LeetCode 919 - Number of Subsequences That Satisfy the Given Sum Condition
- LeetCode 1930 - Unique Length-3 Palindromic Subsequences
- LeetCode 1359 - Count All Valid Pickup and Delivery Options
- LeetCode 2475 - Number of Unequal Triplets in Array
- LeetCode 2549 - Count Distinct Integers After Reverse Operations
- LeetCode 2444 - Count Subarrays With Fixed Bounds

**Bonus (Advanced):**
- LeetCode 2801 - Count Stepping Numbers in Range
- LeetCode 2597 - The Number of Beautiful Subsets

