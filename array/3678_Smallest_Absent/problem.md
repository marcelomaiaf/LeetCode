# [3678. Smallest Absent Positive Greater Than Average](https://leetcode.com/problems/smallest-absent-positive-greater-than-average/)

<div align="center">
  <img alt="difficulty" src="https://img.shields.io/badge/Difficulty-Easy-brightgreen" />
  <img alt="topic" src="https://img.shields.io/badge/Topic-Array-blue" />
  <img alt="topic" src="https://img.shields.io/badge/Topic-Hash%20Set-teal" />
  <img alt="topic" src="https://img.shields.io/badge/Topic-Math-6a5acd" />
</div>

<br>

<details open>
  <summary><strong>Problem Statement</strong></summary>
  <br>
  <p>
    You are given an integer array <code>nums</code>.
  </p>
  <p>
    Return the smallest absent positive integer in <code>nums</code> such that it is
    strictly greater than the average of all elements in <code>nums</code>.
  </p>
  <p>
    The average of an array is defined as the sum of all its elements divided by
    the number of elements.
  </p>
</details>

<details open>
  <summary><strong>Examples</strong></summary>
  <br>

  <strong>Example 1</strong>

  <pre><code>Input: nums = [3,5]
Output: 6
Explanation:
The average of nums is (3 + 5) / 2 = 8 / 2 = 4.
The smallest absent positive integer greater than 4 is 6.</code></pre>

  <strong>Example 2</strong>

  <pre><code>Input: nums = [-1,1,2]
Output: 3
Explanation:
The average of nums is (-1 + 1 + 2) / 3 = 2 / 3 = 0.667.
The smallest absent positive integer greater than 0.667 is 3.</code></pre>

  <strong>Example 3</strong>

  <pre><code>Input: nums = [4,-1]
Output: 2
Explanation:
The average of nums is (4 + (-1)) / 2 = 3 / 2 = 1.50.
The smallest absent positive integer greater than 1.50 is 2.</code></pre>
</details>

<details open>
  <summary><strong>Constraints</strong></summary>
  <br>
  <ul>
    <li><code>1 &lt;= nums.length &lt;= 100</code></li>
    <li><code>-100 &lt;= nums[i] &lt;= 100</code></li>
  </ul>
</details>

<details>
  <summary><strong>Notes</strong></summary>
  <br>
  <ul>
    <li>Start from the smallest positive integer greater than the average.</li>
    <li>Use a set for O(1) membership checks while advancing to the first absent value.</li>
  </ul>
</details>

