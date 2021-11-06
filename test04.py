# Author: Gan Li
# Date: 10/28/21 4:59 下午
# Description:
def reverse_str(st, pos=0, rev=""):
    """
    Returns a new string that is the reverse of st
    When first called, the pos parameter must be zero and
    the rev parameter must be "" (the empty string)
    """
    if pos == len(st):
        return rev

    return reverse_str(st, pos+1, st[pos] + rev)
