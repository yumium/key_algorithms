# Source: https://leetcode.com/problems/accounts-merge/

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        '''
        Given:
            accounts: A list of accounts (of format ['name', 'email1', 'email2', ...])
                1 <= len(account) <= 1000
                2 <= len(account[i]) <= 10 at least 1 email per person
                1 <= len(accounts[i][j]) <= 30
        Return:
            A list of accounts merged
        '''
        # Build graph: index -> set of indices of neighbours

        emails = {}  # Account index -> set of emails
        for i in range(len(accounts)):
            emails[i] = set(accounts[i][1:])

        graph = {i: set() for i in range(len(accounts))}
        for i in range(len(accounts)):
            for email in emails[i]:
                for j in range(len(accounts)):
                    if i == j:
                        continue

                    if email in emails[j]:
                        graph[i].add(j)
        
        ccs = self.ccs(graph)  # O(N^2)

        print(ccs)
        res = []
        for cc in ccs:
            es = set()
            for i in cc:
                es |= emails[i]
            res.append([accounts[cc[0]][0]] + sorted(list(es)))

        return res

    def ccs(self, graph):
        ccs = []
        cc = []
        seen = set()
        for n in graph:
            if n not in seen:
                self.visit(graph, n, seen, cc)
                ccs.append(cc)
                cc = []
        return ccs

    def visit(self, graph, n, seen, cc):
        seen.add(n)
        for u in graph[n]:
            if u not in seen:
                self.visit(graph, u, seen, cc)
        cc.append(n)



