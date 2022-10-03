"""
Going back to part 1's code and changing a few things.
We'll add more neurons and inputs

"""
# 4 inputs with 3 Neurons and 3 outputs
inputs = [1, 2, 3, 2.5]

weights_1 = [0.2, 0.8, -0.5, 1.0]
weights_2 = [0.5, -0.91, 0.26, -0.5]
weights_3 = [-0.26, -0.27, 0.17, 0.87]

bias_1 = 2
bias_2 = 3
bias_3 = 0.5

output = [  # Neuron 1
            inputs[0]*weights_1[0] + inputs[1]*weights_1[1] + \
            inputs[2]*weights_1[2] + inputs[3]*weights_1[3] + \
            bias_1,

            # Neuron 2
            inputs[0] * weights_2[0] + inputs[1] * weights_2[1] + \
            inputs[2] * weights_2[2] + inputs[3] * weights_2[3] + \
            bias_2,

            # Neuron 3
            inputs[0]*weights_3[0] + inputs[1]*weights_3[1] + \
            inputs[2]*weights_3[2] + inputs[3]*weights_3[3] + \
            bias_3]

print(output)

""" 
Each Neuron has it's own bias :)
"""
