# [28. Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/)

<div align="center">
  <img alt="difficulty" src="https://img.shields.io/badge/Difficulty-Easy-brightgreen" />
  <img alt="topic" src="https://img.shields.io/badge/Topic-String-blue" />
  <img alt="topic" src="https://img.shields.io/badge/Topic-Two%20Pointers-teal" />
  <img alt="topic" src="https://img.shields.io/badge/Topic-String%20Matching-6a5acd" />
</div>

<br>

<details open>
  <summary><strong>Problem Statement</strong></summary>
  <br>
  <p>
    Given two strings <code>needle</code> and <code>haystack</code>, return the index of
    the first occurrence of <code>needle</code> in <code>haystack</code>, or <code>-1</code>
    if <code>needle</code> is not part of <code>haystack</code>.
  </p>
</details>

<details open>
  <summary><strong>Examples</strong></summary>
  <br>

  <strong>Example 1</strong>

  <pre><code>Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.</code></pre>

  <strong>Example 2</strong>

  <pre><code>Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.</code></pre>
</details>

<details open>
  <summary><strong>Constraints</strong></summary>
  <br>
  <ul>
    <li><code>1 &lt;= haystack.length, needle.length &lt;= 10^4</code></li>
    <li><code>haystack</code> and <code>needle</code> consist of only lowercase English characters.</li>
  </ul>
</details>

<details>
  <summary><strong>Notes</strong></summary>
  <br>
  <ul>
    <li>Return the index of the first full match of <code>needle</code> inside <code>haystack</code>.</li>
    <li>If no match exists, return <code>-1</code>.</li>
  </ul>
</details>
