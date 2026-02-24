# [129. Sum Root to Leaf Numbers](https://leetcode.com/problems/sum-root-to-leaf-numbers/description/?envType=study-plan-v2&envId=top-interview-150)

<div align="center">
  <img alt="difficulty" src="https://img.shields.io/badge/Difficulty-Medium-orange" />
  <img alt="topic" src="https://img.shields.io/badge/Topic-Tree-blue" />
  <img alt="topic" src="https://img.shields.io/badge/Topic-Depth--First%20Search-teal" />
  <img alt="topic" src="https://img.shields.io/badge/Topic-Binary%20Tree-6a5acd" />
</div>

<br>

<details open>
  <summary><strong>Problem Statement</strong></summary>
  <br>
  <p>
    You are given the <code>root</code> of a binary tree containing digits from
    <code>0</code> to <code>9</code> only.
  </p>
  <p>
    Each root-to-leaf path in the tree represents a number.
  </p>
  <p>
    For example, the root-to-leaf path <code>1 -&gt; 2 -&gt; 3</code> represents the
    number <code>123</code>.
  </p>
  <p>
    Return the total sum of all root-to-leaf numbers.
    Test cases are generated so that the answer will fit in a 32-bit integer.
  </p>
  <p>
    A leaf node is a node with no children.
  </p>
</details>

<details open>
  <summary><strong>Examples</strong></summary>
  <br>

  <strong>Example 1</strong>

  <pre><code>Input: root = [1,2,3]
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.</code></pre>

  <strong>Example 2</strong>

  <pre><code>Input: root = [4,9,0,5,1]
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.</code></pre>
</details>

<details open>
  <summary><strong>Constraints</strong></summary>
  <br>
  <ul>
    <li>The number of nodes in the tree is in the range <code>[1, 1000]</code>.</li>
    <li><code>0 &lt;= Node.val &lt;= 9</code></li>
    <li>The depth of the tree will not exceed <code>10</code>.</li>
  </ul>
</details>

<details>
  <summary><strong>Notes</strong></summary>
  <br>
  <ul>
    <li>Build each path value as <code>current * 10 + node.val</code> while traversing.</li>
    <li>When reaching a leaf, add the built value to the answer.</li>
    <li>DFS (recursive or iterative) is the most direct approach.</li>
  </ul>
</details>
