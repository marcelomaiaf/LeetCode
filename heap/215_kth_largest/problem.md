# [215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/description/)

<div align="center">
  <img alt="difficulty" src="https://img.shields.io/badge/Difficulty-Medium-orange" />
  <img alt="topic" src="https://img.shields.io/badge/Topic-Heap-blue" />
  <img alt="topic" src="https://img.shields.io/badge/Topic-Quickselect-teal" />
  <img alt="topic" src="https://img.shields.io/badge/Topic-Divide%20and%20Conquer-6a5acd" />
</div>

<br>

<details open>
  <summary><strong>Problem Statement</strong></summary>
  <br>
  <p>
    Given an integer array <code>nums</code> and an integer <code>k</code>, return the
    <code>k</code>th largest element in the array.
  </p>
  <p>
    Note that it is the <code>k</code>th largest element in the sorted order,
    not the <code>k</code>th distinct element.
  </p>
  <p>Can you solve it without sorting?</p>
</details>

<details open>
  <summary><strong>Examples</strong></summary>
  <br>

  <strong>Example 1</strong>

  <pre><code>Input: nums = [3,2,1,5,6,4], k = 2
Output: 5</code></pre>

  <strong>Example 2</strong>

  <pre><code>Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4</code></pre>
</details>

<details open>
  <summary><strong>Constraints</strong></summary>
  <br>
  <ul>
    <li><code>1 &lt;= k &lt;= nums.length &lt;= 10^5</code></li>
    <li><code>-10^4 &lt;= nums[i] &lt;= 10^4</code></li>
  </ul>
</details>

<details>
  <summary><strong>Notes</strong></summary>
  <br>
  <ul>
    <li>The answer is based on sorted order, not distinct values.</li>
    <li>Common approaches: Min-Heap of size k, or Quickselect (average O(n)).</li>
  </ul>
</details>
