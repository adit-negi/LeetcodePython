class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        clips.sort()
        if T == 0:
            return 0
        last = 0
        cnt = 1
        first = 0
        i = 0
        while i < len(clips):

            if clips[i][0] == first:
                last = clips[i][1]
                if last >= T:
                    return cnt
            elif clips[i][0] > first:
                cnt += 1
                if clips[i][0] > last:
                    return -1
                else:
                    temp = last
                    while i < len(clips) and clips[i][0] <= temp:
                        last = max(last, clips[i][1])
                        if last >= T:
                            return cnt
                        i += 1

                    if i == len(clips):
                        if T > last:
                            return -1
                        return cnt
                    first = clips[i][0]
            i += 1
        if clips[-1][1] == T:
            return cnt+1
        if T > last:
            return -1
        return cnt
