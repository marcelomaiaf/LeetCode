# [977. Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/description/)

<div align="center">
  <img alt="difficulty" src="https://img.shields.io/badge/Difficulty-Easy-brightgreen" />
  <img alt="topic" src="https://img.shields.io/badge/Topic-Array-blue" />
  <img alt="topic" src="https://img.shields.io/badge/Topic-Two%20Pointers-teal" />
  <img alt="topic" src="https://img.shields.io/badge/Topic-Sorting-6a5acd" />
</div>

<br>

<details open>
  <summary><strong>Problem Statement</strong></summary>
  <br>
  <p>
    Given an integer array <code>nums</code> sorted in <strong>non-decreasing</strong> order, return <em>an array of <strong>the squares of each number</strong> sorted in non-decreasing order</em>.
  </p>
</details>

<details open>
  <summary><strong>Examples</strong></summary>
  <br>

  <strong>Example 1</strong>

  <pre><code>Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].</code></pre>

  <strong>Example 2</strong>

  <pre><code>Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]</code></pre>
</details>

<details open>
  <summary><strong>Constraints</strong></summary>
  <br>
  <ul>
    <li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
    <li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
    <li><code>nums</code> is sorted in <strong>non-decreasing</strong> order.</li>
  </ul>
</details>

<details>
  <summary><strong>Follow-up</strong></summary>
  <br>
  <ul>
    <li>Squaring each element and sorting the new array is very trivial. Can you find an <code>O(n)</code> solution using a different approach?</li>
  </ul>
</details>

<details>
  <summary><strong>Notes</strong></summary>
  <br>
  <ul>
    <li>Move the two pointers according to a clear invariant instead of treating them as independent scans.</li>
    <li>Sorting is often the simplest way to make order-dependent relationships explicit before scanning.</li>
  </ul>
</details>
