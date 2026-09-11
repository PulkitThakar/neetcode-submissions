class Solution:
    def simplifyPath(self, path: str) -> str:
        path_list = path.split('/')
        temp = []
        print(path_list)
        for i in path_list:
            if i == "" or i == ".":
                continue
            elif i == "..":
                if temp:
                    temp.pop()
                else:
                    continue
            else:
                temp.append(i)
        path_list = temp
        print(path_list)
        res = "/" + "/".join(path_list)
        return res