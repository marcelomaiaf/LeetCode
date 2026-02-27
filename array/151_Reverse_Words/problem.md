# [151. Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/description/)

<div align="center">
  <img alt="difficulty" src="https://img.shields.io/badge/Difficulty-Medium-yellow" />
  <img alt="topic" src="https://img.shields.io/badge/Topic-Two%20Pointers-blue" />
  <img alt="topic" src="https://img.shields.io/badge/Topic-String-teal" />
</div>

<br>

<details open>
  <summary><strong>Problem Statement</strong></summary>
  <br>
  <p>
    Given an input string <code>s</code>, reverse the order of the words.
  </p>
  <p>
    A word is defined as a sequence of non-space characters. The words in
    <code>s</code> will be separated by at least one space.
  </p>
  <p>
    Return a string of the words in reverse order concatenated by a single
    space.
  </p>
  <p>
    Note that <code>s</code> may contain leading or trailing spaces or multiple
    spaces between two words. The returned string should only have a single
    space separating the words. Do not include any extra spaces.
  </p>
</details>

<details open>
  <summary><strong>Examples</strong></summary>
  <br>

  <strong>Example 1</strong>

  <pre><code>Input: s = "the sky is blue"
Output: "blue is sky the"</code></pre>

  <strong>Example 2</strong>

  <pre><code>Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.</code></pre>

  <strong>Example 3</strong>

  <pre><code>Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.</code></pre>
</details>

<details open>
  <summary><strong>Constraints</strong></summary>
  <br>
  <ul>
    <li><code>1 &lt;= s.length &lt;= 10^4</code></li>
    <li><code>s</code> contains English letters (upper-case and lower-case), digits, and spaces <code>' '</code>.</li>
    <li>There is at least one word in <code>s</code>.</li>
  </ul>
</details>

<details>
  <summary><strong>Follow-up</strong></summary>
  <br>
  <ul>
    <li>If the string data type is mutable in your language, can you solve it in-place with <code>O(1)</code> extra space?</li>
  </ul>
</details>

<details>
  <summary><strong>Notes</strong></summary>
  <br>
  <ul>
    <li>Ignore extra spaces at the beginning, at the end, and between words when building the final answer.</li>
    <li>A direct approach is to split the words, reverse their order, and join them back with a single space.</li>
  </ul>
</details>
