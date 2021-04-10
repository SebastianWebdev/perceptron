import random

class Perceptron:
    def __init__(self, activation_value, correction_value=0.1, dimension=1):
        self.correction = correction_value
        self.activationValue = activation_value
        self.inputs = []
        self.weights = []
        self.dimension = dimension
        self.sum = 0
        self.output = 0
        for x in range(dimension):
            self.weights.insert(x, random.uniform(-0.5, 0.5))

    def sumator(self):
        i = 0
        sum = 0
        for u in self.inputs:
            sum += u * self.weights[i]
            i += 1
        return sum - self.activationValue

    def print_data(self):
        print("")
        print("----------------------")
        print("Wagi:", self.weights)
        print("Inputs:", self.inputs)
        print("Suma:", self.sum)
        print("Wynik:", self.output)
        print("-----------------------")
        print("")

    def activation(self, sum):
        if sum >= 0:
            self.output = 1
        else:
            self.output = 0

    def compute(self, inputs):
        if len(inputs) != self.dimension:
            raise Exception("Liczba wejść musi być równa:" + str(self.dimension))
        self.inputs = inputs
        sum = self.sumator()
        self.activation(sum)

        return self.output

    def learn(self, learning_data):
        for U in learning_data:
            local_inputs = U[0]
            correct_output = U[1]
            result = self.compute(local_inputs)
            i = 0

            print(self.weights)
            for w in self.weights:
                print(w)
                new_weight = w + self.correction * local_inputs[i] * (correct_output - result)
                self.weights[i] = new_weight
                i += 1



learning_dat = [[[0, 0], 0], [[0, 1], 0], [[1, 0], 0], [[1, 1], 1]]

and_perceptron = Perceptron(0.7, 0.1, 2)

and_perceptron.learn(learning_dat)
and_perceptron.learn(learning_dat)
and_perceptron.learn(learning_dat)
and_perceptron.learn(learning_dat)
and_perceptron.learn(learning_dat)
and_perceptron.learn(learning_dat)




print(and_perceptron.compute([0, 0]), "output: 0")
print(and_perceptron.compute([0, 1]), "output: 0")
print(and_perceptron.compute([1, 0]), "output: 0")
print(and_perceptron.compute([1, 1]), "output: 1")
