class Solution:

    def encode(self, strs: List[str]) -> str:
        encodings = []
        if strs:
            for s in strs:
                if len(s) == 0:
                    e = "\\c\\"
                else:
                    e = "\\c\\".join([str(ord(c)) for c in s])
                encodings.append(e)
            return "\\l\\".join(encodings)
        else:
            return ""

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        encodings = s.split("\\l\\")
        results = []
        for e in encodings:
            decodings = [chr(int(d)) for d in e.split("\\c\\") if d]
            d = "".join(decodings)
            results.append(d)
        return results
