# [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/description/)

<div align="center">
  <img alt="difficulty" src="https://img.shields.io/badge/Difficulty-Medium-orange" />
  <img alt="topic" src="https://img.shields.io/badge/Topic-Sliding%20Window-blue" />
  <img alt="topic" src="https://img.shields.io/badge/Topic-Hash%20Map-teal" />
  <img alt="topic" src="https://img.shields.io/badge/Topic-Two%20Pointers-6a5acd" />
</div>

<br>

<details open>
  <summary><strong>Problem Statement</strong></summary>
  <br>
  <p>
    Given a string <code>s</code>, find the length of the longest substring without
    duplicate characters.
  </p>
</details>

<details open>
  <summary><strong>Examples</strong></summary>
  <br>

  <strong>Example 1</strong>

  <pre><code>Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab"
are also correct answers.</code></pre>

  <strong>Example 2</strong>

  <pre><code>Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.</code></pre>

  <strong>Example 3</strong>

  <pre><code>Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. Notice that the answer must
be a substring, "pwke" is a subsequence and not a substring.</code></pre>
</details>

<details open>
  <summary><strong>Constraints</strong></summary>
  <br>
  <ul>
    <li><code>0 &lt;= s.length &lt;= 5 * 10^4</code></li>
    <li><code>s consists of English letters, digits, symbols and spaces.</code></li>
  </ul>
</details>

<details>
  <summary><strong>Notes</strong></summary>
  <br>
  <ul>
    <li>Track last seen positions to maintain a valid window.</li>
    <li>Sliding window yields linear time on the input size.</li>
  </ul>
</details>
