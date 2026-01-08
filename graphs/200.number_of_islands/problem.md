# [200. Number of Islands](https://leetcode.com/problems/number-of-islands/description/)

<div align="center">
  <img alt="difficulty" src="https://img.shields.io/badge/Difficulty-Medium-orange" />
  <img alt="topic" src="https://img.shields.io/badge/Topic-DFS-blue" />
  <img alt="topic" src="https://img.shields.io/badge/Topic-BFS-teal" />
  <img alt="topic" src="https://img.shields.io/badge/Topic-Union%20Find-6a5acd" />
</div>

<br>

<details open>
  <summary><strong>Problem Statement</strong></summary>
  <br>
  <p>
    Given an <code>m x n</code> 2D binary grid <code>grid</code> which represents a map of
    <code>'1'</code>s (land) and <code>'0'</code>s (water), return the number of islands.
  </p>
  <p>
    An island is surrounded by water and is formed by connecting adjacent lands
    horizontally or vertically. You may assume all four edges of the grid are all
    surrounded by water.
  </p>
</details>

<details open>
  <summary><strong>Examples</strong></summary>
  <br>

  <strong>Example 1</strong>

  <pre><code>Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1</code></pre>

  <strong>Example 2</strong>

  <pre><code>Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3</code></pre>
</details>

<details open>
  <summary><strong>Constraints</strong></summary>
  <br>
  <ul>
    <li><code>m == grid.length</code></li>
    <li><code>n == grid[i].length</code></li>
    <li><code>1 &lt;= m, n &lt;= 300</code></li>
    <li><code>grid[i][j] is '0' or '1'</code></li>
  </ul>
</details>

<details>
  <summary><strong>Notes</strong></summary>
  <br>
  <ul>
    <li>Adjacency is 4-directional (up, down, left, right).</li>
    <li>Typical solutions: DFS/BFS flood fill or Union-Find.</li>
  </ul>
</details>
