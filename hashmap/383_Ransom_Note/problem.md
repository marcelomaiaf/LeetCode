# [383. Ransom Note](https://leetcode.com/problems/ransom-note/description/)

<div align="center">
  <img alt="difficulty" src="https://img.shields.io/badge/Difficulty-Easy-brightgreen" />
  <img alt="topic" src="https://img.shields.io/badge/Topic-Hash%20Table-blue" />
  <img alt="topic" src="https://img.shields.io/badge/Topic-String-teal" />
  <img alt="topic" src="https://img.shields.io/badge/Topic-Counting-6a5acd" />
</div>

<br>

<details open>
  <summary><strong>Problem Statement</strong></summary>
  <br>
  <p>
    Given two strings <code>ransomNote</code> and <code>magazine</code>, return
    <code>true</code> if <code>ransomNote</code> can be constructed by using the
    letters from <code>magazine</code>, and <code>false</code> otherwise.
  </p>
  <p>
    Each letter in <code>magazine</code> can only be used once in
    <code>ransomNote</code>.
  </p>
</details>

<details open>
  <summary><strong>Examples</strong></summary>
  <br>

  <strong>Example 1</strong>

  <pre><code>Input: ransomNote = "a", magazine = "b"
Output: false</code></pre>

  <strong>Example 2</strong>

  <pre><code>Input: ransomNote = "aa", magazine = "ab"
Output: false</code></pre>

  <strong>Example 3</strong>

  <pre><code>Input: ransomNote = "aa", magazine = "aab"
Output: true</code></pre>
</details>

<details open>
  <summary><strong>Constraints</strong></summary>
  <br>
  <ul>
    <li><code>1 &lt;= ransomNote.length, magazine.length &lt;= 10^5</code></li>
    <li><code>ransomNote</code> and <code>magazine</code> consist of lowercase English letters.</li>
  </ul>
</details>

<details>
  <summary><strong>Notes</strong></summary>
  <br>
  <ul>
    <li>Count each character frequency in <code>magazine</code>.</li>
    <li>Consume counts while iterating through <code>ransomNote</code>.</li>
    <li>If any required character is missing (or exhausted), return <code>false</code>.</li>
  </ul>
</details>
