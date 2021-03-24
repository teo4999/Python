from collections import defaultdict

eps = '~'


# transformare din expresie regulata in automat finit nedeterminist
class RegexToNFA:
    def __init__(self, alphabet=None):
        self.states = set()
        self.transition_function = defaultdict(defaultdict)
        self.alphabet = alphabet
        self.start_state = None
        self.final_states = []

    # se seteaza starea initiala
    def set_start(self, state):
        self.start_state = state
        self.states.add(state)

    # se seteaza starea finala
    def set_final(self, final_states):
        if isinstance(final_states, int):
            final_states = [final_states]

        for state in final_states:
            self.final_states.append(state)

    # se adauga o singura tranzitie in matricea delta
    def add_transition(self, origin, destination, value):
        if isinstance(value, str):
            value = {value}
        self.states.add(origin)
        self.states.add(destination)

        if origin in self.transition_function and destination in self.transition_function[origin]:
            self.transition_function[origin][destination] = self.transition_function[origin][destination].union(value)
        else:
            self.transition_function[origin][destination] = value

    # se adauga mai multe tranzitii
    def add_transitions(self, transitions):
        for origin, destinations in transitions.items():
            for destination in destinations:
                self.add_transition(origin, destination, transitions[origin][destination])

    # se deplaseaza automatul cu num pozitii
    def move_states(self, num):
        new_fa = RegexToNFA(alphabet=self.alphabet)

        moves = {}
        for state in self.states:
            moves[state] = num
            num += 1
        new_fa.set_start(moves[self.start_state])
        for final_state in self.final_states:
            new_fa.set_final(moves[final_state])

        for origin, destinations in self.transition_function.items():
            for destination in destinations:
                new_fa.add_transition(moves[origin], moves[destination], self.transition_function[origin][destination])

        return new_fa, num - 1

    # afisarea automatului
    def print_nfa(self, output_location):
        output_file = open(output_location, "w")
        output_file.write(str(len(self.states)))
        output_file.write("\n")

        for state in self.final_states:
            output_file.write(str(state) + " ")
        output_file.write("\n")

        for origin, destinations in sorted(self.transition_function.items()):
            values_dict = dict()
            for destination in destinations:
                for value in self.transition_function[origin][destination]:
                    if value not in values_dict.keys():
                        values_dict[value] = set()
                        values_dict[value].add(destination)
                    else:
                        values_dict[value].add(destination)
            for value in values_dict.keys():
                output_file.write(str(origin) + " ")
                if value != eps:
                    output_file.write(value + " ")
                else:
                    output_file.write("eps ")
                for destination in values_dict[value]:
                    output_file.write(str(destination) + " ")
                output_file.write("\n")
        output_file.close()

	# automat cu 2 stari si o valoare
    @staticmethod
    def add_variable(value):
        fa = RegexToNFA()
        fa.set_start(0)
        fa.set_final([1])
        fa.add_transition(0, 1, value)

        return fa

	# concatenarea a doua automate
    @staticmethod
    def concatenation(fa1, fa2):
        fa1, max1 = fa1.move_states(0)
        fa2, max2 = fa2.move_states(max1)

        result = RegexToNFA()
        result.set_start(fa1.start_state)
        result.set_final(fa2.final_states)

        result.add_transitions(fa1.transition_function)
        result.add_transitions(fa2.transition_function)

        return result
	
	# aplicarea kleene star asupra unui automat
    @staticmethod
    def kleene_star(fa):
        fa, max = fa.move_states(1)

        result = RegexToNFA()
        result.set_start(0)
        result.set_final(max + 1)

        result.add_transition(0, fa.start_state, eps)
        result.add_transition(0, max + 1, eps)

        for final_state in fa.final_states:
            result.add_transition(final_state, max + 1, eps)
            result.add_transition(final_state, fa.start_state, eps)

        result.add_transitions(fa.transition_function)

        return result
	
	# aplicarea "|" asupra unui automat
    @staticmethod
    def union(fa1, fa2):
        fa1, max1 = fa1.move_states(1)
        fa2, max2 = fa2.move_states(max1 + 1)

        result = RegexToNFA()
        result.set_start(0)
        result.set_final(max2 + 1)

        result.add_transition(result.start_state, fa2.start_state, eps)
        result.add_transition(result.start_state, fa1.start_state, eps)

        for final_state_left in fa1.final_states:
            result.add_transition(final_state_left, max2 + 1, eps)
        for final_state_right in fa2.final_states:
            result.add_transition(final_state_right, max2 + 1, eps)

        result.add_transitions(fa1.transition_function)
        result.add_transitions(fa2.transition_function)

        return result
