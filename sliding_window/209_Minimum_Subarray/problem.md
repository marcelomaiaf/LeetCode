# [209. Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/description/)

<div align="center">
  <img alt="difficulty" src="https://img.shields.io/badge/Difficulty-Medium-orange" />
  <img alt="topic" src="https://img.shields.io/badge/Topic-Sliding%20Window-blue" />
  <img alt="topic" src="https://img.shields.io/badge/Topic-Array-teal" />
  <img alt="topic" src="https://img.shields.io/badge/Topic-Binary%20Search-6a5acd" />
</div>

<br>

<details open>
  <summary><strong>Problem Statement</strong></summary>
  <br>
  <p>
    Given an array of positive integers <code>nums</code> and a positive integer
    <code>target</code>, return the minimal length of a subarray whose sum is greater
    than or equal to <code>target</code>.
  </p>
  <p>
    If there is no such subarray, return <code>0</code> instead.
  </p>
</details>

<details open>
  <summary><strong>Examples</strong></summary>
  <br>

  <strong>Example 1</strong>

  <pre><code>Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.</code></pre>

  <strong>Example 2</strong>

  <pre><code>Input: target = 4, nums = [1,4,4]
Output: 1</code></pre>

  <strong>Example 3</strong>

  <pre><code>Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0</code></pre>
</details>

<details open>
  <summary><strong>Constraints</strong></summary>
  <br>
  <ul>
    <li><code>1 &lt;= target &lt;= 10^9</code></li>
    <li><code>1 &lt;= nums.length &lt;= 10^5</code></li>
    <li><code>1 &lt;= nums[i] &lt;= 10^4</code></li>
  </ul>
</details>

<details>
  <summary><strong>Notes</strong></summary>
  <br>
  <ul>
    <li>Because all numbers are positive, a sliding window finds the answer in <code>O(n)</code>.</li>
    <li>Follow-up asks for an <code>O(n log n)</code> approach, typically via prefix sums + binary search.</li>
  </ul>
</details>
