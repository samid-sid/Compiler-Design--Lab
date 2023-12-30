def remove_space(s):
    return s.strip()

def break_production(s, spliter):
    tokens = s.split(spliter)
    return [token.strip() for token in tokens]

def calculate_follow(symbol, production_rules, first_sets, follow_sets, visited):
    visited.add(symbol)
    follow_sets.setdefault(symbol, set())

    for left_symbol, productions in production_rules.items():
        for production in productions:
            for i in range(len(production)):
                if production[i] == symbol:
                    if i < len(production) - 1:
                        next_symbol = production[i + 1]
                        if next_symbol not in production_rules:
                            follow_sets[symbol].add(next_symbol)
                        else:
                            first_of_next = first_sets[next_symbol]
                            follow_sets[symbol].update(first_of_next)
                            follow_sets[symbol].discard("#")
                            if "#" in first_of_next and next_symbol not in visited:
                                calculate_follow(next_symbol, production_rules, first_sets, follow_sets, visited)
                                follow_of_next = follow_sets[next_symbol]
                                follow_sets[symbol].update(follow_of_next)
                    else:
                        if left_symbol != symbol and left_symbol not in visited:
                            calculate_follow(left_symbol, production_rules, first_sets, follow_sets, visited)
                        if left_symbol != symbol and left_symbol in production_rules:
                            follow_of_left = follow_sets[left_symbol]
                            follow_sets[symbol].update(follow_of_left)

    visited.remove(symbol)

def calculate_first_function(symbol, production_rules, first_sets):
    if symbol in first_sets:
        return first_sets[symbol]

    first_set = set()

    for production in production_rules[symbol]:
        for term in production:
            if term not in production_rules:
                first_set.add(term)
                break
            else:
                term_first = calculate_first_function(term, production_rules, first_sets)
                first_set.update(term_first)
                if "#" not in term_first:
                    break

    first_sets[symbol] = first_set
    return first_set

def main():
    num_rules = int(input("Enter the number of grammar rules: "))
    production_rules = {}

    for _ in range(num_rules):
        rule = input(f"Enter grammar rule {_ + 1}: ")
        arrow_pos = rule.find("->")
        symbol = remove_space(rule[:arrow_pos])

        production_part = remove_space(rule[arrow_pos + 2:])
        alternatives = break_production(production_part, '|')

        for alt in alternatives:
            parts = alt.split()
            production_rules.setdefault(symbol, []).append(parts)

    first_sets = {}
    for rule in production_rules:
        calculate_first_function(rule, production_rules, first_sets)

    for symbol, first_set in first_sets.items():
        print(f"FIRST({symbol}) = {{ {', '.join(first_set)} }}")

    print()

    follow_sets = {next(iter(production_rules)): set('$')}
    visited = set()

    for rule in production_rules:
        calculate_follow(rule, production_rules, first_sets, follow_sets, visited)

    for symbol, follow_set in follow_sets.items():
        print(f"FOLLOW({symbol}) = {{ {', '.join(follow_set)} }}")

if __name__ == "__main__":
    main()
