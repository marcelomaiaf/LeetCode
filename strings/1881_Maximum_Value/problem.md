# [1881. Maximum Value after Insertion](https://leetcode.com/problems/maximum-value-after-insertion/description/)

<div align="center">
  <img alt="difficulty" src="https://img.shields.io/badge/Difficulty-Medium-orange" />
  <img alt="topic" src="https://img.shields.io/badge/Topic-String-blue" />
  <img alt="topic" src="https://img.shields.io/badge/Topic-Greedy-teal" />
  <img alt="topic" src="https://img.shields.io/badge/Topic-Math-6a5acd" />
</div>

<br>

<details open>
  <summary><strong>Problem Statement</strong></summary>
  <br>
  <p>
    You are given a very large integer <code>n</code>, represented as a string, and an
    integer digit <code>x</code>. The digits in <code>n</code> and the digit <code>x</code>
    are in the inclusive range <code>[1, 9]</code>, and <code>n</code> may represent a
    negative number.
  </p>
  <p>
    You want to maximize <code>n</code>'s numerical value by inserting <code>x</code>
    anywhere in the decimal representation of <code>n</code>. You cannot insert
    <code>x</code> to the left of the negative sign.
  </p>
  <p>
    Return a string representing the maximum value of <code>n</code> after the insertion.
  </p>
</details>

<details open>
  <summary><strong>Examples</strong></summary>
  <br>

  <strong>Example 1</strong>

  <pre><code>Input: n = "99", x = 9
Output: "999"
Explanation: The result is the same regardless of where you insert 9.</code></pre>

  <strong>Example 2</strong>

  <pre><code>Input: n = "-13", x = 2
Output: "-123"
Explanation: You can make n one of {-213, -123, -132}, and the largest of those three is -123.</code></pre>
</details>

<details open>
  <summary><strong>Constraints</strong></summary>
  <br>
  <ul>
    <li><code>1 &lt;= n.length &lt;= 10^5</code></li>
    <li><code>1 &lt;= x &lt;= 9</code></li>
    <li>The digits in <code>n</code> are in the range <code>[1, 9]</code>.</li>
    <li><code>n</code> is a valid representation of an integer.</li>
    <li>In the case of a negative <code>n</code>, it will begin with <code>'-'</code>.</li>
  </ul>
</details>

<details>
  <summary><strong>Notes</strong></summary>
  <br>
  <ul>
    <li>For positive numbers, insert <code>x</code> before the first digit smaller than <code>x</code>.</li>
    <li>For negative numbers, insert <code>x</code> before the first digit larger than <code>x</code>.</li>
  </ul>
</details>

