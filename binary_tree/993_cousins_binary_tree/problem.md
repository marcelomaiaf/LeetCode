# [993. Cousins in Binary Tree](https://leetcode.com/problems/cousins-in-binary-tree/description/)

<div align="center">
  <img alt="difficulty" src="https://img.shields.io/badge/Difficulty-Easy-brightgreen" />
  <img alt="topic" src="https://img.shields.io/badge/Topic-Tree-blue" />
  <img alt="topic" src="https://img.shields.io/badge/Topic-Binary%20Tree-ff8c00" />
</div>

<br>

<details open>
  <summary><strong>Problem Statement</strong></summary>
  <br>
  <p>
    Given the <code>root</code> of a binary tree with unique values and the values of two different nodes of the tree <code>x</code> and <code>y</code>, return <code>true</code> <em>if the nodes corresponding to the values </em><code>x</code><em> and </em><code>y</code><em> in the tree are <strong>cousins</strong>, or </em><code>false</code><em> otherwise.</em>
  </p>
  <p>
    Two nodes of a binary tree are <strong>cousins</strong> if they have the same depth with different parents.
  </p>
  <p>
    Note that in a binary tree, the root node is at the depth <code>0</code>, and children of each depth <code>k</code> node are at the depth <code>k + 1</code>.
  </p>
</details>

<details open>
  <summary><strong>Examples</strong></summary>
  <br>

  <strong>Example 1</strong>

  <pre><code>Input: root = [1,2,3,4], x = 4, y = 3
Output: false</code></pre>

  <strong>Example 2</strong>

  <pre><code>Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true</code></pre>

  <strong>Example 3</strong>

  <pre><code>Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false</code></pre>
</details>

<details open>
  <summary><strong>Constraints</strong></summary>
  <br>
  <ul>
    <li>The number of nodes in the tree is in the range <code>[2, 100]</code>.</li>
    <li><code>1 &lt;= Node.val &lt;= 100</code></li>
    <li>Each node has a <strong>unique</strong> value.</li>
    <li><code>x != y</code></li>
    <li><code>x</code> and <code>y</code> both exist in the tree.</li>
  </ul>
</details>

<details>
  <summary><strong>Notes</strong></summary>
  <br>
  <ul>
    <li>Track the depth and parent of each target node, then compare the two results.</li>
    <li>A DFS or BFS traversal works well because each visit can carry the current depth and parent.</li>
  </ul>
</details>
