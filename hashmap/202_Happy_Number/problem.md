# [202. Happy Number](https://leetcode.com/problems/happy-number/description/)

<div align="center">
  <img alt="difficulty" src="https://img.shields.io/badge/Difficulty-Easy-brightgreen" />
  <img alt="topic" src="https://img.shields.io/badge/Topic-Hash%20Table-blue" />
  <img alt="topic" src="https://img.shields.io/badge/Topic-Math-teal" />
  <img alt="topic" src="https://img.shields.io/badge/Topic-Two%20Pointers-6a5acd" />
</div>

<br>

<details open>
  <summary><strong>Problem Statement</strong></summary>
  <br>
  <p>
    Write an algorithm to determine if a number <code>n</code> is happy.
  </p>
  <p>
    A happy number is defined by the following process:
  </p>
  <ul>
    <li>Starting with any positive integer, replace the number by the sum of the squares of its digits.</li>
    <li>Repeat the process until the number equals <code>1</code> (where it will stay), or it loops endlessly in a cycle that does not include <code>1</code>.</li>
    <li>Numbers for which this process ends in <code>1</code> are happy.</li>
  </ul>
  <p>
    Return <code>true</code> if <code>n</code> is a happy number, and <code>false</code> otherwise.
  </p>
</details>

<details open>
  <summary><strong>Examples</strong></summary>
  <br>

  <strong>Example 1</strong>

  <pre><code>Input: n = 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1</code></pre>

  <strong>Example 2</strong>

  <pre><code>Input: n = 2
Output: false</code></pre>
</details>

<details open>
  <summary><strong>Constraints</strong></summary>
  <br>
  <ul>
    <li><code>1 &lt;= n &lt;= 2^31 - 1</code></li>
  </ul>
</details>

<details>
  <summary><strong>Notes</strong></summary>
  <br>
  <ul>
    <li>Use a set to detect repeated values and identify cycles.</li>
    <li>An alternative approach is Floyd's cycle detection (slow/fast pointers).</li>
  </ul>
</details>
