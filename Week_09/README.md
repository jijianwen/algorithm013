# 第9周学习笔记
## 高级动态规划
动态规划 Dynamic Programming
1. Simplifying a complicated problem by breaking it down into simpler sub-problems
1. Divide & Conquer + Optimal substructure
1. 顺推形式：动态递推

DP顺推模板
```python
function DP():
    dp = [][] # 二维情况

    for i = 0..M {
        for j = 0..N {
            dp[i][j] = _Function(dp[i'][j']...)
    }
```
动态规划和递归或者分治没有根本上的区别（关键看有无最优的子结构）
拥有共性: 找到重复子问题
**差异性:最优子结构，中途可以淘汰次优解**

## 字符串算法
字符串
* Python
```python
x = 'abbc'
x = "abbc"
```
* Java
```Java
String x = "abbc"
```
* C++
```c++
string x("abbc")
```
string immutable:
https://lemire.me/blog/2017/07/07/are-your-strings-immutable/

遍历字符串
* Python
```python
for ch in "abbc":
    print(ch)
```
* Java:
```java
String x = "abbc"
for (int i = 0; i < x.size(); i++) {
    char ch = x.charAt(i)
}
for ch in x.toCharArray() {
    System.out.println(ch);
}
```
* C++
```c++
stirng x("abbc")
for (int i = 0; i < x.lengt(); i++) {
    cout << x[i];
}
```
字符串比较
Java:
String x = new String("abb");
String y = new String("abb");

x == y --> false

x.equals(y) --> true
x.equalsIgnoreCase(y) --> true

### 字符串匹配算法
1. 暴力法
1. Rabin-Karp算法
1. KMP算法

暴力法:
```java
public static int forceSearch(String txt, String pat) {
    int M = txt.length()
    int N = pat.length()

    for (int i = 0; i < M-N; i++) {
        int j;
        for (j = 0; j < N; j++) {
            if (txt.charAt[i] != txt.charAt[j])
                break;
        }
        if (j == N) {
            return i;
        }
    }
    return -1;
}
```

Rabin-Karp算法思想：
1. 假设子串的长度为M(pat), 目标字符串长度为N(txt)
1. 计算子串的hash值hash_pat
1. 计算目标字符串txt中每个长度为M的子串的hash值(共需要计算N-M+1次)
1. 比较hash值：如果hash值不同，字符串必然不匹配；如果hash值相同，还需要用朴素算法再次判断

KMP算法
当子串与目标字符串不匹配时，我们已经知道了前面已经匹配成功那一部分的字符。设法利用这个已知信息，不要把搜索为子移回已经比较过的位置，继续把它向后移，这样就提高了效率。
