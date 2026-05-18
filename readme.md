Hot 100 学习
### 一刷 2026年5月16日
### nums
* 207 课程表 ———— dfs图论
* 215 数组中的第k个最大元素 ———— 快速选择
* 239 滑动窗口中的最大值 ———— 双端队列
* 300 最长递增子序列 ———— dp(len) + 二分
* 312 戳气球 ———— dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + vi* vj *vk)
* 406 身高重建队列 ———— h降序k升序,再插入
* 448 消失的数字 ———— 原地哈希
* 494 目标和 ———— neg转换 + 01背包
* 560 和为K的子数组 ———— 前缀和
* 581 无序子数组  ———— 双指针双向遍历
### string
* 003 最长无重复子串 ———— start = max(start,last_seen[ch]+1)
* 005 最长回文子串 ———— 中心扩展 + 更新公式 start = i-(ml-1)//2 ; end=i+ml//2
* 076 最小覆盖字串 ———— 滑动窗口，先r再缩l
* 139 单词拆分 ———— 动态规划 if s[j:i] in word_set and dp[j]:dp[i]=True
* 301 删除无效的括号 ———— 递归 helper(s, start, lremove, rremove)
### tree
* 094 中序遍历 ———— 迭代法
* 105 前序中序构造二叉树 ———— index_map{val:i} + helper(pre_l, pre_r, in_l, in_r)
* 124 最大路径和 ———— l = max(maxNodeSum(root.left), 0)  return max(l,r)+node.val
* 256 最近公共祖先 ———— if left and right:return root  return left if left else right
* 297 序列化和反序列化 ———— 前序
* 337 打家劫舍 ———— (偷,不偷)  sr, nr = dfs(node.right)   return node.val + nl + nr, max(sl, nl) + max(sr, nr)
* 437 路径总和Ⅲ ———— dfs(root, curr)： ret += prefix[curr - targetSum]
### link
* 002 两数相加 ———— while l1 or l2 or carry:
* 023 合并K个升序链表 ———— 二分 merge
* 148 排序链表 ———— 快慢指针二分(mid = slow) + merge(sortFunc(head, mid), sortFunc(mid, tail))
* 160 相交链表 ———— 尾部对齐
* 234 回文链表 ———— 快慢指针二分 + 逆转链表
### Else
* 079 单词搜索
* 085 最大矩形 ———— left,right 柱状图面积
* 200 岛屿数量 ———— bfs/dfs归0
* 279 完全平方数
* 338 比特位计数 ———— re.append(1 + re[i - highBit])
* 339 除法求值
* 621 任务调度器