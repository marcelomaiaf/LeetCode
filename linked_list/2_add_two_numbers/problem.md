# [2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers/description/)

<div align="center">
  <img alt="difficulty" src="https://img.shields.io/badge/Difficulty-Medium-orange" />
  <img alt="topic" src="https://img.shields.io/badge/Topic-Linked%20List-blue" />
  <img alt="topic" src="https://img.shields.io/badge/Topic-Math-teal" />
  <img alt="topic" src="https://img.shields.io/badge/Topic-Recursion-6a5acd" />
</div>

<br>

<details open>
  <summary><strong>Problem Statement</strong></summary>
  <br>
  <p>
    You are given two non-empty linked lists representing two non-negative integers.
    The digits are stored in reverse order, and each of their nodes contains a single
    digit. Add the two numbers and return the sum as a linked list.
  </p>
  <p>
    You may assume the two numbers do not contain any leading zero, except the number
    <code>0</code> itself.
  </p>
</details>

<details open>
  <summary><strong>Examples</strong></summary>
  <br>

  <strong>Example 1</strong>

  <pre><code>Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.</code></pre>

  <strong>Example 2</strong>

  <pre><code>Input: l1 = [0], l2 = [0]
Output: [0]</code></pre>

  <strong>Example 3</strong>

  <pre><code>Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]</code></pre>
</details>

<details open>
  <summary><strong>Constraints</strong></summary>
  <br>
  <ul>
    <li>The number of nodes in each linked list is in the range <code>[1, 100]</code>.</li>
    <li><code>0 &lt;= Node.val &lt;= 9</code></li>
    <li>It is guaranteed that the list represents a number that does not have leading zeros.</li>
  </ul>
</details>

<details>
  <summary><strong>Notes</strong></summary>
  <br>
  <ul>
    <li>Process both lists digit by digit and keep track of carry.</li>
    <li>If a carry remains after both lists end, append one more node.</li>
  </ul>
</details>
