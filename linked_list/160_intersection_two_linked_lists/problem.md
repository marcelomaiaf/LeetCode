# [160. Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/description/)

<div align="center">
  <img alt="difficulty" src="https://img.shields.io/badge/Difficulty-Easy-brightgreen" />
  <img alt="topic" src="https://img.shields.io/badge/Topic-Hash%20Table-blue" />
  <img alt="topic" src="https://img.shields.io/badge/Topic-Linked%20List-teal" />
  <img alt="topic" src="https://img.shields.io/badge/Topic-Two%20Pointers-6a5acd" />
</div>

<br>

<details open>
  <summary><strong>Problem Statement</strong></summary>
  <br>
  <p>
    Given the heads of two singly linked lists <code>headA</code> and <code>headB</code>,
    return the node at which the two lists intersect. If the two linked lists have no
    intersection at all, return <code>null</code>.
  </p>
  <p>
    The test cases are generated such that there are no cycles anywhere in the entire
    linked structure, and the linked lists must retain their original structure after
    the function returns.
  </p>
  <p>
    The inputs used by the custom judge include <code>intersectVal</code>,
    <code>listA</code>, <code>listB</code>, <code>skipA</code>, and <code>skipB</code>.
    The judge builds the linked structure from those values and passes only
    <code>headA</code> and <code>headB</code> to your function.
  </p>
</details>

<details open>
  <summary><strong>Examples</strong></summary>
  <br>

  <strong>Example 1</strong>

  <pre><code>Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Intersected at '8'
Explanation: The intersected node's value is 8. There are 2 nodes before the intersected node in A and 3 nodes before the intersected node in B.
Note that the nodes with value 1 in A and B are different node references, while the nodes with value 8 in A and B point to the same location in memory.</code></pre>

  <strong>Example 2</strong>

  <pre><code>Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Intersected at '2'
Explanation: The intersected node's value is 2. There are 3 nodes before the intersected node in A and 1 node before the intersected node in B.</code></pre>

  <strong>Example 3</strong>

  <pre><code>Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: No intersection
Explanation: The two lists do not intersect, so return null.</code></pre>
</details>

<details open>
  <summary><strong>Constraints</strong></summary>
  <br>
  <ul>
    <li>The number of nodes of <code>listA</code> is in the range <code>[1, 3 * 10^4]</code>.</li>
    <li>The number of nodes of <code>listB</code> is in the range <code>[1, 3 * 10^4]</code>.</li>
    <li><code>1 &lt;= Node.val &lt;= 10^5</code></li>
    <li><code>0 &lt;= skipA &lt;= m</code></li>
    <li><code>0 &lt;= skipB &lt;= n</code></li>
    <li><code>intersectVal</code> is <code>0</code> if <code>listA</code> and <code>listB</code> do not intersect.</li>
    <li><code>intersectVal == listA[skipA] == listB[skipB]</code> if <code>listA</code> and <code>listB</code> intersect.</li>
  </ul>
</details>

<details open>
  <summary><strong>Follow-up</strong></summary>
  <br>
  <p>
    Could you write a solution that runs in <code>O(m + n)</code> time and uses only
    <code>O(1)</code> memory?
  </p>
</details>

<details>
  <summary><strong>Notes</strong></summary>
  <br>
  <ul>
    <li>The intersection is determined by node reference, not by node value.</li>
    <li>A hash-based solution works in linear time, but the follow-up asks for constant extra space.</li>
  </ul>
</details>
