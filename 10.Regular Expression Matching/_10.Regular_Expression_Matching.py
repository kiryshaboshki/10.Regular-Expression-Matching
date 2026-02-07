class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        pred = [False] * (len(p) + 1)
        tek = [False] * (len(p) + 1)

        pred[0] = True

        for j in range(1, len(p) + 1):
            if p[j-1] == '*':
                pred[j] = pred[j-2]

        for i in range(1, len(s) + 1):
            tek[0] = False

            for j in range(1, len(p) + 1):
                if p[j-1] == '*':
                    if p[j-2] == s[i-1] or p[j-2] == '.':
                        tek[j] = tek[j-2] or pred[j]
                    else:
                        tek[j] = tek[j-2]
                elif p[j-1] == '.' or p[j-1] == s[i-1]:
                    tek[j] = pred[j-1]
                else:
                    tek[j] = False

            pred, tek = tek, [False] * (len(p) + 1)

        return pred[len(p)]

