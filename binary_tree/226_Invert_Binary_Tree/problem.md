# [226. Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/description/)

<div align="center">
  <img alt="difficulty" src="https://img.shields.io/badge/Difficulty-Easy-brightgreen" />
  <img alt="topic" src="https://img.shields.io/badge/Topic-Tree-blue" />
  <img alt="topic" src="https://img.shields.io/badge/Topic-Depth--First%20Search-teal" />
</div>

<br>

<details open>
  <summary><strong>Problem Statement</strong></summary>
  <br>
  <p>
    Given the root of a binary tree, invert the tree, and return its root.
  </p>
</details>

<details open>
  <summary><strong>Examples</strong></summary>
  <br>

  <strong>Example 1</strong>

  <pre><code>Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]</code></pre>

  <strong>Example 2</strong>

  <pre><code>Input: root = [2,1,3]
Output: [2,3,1]</code></pre>

  <strong>Example 3</strong>

  <pre><code>Input: root = []
Output: []</code></pre>
</details>

<details open>
  <summary><strong>Constraints</strong></summary>
  <br>
  <ul>
    <li>The number of nodes in the tree is in the range <code>[0, 100]</code>.</li>
    <li><code>-100 &lt;= Node.val &lt;= 100</code></li>
  </ul>
</details>

<details>
  <summary><strong>Notes</strong></summary>
  <br>
  <ul>
    <li>Swap each node's left and right children.</li>
    <li>You can solve it recursively (DFS) or iteratively (BFS/stack).</li>
  </ul>
</details>
