# 論理演算で差、積、商はどうやって行う？
class Operator:
    def add(self, a, b):
        def half_add(a, b):
            a0 = a & 1
            b0 = b & 1
            s = a0 ^ b0
            c = a0 & b0
            return s, c
        
        def full_add(a, b, x):
            a0 = a & 1
            b0 = b & 1
            x0 = x & 1

            s1, c1 = half_add(a0, b0)
            s2, c2 = half_add(s1, x0)

            c = c1 | c2
            return s2, c

        def byte_add(a, b, x):
            s = 0
            tmpc = x

            for bit in range(8):
                ab = (a & (1 << bit)) >> bit
                bb = (b & (1 << bit)) >> bit
                tmpx = tmpc
                tmps, tmpc = full_add(ab, bb, tmpx)
                s = s | (tmps << bit)

            return s, tmpc

        c = 0
        result = 0

        for bit in range(0, 25, 8):
            ab = (a & (0b11111111 << bit)) >> bit
            bb = (b & (0b11111111 << bit)) >> bit
            x = c
            s, c = byte_add(ab, bb, x)
            result = result | (s << bit)

        return result
    
    def sub(self, a, b):
        if a < b:
            return -self.add(b, self.add(~a, 1))
        return self.add(a, self.add(~b, 1))
    
    def mul(self, a, b):
        if a & (1 << 31):
            ua = self.sub(0, a)
            sa = 1
        else:
            ua = a
            sa = 0
        
        if b & (1 << 31):
            ub = self.sub(0, b)
            sb = 1
        else:
            ub = b
            sb = 0
        
        tmpb = ub
        bit = 0
        while tmpb > 0:
            bit = self.add(bit, 1)
            tmpb = tmpb >> 1
        
        result = 0
        while bit >= 0:
            if ub & (1 << bit):
                result = self.add(result, (ua << bit))
            bit = self.sub(bit, 1)

        if (sa == 1 and sb == 0) or (sa == 0 and sb == 1):
            result = self.sub(0, result)

        return result
    
    def div(self, a, b):
        if a & (1 << 31):
            ua = self.sub(0, a)
            sa = 1
        else:
            ua = a
            sa = 0
        
        if b & (1 << 31):
            ub = self.sub(0, b)
            sb = 1
        else:
            ub = b
            sb = 0

        temb = ub
        bit = 0
        while temb > 0:
            bit = self.add(bit, 1)
            temb = temb >> 1

        result = 0
        while bit >= 0:
            if ua >= ub << bit:
                ua = self.sub(ua, ub << bit)
                result = self.add(result, 1 << bit)
            bit = self.sub(bit, 1)

        if (sa == 1 and sb == 0) or (sa == 0 and sb == 1):
            result = self.sub(0, result)
        
        return result


if __name__ == "__main__":
    op = Operator()
    print(op.add(10, 20)) # 30
    print(op.sub(100, 20)) # 80
    print(op.mul(10, 20)) # 200
    print(op.div(100, 20)) # 5
