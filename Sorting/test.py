
# s = "abbda"
s="aca"

def check_palindrome(le,ri):  
    print(le, ri)  
    while(le<ri):
        if s[le] != s[ri]:
            return False
        le += 1
        ri -= 1
    return True
l,r = 0, len(s)-1       
while(l<r):
    if s[l] != s[r]:
        r_l = check_palindrome(l+1, r)
        r_r = check_palindrome(l, r-1)
        # return r_l or r_r
        print(f"r_l : {r_l} and r_r : {r_r}")
    l += 1
    r -= 1
# print(s, "un_match_count is :",un_match_count)