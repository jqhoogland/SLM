class ReservoirNetwork(nn.Module):
    def __init__(self, input_size, n_neurons, output_size, spectral_radius, average_degree=6):
        super(ReservoirNetwork, self).__init__()

        self.reservoir_state = torch.zeros(n_neurons)
        self.adjacency_matrix = torch.from_numpy(initialize_reservoir(n_neurons, spectral_radius, average_degree))
        self.input_matrix = torch.zeros((input_size, n_neurons))
        self.output_layer = nn.Linear(n_neurons, output_size)
        self.output_layer.weight = torch.nn.Parameter(torch.zeros(in_dim,hid))

    def forward(self, input_):
        self.reservoir_state = nn.Tanh(torch.mm(input_matrix, input_)
                                       + torch.mm(adjacency_matrix, self.reservoir_state))
        return torch.mm(self.output_matrix, self.reservoir_state)
class ReservoirNetworkTrainer(object):
    def __init__(self, n_neurons, output_size, spectral_radius, average_degree=6):
        self.model = ReservoirNetwork(input_size, n_neurons, output_size, spectral_radius, average_degree=6)
        self.criterion = nn.MSELoss()
        self.optimizer = optim.Adam(self.model.parameters())

    def train(self, n_epochs = 100):
        """
        Optimize the weights of `self.model`.

        Args:
            `n_epochs` (int): Number of epochs used to train the network.
        """

        loss_archive = []
        for epoch in range(n_epochs):
            accuracy = self.validate()
            print(f'Accuracy: {accuracy}')
            for index, (model_input, labels) in enumerate(self.train_loader):


                model_input = Variable(model_input)
                labels = Variable(labels)

                self.optimizer.zero_grad()
                model_output = self.model(model_input)
                loss = self.criterion(model_output, labels)
                loss.backward()
                self.optimizer.step()

                if index % (n_epochs / 1) == 0:
                    print("Epoch {} - loss: {}".format(epoch, loss.item()))

                loss_archive.append(loss.item())

            validation_loss = self.validate()
            print('Validation loss: {}'.format(validation_loss))
            validation_loss_archive.append(validation_loss)

        return loss_archive, validation_loss_archive

    def test(self):
        """
        Test `self.model` and return its accuracy.
        """

        test_DA = DataAggregator("../data/combined/test_data/", batch_size=64, binary_classification=True, use_spectrograms=True, spectrogram_rows=100)
        _, test_loader = test_DA.create_training_and_validation_loaders(validation_split=1.0)
        predictions_correctness = []
        for model_input, labels in test_loader:
            model_output = torch.round(self.model(model_input))

            # add 1 if the model makes a correct prediction and 0 if not.
            predictions_correctness.extend([int(int(model_output[i]) == int(labels[i])) for i in range(len(labels))])

        return sum(predictions_correctness) / len(predictions_correctness)
