class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

    def is_empty(self):
        return len(self.stack) == 0


def precedence(operator_symbol):
    if operator_symbol in ('+', '-'):
        return 1
    if operator_symbol in ('*', '/'):
        return 2
    return 0

def apply_operator(a, b, operator_symbol):
    if operator_symbol == '+': return a + b
    if operator_symbol == '-': return a - b
    if operator_symbol == '*': return a * b
    if operator_symbol == '/': return a / b

def evaluate(expression_text):
    value_stack = Stack()
    operator_stack = Stack()
    i = 0 #character_position

    while i < len(expression_text):
        if expression_text[i] == ' ':
            i += 1
            continue

        elif expression_text[i].isdigit():
            number_value = 0
            while i < len(expression_text) and expression_text[i].isdigit():
                number_value = number_value * 10 + int(expression_text[i])
                i += 1
            value_stack.push(number_value)
            continue

        elif expression_text[i] == '(':
            operator_stack.push(expression_text[i])

        elif expression_text[i] == ')':
            while not operator_stack.is_empty() and operator_stack.peek() != '(':
                number_value1 = value_stack.pop()
                number_value2 = value_stack.pop()
                pending_operator = operator_stack.pop()
                value_stack.push(apply_operator(number_value2, number_value1, pending_operator))
            operator_stack.pop()

        else:
            while (not operator_stack.is_empty() and precedence(operator_stack.peek()) >= precedence(expression_text[i])):
                number_value1 = value_stack.pop()
                number_value2 = value_stack.pop()
                pending_operator = operator_stack.pop()
                value_stack.push(apply_operator(number_value2, number_value1, pending_operator))
            operator_stack.push(expression_text[i])
        i += 1

    while not operator_stack.is_empty():
        number_value1 = value_stack.pop()
        number_value2 = value_stack.pop()
        pending_operator = operator_stack.pop()
        value_stack.push(apply_operator(number_value2, number_value1, pending_operator))

    return value_stack.pop()

def process_files():
    with open("Input.txt", "r") as input_file, open("Output.txt", "w") as output_file:
        for input_line in input_file:
            expression_line = input_line.strip()
            if expression_line == "-----":
                output_file.write("-----\n")

            elif expression_line:
                try:
                    calculated_result = evaluate(expression_line)
                    output_file.write(str(calculated_result) + "\n")
                except Exception:
                    output_file.write("Error in expression\n")

if __name__ == "__main__":
    process_files()
