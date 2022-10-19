def solution(p):
    def get_correct(s):
        if not s:
            return ''
        
        u, v = get_uv(s)
        if check_correct(u):
            return u + get_correct(v)
        return '(' + get_correct(v) + ')' + reverse_u(u[1:-1])

    
    def get_uv(s):
        lc = rc = 0
        if s[0] == '(':
            lc += 1
        else:
            rc += 1

        for i in range(1, len(s)):
            if s[i] == '(':
                lc += 1
            else:
                rc += 1
            
            if lc == rc:
                break

        return s[:i+1], s[i+1:]
    

    def reverse_u(s):
        rev = ''
        for char in s:
            if char == '(':
                rev += ')'
            else:
                rev += '('
        return rev

    
    def check_correct(s):
        return

    
    return get_correct(p)
