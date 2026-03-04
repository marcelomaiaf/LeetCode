# [208. Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/description/)

<div align="center">
  <img alt="difficulty" src="https://img.shields.io/badge/Difficulty-Medium-orange" />
  <img alt="topic" src="https://img.shields.io/badge/Topic-Hash%20Table-blue" />
  <img alt="topic" src="https://img.shields.io/badge/Topic-String-teal" />
  <img alt="topic" src="https://img.shields.io/badge/Topic-Design-6a5acd" />
  <img alt="topic" src="https://img.shields.io/badge/Topic-Trie-ff8c00" />
</div>

<br>

<details open>
  <summary><strong>Problem Statement</strong></summary>
  <br>
  <p>
    A <strong>trie</strong> (pronounced as "try") or <strong>prefix tree</strong> is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.
  </p>
  <p>
    Implement the Trie class:
  </p>
  <ul>
    <li><code>Trie()</code> Initializes the trie object.</li>
    <li><code>void insert(String word)</code> Inserts the string <code>word</code> into the trie.</li>
    <li><code>boolean search(String word)</code> Returns <code>true</code> if the string <code>word</code> is in the trie (i.e., was inserted before), and <code>false</code> otherwise.</li>
    <li><code>boolean startsWith(String prefix)</code> Returns <code>true</code> if there is a previously inserted string <code>word</code> that has the prefix <code>prefix</code>, and <code>false</code> otherwise.</li>
  </ul>
</details>

<details open>
  <summary><strong>Examples</strong></summary>
  <br>

  <strong>Example 1</strong>

  <pre><code>Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]
Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True</code></pre>
</details>

<details open>
  <summary><strong>Constraints</strong></summary>
  <br>
  <ul>
    <li><code>1 &lt;= word.length, prefix.length &lt;= 2000</code></li>
    <li><code>word</code> and <code>prefix</code> consist only of lowercase English letters.</li>
    <li>At most <code>3 * 10<sup>4</sup></code> calls <strong>in total</strong> will be made to <code>insert</code>, <code>search</code>, and <code>startsWith</code>.</li>
  </ul>
</details>

<details>
  <summary><strong>Notes</strong></summary>
  <br>
  <ul>
    <li>Use a hash-based structure when the solution depends on fast lookups, counts, or mappings.</li>
    <li>Process characters in order and preserve the positional rules described in the prompt.</li>
  </ul>
</details>
