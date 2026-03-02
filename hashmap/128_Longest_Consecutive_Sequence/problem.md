# [128. Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/description/)

<div align="center">
  <img alt="difficulty" src="https://img.shields.io/badge/Difficulty-Medium-orange" />
  <img alt="topic" src="https://img.shields.io/badge/Topic-Array-blue" />
  <img alt="topic" src="https://img.shields.io/badge/Topic-Hash%20Table-teal" />
  <img alt="topic" src="https://img.shields.io/badge/Topic-Union-Find-6a5acd" />
</div>

<br>

<details open>
  <summary><strong>Problem Statement</strong></summary>
  <br>
  <p>
    Given an unsorted array of integers <code>nums</code>, return <em>the length of the longest consecutive elements sequence.</em>
  </p>
  <p>
    You must write an algorithm that runs in <code>O(n)</code> time.
  </p>
</details>

<details open>
  <summary><strong>Examples</strong></summary>
  <br>

  <strong>Example 1</strong>

  <pre><code>Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.</code></pre>

  <strong>Example 2</strong>

  <pre><code>Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9</code></pre>

  <strong>Example 3</strong>

  <pre><code>Input: nums = [1,0,1,2]
Output: 3</code></pre>
</details>

<details open>
  <summary><strong>Constraints</strong></summary>
  <br>
  <ul>
    <li><code>0 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
    <li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
  </ul>
</details>

<details>
  <summary><strong>Notes</strong></summary>
  <br>
  <ul>
    <li>Track connected components with path compression and union by rank or size when connectivity matters.</li>
    <li>Use a hash-based structure when the solution depends on fast lookups, counts, or mappings.</li>
  </ul>
</details>
