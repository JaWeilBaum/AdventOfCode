from aoc import Day
from aoc.Math import mul


class Day19(Day):

    def __init__(self):
        super().__init__(19)
        self.r = {}

    def eval(self, workflow: dict, rule_key: str) -> str:
        rules = self.r[rule_key]
        for rule in rules:
            if rule['rule'] == True:
                return rule['destination']
            letter = rule['rule'][0]
            number = int(rule['rule'].replace('>', '').replace('<', '').replace(letter, ''))
            condition = number > workflow[letter] if rule['rule'].__contains__('<') else number < workflow[letter]
            if condition:
                return rule['destination']

    def create_workflows(self, data: str):
        for workflow in data.splitlines():
            name, rest = workflow.replace('}', '').split("{")
            decisions = rest.split(',')
            dicts = []
            for decision in decisions:
                condition, *destination = decision.split(':')

                if len(destination) == 0:
                    dicts.append({"rule": True, "destination": condition})
                else:
                    dicts.append({"rule": condition, "destination": destination[0]})
            self.r[name] = dicts

    def part_one(self, raw_data: str) -> str:
        workflows, parts = raw_data.split("\n\n")

        self.create_workflows(workflows)

        A = []
        R = []

        for part in parts.splitlines():
            part = {element.split('=')[0]: int(element.split('=')[1]) for element in part.replace('}', '').replace('{', '').split(',')}

            destination = self.eval(part, "in")
            while destination not in 'AR':
                print(f"{destination} -> ", end="")
                destination = self.eval(part, destination)
            print(f"{destination}")
            if destination == 'A':
                A.append(part)
            else:
                R.append(part)

        values = [sum(list(p.values())) for p in A]
        return str(sum(values))

    def create_new_range(self, rule: str, ranges: dict) :
        def _n_r(_operator, _value, val):
            _lower, _upper = val
            if _operator == '>':
                _lower = max(_lower, _value + 1)
            elif _operator == '<':
                _upper = min(_upper, _value - 1)
            elif _operator == '>=':
                _lower = max(_lower, _value)
            elif _operator == '<=':
                _upper = min(_upper, _value)
            return [_lower, _upper]

        variable = rule[0]
        operator = rule[1:3] if '=' in rule else rule[1:2]
        value = int(rule[3:]) if '=' in rule else int(rule[2:])

        if variable == 'x':
            ranges[variable] = _n_r(operator, value, ranges['x'])
        elif variable == 'm':
            ranges[variable] = _n_r(operator, value, ranges['m'])
        elif variable == 'a':
            ranges[variable] = _n_r(operator, value, ranges['a'])
        elif variable == 's':
            ranges[variable] = _n_r(operator, value, ranges['s'])
        return ranges

    def part_two(self, raw_data: str) -> str:
        workflows, parts = raw_data.split("\n\n")
        if len(self.r) == 0:
            self.create_workflows(workflows)

        queue = [{'next': 'in', 'vals': {'x': [1, 4000], 'm': [1, 4000], 'a': [1, 4000], 's': [1, 4000]}}]

        values = []
        while len(queue) > 0:
            element = queue.pop()
            current_vals = element['vals']
            if any(list(map(lambda x: x[0] > x[1], current_vals.values()))):
                print(element)
                continue
            if element['next'] == 'A':
                values.append(mul(list(map(lambda x: (x[1] - x[0]) + 1, current_vals.values()))))
                continue
            if element['next'] == 'R':
                continue
            for rule in self.r[element['next']]:
                destination = rule['destination']
                if rule['rule'] == True:
                    queue.append({'next': destination, 'vals': current_vals})
                    break
                else:
                    queue.append({'next': destination, 'vals': self.create_new_range(rule['rule'], current_vals.copy())})

                    new_rule = rule['rule']
                    new_rule = (new_rule.replace('>', '<=') if new_rule[1] == '>' else new_rule.replace('<', '>='))
                    current_vals = self.create_new_range(new_rule, current_vals)

        return str(sum(values))

if __name__ == '__main__':
    Day19().run(False, False, True)