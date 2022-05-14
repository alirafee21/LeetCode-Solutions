class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a, b = a[::-1] , b[::-1]
        stra = '' 
        carry = 0 
        right_bit = ''
        for i in range(max(len(a),len(b))):
            if i < len(a):
                digit1 = int(a[i])
            else:
                digit1 = 0
            if i < len(b):
                digit2 = int(b[i])
            else:
                digit2 = 0
                
            tot = digit1 + digit2 + carry 
            stra = str(tot % 2) + stra
            carry = tot // 2
            
        if carry:
            stra = '1' + stra
            
        return stra