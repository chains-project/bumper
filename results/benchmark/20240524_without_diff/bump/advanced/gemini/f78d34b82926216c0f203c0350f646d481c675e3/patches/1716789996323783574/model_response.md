```java
import org.deeplearning4j.nn.conf.NeuralNetConfiguration;
import org.deeplearning4j.nn.conf.layers.DenseLayer;
import org.deeplearning4j.nn.conf.layers.OutputLayer;
import org.deeplearning4j.nn.multilayer.MultiLayerNetwork;
import org.deeplearning4j.nn.weights.WeightInit;
import org.nd4j.linalg.activations.Activation;
import org.nd4j.linalg.api.ndarray.INDArray;
import org.nd4j.linalg.factory.Nd4j;
import org.nd4j.linalg.learning.config.Sgd;
import org.nd4j.linalg.lossfunctions.LossFunctions;

public class Neuron {

    public static void main(String[] args) {
        // Create a neural network configuration
        NeuralNetConfiguration.Builder builder = new NeuralNetConfiguration.Builder()
                .seed(123) // Seed for reproducibility
                .weightInit(WeightInit.XAVIER) // Weight initialization
                .updater(new Sgd(0.1)) // Stochastic gradient descent optimizer
                .l2(1e-4) // L2 regularization
                .list()
                .layer(0, new DenseLayer.Builder() // Hidden layer
                        .nIn(2) // Number of input neurons
                        .nOut(4) // Number of output neurons
                        .activation(Activation.SIGMOID) // Sigmoid activation function
                        .build())
                .layer(1, new OutputLayer.Builder() // Output layer
                        .nIn(4) // Number of input neurons
                        .nOut(1) // Number of output neurons
                        .lossFunction(LossFunctions.LossFunction.MSE) // Mean squared error loss function
                        .activation(Activation.IDENTITY) // Identity activation function
                        .build());

        // Create a neural network
        MultiLayerNetwork model = new MultiLayerNetwork(builder.build());
        model.init();

        // Create some training data
        INDArray input = Nd4j.create(new double[][]{{0, 0}, {0, 1}, {1, 0}, {1, 1}});
        INDArray output = Nd4j.create(new double[][]{{0}, {1}, {1}, {0}});

        // Train the neural network
        model.fit(input, output);

        // Test the neural network
        INDArray testInput = Nd4j.create(new double[][]{{0.1, 0.1}});
        INDArray testOutput = model.output(testInput);
        System.out.println(testOutput);
    }
}
```