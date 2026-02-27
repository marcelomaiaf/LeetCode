# [189. Rotate Array](https://leetcode.com/problems/rotate-array/description/)

<div align="center">
  <img alt="difficulty" src="https://img.shields.io/badge/Difficulty-Medium-yellow" />
  <img alt="topic" src="https://img.shields.io/badge/Topic-Array-blue" />
  <img alt="topic" src="https://img.shields.io/badge/Topic-Math-teal" />
  <img alt="topic" src="https://img.shields.io/badge/Topic-Two%20Pointers-6a5acd" />
</div>

<br>

<details open>
  <summary><strong>Problem Statement</strong></summary>
  <br>
  <p>
    Given an integer array <code>nums</code>, rotate the array to the right by
    <code>k</code> steps, where <code>k</code> is non-negative.
  </p>
</details>

<details open>
  <summary><strong>Examples</strong></summary>
  <br>

  <strong>Example 1</strong>

  <pre><code>Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]</code></pre>

  <strong>Example 2</strong>

  <pre><code>Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]</code></pre>
</details>

<details open>
  <summary><strong>Constraints</strong></summary>
  <br>
  <ul>
    <li><code>1 &lt;= nums.length &lt;= 10^5</code></li>
    <li><code>-2^31 &lt;= nums[i] &lt;= 2^31 - 1</code></li>
    <li><code>0 &lt;= k &lt;= 10^5</code></li>
  </ul>
</details>

<details>
  <summary><strong>Follow-up</strong></summary>
  <br>
  <ul>
    <li>Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.</li>
    <li>Could you do it in-place with <code>O(1)</code> extra space?</li>
  </ul>
</details>

<details>
  <summary><strong>Notes</strong></summary>
  <br>
  <ul>
    <li>When <code>k</code> is larger than the array length, rotating by <code>k % nums.length</code> is enough.</li>
    <li>A common in-place solution is based on reversing the whole array, then reversing each rotated part.</li>
  </ul>
</details>
