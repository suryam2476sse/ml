def find_s(training_data):
    """
    Implements the FIND-S algorithm.
    training_data: list of tuples (attributes, label)
    label is 'Yes' for positive examples and 'No' for negative examples
    """

    # Step 1: Initialize hypothesis to the most specific hypothesis
    num_attributes = len(training_data[0][0])
    hypothesis = ['0'] * num_attributes

    # Step 2: Process each training example
    for attributes, label in training_data:
        if label == 'Yes':  # Only consider positive examples
            for i in range(num_attributes):
                if hypothesis[i] == '0':
                    hypothesis[i] = attributes[i]
                elif hypothesis[i] != attributes[i]:
                    hypothesis[i] = '?'

    return hypothesis
