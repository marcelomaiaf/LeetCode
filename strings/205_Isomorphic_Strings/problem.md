# [205. Isomorphic Strings](https://leetcode.com/problems/isomorphic-strings/description/)

<div align="center">
  <img alt="difficulty" src="https://img.shields.io/badge/Difficulty-Easy-brightgreen" />
  <img alt="topic" src="https://img.shields.io/badge/Topic-Hash%20Table-blue" />
  <img alt="topic" src="https://img.shields.io/badge/Topic-String-teal" />
</div>

<br>

<details open>
  <summary><strong>Problem Statement</strong></summary>
  <br>
  <p>
    Given two strings <code>s</code> and <code>t</code>, determine if they are isomorphic.
  </p>
  <p>
    Two strings <code>s</code> and <code>t</code> are isomorphic if the characters in
    <code>s</code> can be replaced to get <code>t</code>.
  </p>
  <p>
    All occurrences of a character must be replaced with another character while
    preserving the order of characters. No two characters may map to the same
    character, but a character may map to itself.
  </p>
</details>

<details open>
  <summary><strong>Examples</strong></summary>
  <br>

  <strong>Example 1</strong>

  <pre><code>Input: s = "egg", t = "add"
Output: true
Explanation:
The strings s and t can be made identical by:
Mapping 'e' to 'a'.
Mapping 'g' to 'd'.</code></pre>

  <strong>Example 2</strong>

  <pre><code>Input: s = "f11", t = "b23"
Output: false
Explanation:
The strings s and t can not be made identical as '1' needs to be mapped to both '2' and '3'.</code></pre>

  <strong>Example 3</strong>

  <pre><code>Input: s = "paper", t = "title"
Output: true</code></pre>
</details>

<details open>
  <summary><strong>Constraints</strong></summary>
  <br>
  <ul>
    <li><code>1 &lt;= s.length &lt;= 5 * 10^4</code></li>
    <li><code>t.length == s.length</code></li>
    <li><code>s</code> and <code>t</code> consist of any valid ASCII character.</li>
  </ul>
</details>

<details>
  <summary><strong>Notes</strong></summary>
  <br>
  <ul>
    <li>Use two hash maps (or two-way checks) to guarantee a one-to-one mapping.</li>
    <li>If an existing mapping conflicts at any position, return <code>false</code>.</li>
  </ul>
</details>
