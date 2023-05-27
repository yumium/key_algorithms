# Jane Street Video Example Interview - Software Engineer

# Unit conversion
"""
example facts: (str, float, str)
    m = 3.28 ft
    ft = 12 in
    hr = 60 min
    min = 60 sec
example queries: (float, str, str)
    2 m = ? in      --> answer = 78.72
    13 in = ? m     --> answer = 0.330 (roughly)
    13 in = ? hr    --> "not convertible!"
"""

class Converter:
    def __init__(self, facts):
        self.graph = {}  # u1 => {u2, u3, ...} where there is a conversion bewteen u1 and u2/u3/... in `facts`
        self.table = {} # (u1, u2) => num s.t. 1 of u1 is num of u2
        self.populate_graph(facts)

    def populate_graph(self, facts):
        for u1_, num_, u2_ in facts:
            if u1_ in self.graph:
                self.graph[u1_].add(u2_)
            else:
                self.graph[u1_] = {u2_}

            if u2_ in self.graph:
                self.graph[u2_].add(u1_)
            else:
                self.graph[u2_] = {u1_}
            self.table[(u1_, u2_)] = num_
            self.table[(u2_, u1_)] = 1 / num_

    def convert(self, num, u1, u2):
        '''
        Given:
            num: (float)    Number of u1
            u1: (str)       Unit from
            u2: (str)       Unit to
            facts: (list)   A list of tuples (u1', num', u2') facts where 1 of u1' = num' of u2'
                len(facts) >= 0
                u1 != u2
        Return:
            A number `n` s.t. num of u1 is n of u2, or the string "not convertible!" otherwise
        Do we need to say "roughly"?

        Obs:
        - u1 and u2 are convertible iff u1 and u2 are nodes in fact graph & there is a path between u1 and u2

        Time: O(F)
        Space: O(F)
        '''
        if u1 in self.graph and u2 in self.graph:
            seen = {u1}
            q = [(u1, num)]  # Invariant: all tuples added to `q` are equivalent to each other
            while len(q) > 0:
                unit_from, value = q.pop()
                for unit_to in self.graph[unit_from]:
                    if unit_to == u2:
                        return value * self.table[(unit_from, unit_to)]
                    elif unit_to not in seen:
                        seen.add(unit_to)
                        q.insert(0, (unit_to, value * self.table[(unit_from, unit_to)]))

        return "not convertible!"

# write tests
facts = [
    ('m', 3.28, 'ft'),
    ('ft', 12.0, 'in'),
    ('hr', 60.0, 'min'),
    ('min', 60.0, 'sec')
]

queries = [
    (2.0, 'm', 'in'),
    (13.0, 'in', 'm'),
    (13.0, 'in', 'hr')
]

answers = [
    78.22,
    0.330,
    "not convertible!"
]

def main():
    conv = Converter(facts)
    eps = 1E-2  # 1% relative error
    for q, ans in zip(queries, answers):
        res = conv.convert(*q)
        assert type(res) == type(ans), type(res)
        if type(res) == type('string'):
            assert res == ans
        else:
            assert abs(res - ans) / ans < eps, res
    print('Test cases finished successfully!')

if __name__ == '__main__':
    main()
