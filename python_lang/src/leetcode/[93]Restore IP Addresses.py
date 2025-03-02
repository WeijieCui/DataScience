# A valid IP address consists of exactly four integers separated by single dots.
#  Each integer is between 0 and 255 (inclusive) and cannot have leading zeros. 
# 
#  
#  For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011
# .255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses. 
#  
# 
#  Given a string s containing only digits, return all possible valid IP 
# addresses that can be formed by inserting dots into s. You are not allowed to reorder 
# or remove any digits in s. You may return the valid IP addresses in any order. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "25525511135"
# Output: ["255.255.11.135","255.255.111.35"]
#  
# 
#  Example 2: 
# 
#  
# Input: s = "0000"
# Output: ["0.0.0.0"]
#  
# 
#  Example 3: 
# 
#  
# Input: s = "101023"
# Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 20 
#  s consists of digits only. 
#  
# 
#  Related Topics String Backtracking 👍 5161 👎 785


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        length = len(s)
        ips = []
        for i in range(min(3, length - 3)):
            ni = s[:i + 1]
            print('ni:', ni)
            if int(ni) > 255 or (len(ni) > 1 and ni[0] == '0'):
                continue
            for j in range(min(3, length - (i + 1) - 2)):
                nj = s[i + 1:i + 1 + j + 1]
                print('nj:', nj)
                if int(nj) > 255 or (len(nj) > 1 and nj[0] == '0'):
                    continue
                for k in range(min(3, length - (i + 1) - (j + 1) - 1)):
                    nk = s[i + 1 + j + 1: i + 1 + j + 1 + k + 1]
                    nl = s[i + 1 + j + 1 + k + 1:]
                    print('nk,nl:', nk, nl)
                    if (int(nk) <= 255 and not (len(nk) > 1 and nk[0] == '0')
                            and int(nl) <= 255 and not (len(nl) > 1 and nl[0] == '0')):
                        ips.append('{}.{}.{}.{}'.format(ni, nj, nk, nl))
        return ips
        # leetcode submit region end(Prohibit modification and deletion)
