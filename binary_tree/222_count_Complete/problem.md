# [222. Count Complete Tree Nodes](https://leetcode.com/problems/count-complete-tree-nodes/description/)

<div align="center">
  <img alt="difficulty" src="https://img.shields.io/badge/Difficulty-Easy-brightgreen" />
  <img alt="topic" src="https://img.shields.io/badge/Topic-Binary%20Search-blue" />
  <img alt="topic" src="https://img.shields.io/badge/Topic-Bit%20Manipulation-teal" />
  <img alt="topic" src="https://img.shields.io/badge/Topic-Tree-6a5acd" />
  <img alt="topic" src="https://img.shields.io/badge/Topic-Binary%20Tree-ff8c00" />
</div>

<br>

<details open>
  <summary><strong>Problem Statement</strong></summary>
  <br>
  <p>
    Given the <code>root</code> of a <strong>complete</strong> binary tree, return the number of the nodes in the tree.
  </p>
  <p>
    According to <strong>Wikipedia</strong>, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between <code>1</code> and <code>2<sup>h</sup></code> nodes inclusive at the last level <code>h</code>.
  </p>
  <p>
    Design an algorithm that runs in less than <code>O(n)</code> time complexity.
  </p>
</details>

<details open>
  <summary><strong>Examples</strong></summary>
  <br>

  <strong>Example 1</strong>

  <pre><code>Input: root = [1,2,3,4,5,6]
Output: 6</code></pre>

  <strong>Example 2</strong>

  <pre><code>Input: root = []
Output: 0</code></pre>

  <strong>Example 3</strong>

  <pre><code>Input: root = [1]
Output: 1</code></pre>
</details>

<details open>
  <summary><strong>Constraints</strong></summary>
  <br>
  <ul>
    <li>The number of nodes in the tree is in the range <code>[0, 5 * 10<sup>4</sup>]</code>.</li>
    <li><code>0 &lt;= Node.val &lt;= 5 * 10<sup>4</sup></code></li>
    <li>The tree is guaranteed to be <strong>complete</strong>.</li>
  </ul>
</details>

<details>
  <summary><strong>Notes</strong></summary>
  <br>
  <ul>
    <li>Search on a monotonic condition and keep the loop invariant explicit when moving the bounds.</li>
    <li>Choose the traversal order that naturally exposes the parent-child relation the problem depends on.</li>
  </ul>
</details>
