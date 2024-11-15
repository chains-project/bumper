```java
import org.deeplearning4j.nn.conf.NeuralNetConfiguration;
import org.deeplearning4j.nn.conf.layers.DenseLayer;
import org.deeplearning4j.nn.conf.layers.OutputLayer;
import org.deeplearning4j.nn.multilayer.MultiLayerNetwork;
import org.deeplearning4j.nn.weights.WeightInit;
import org.nd4j.linalg.activations.Activation;
import org.nd4j.linalg.api.ndarray.INDArray;
import org.nd4j.linalg.factory.Nd4j;
import org.nd4j.linalg.learning.config.Nesterovs;
import org.nd4j.linalg.lossfunctions.LossFunctions;

import java.util.Random;

public class LearnMath {

    public static double sigmoid(double x) {
        return 1.0 / (1.0 + Math.exp(-x));
    }

    public static void main(String[] args) {
        // Create a neural network with one input, one hidden layer, and one output layer
        MultiLayerNetwork net = new MultiLayerNetwork(new NeuralNetConfiguration.Builder()
                .seed(1234)
                .weightInit(WeightInit.XAVIER)
                .updater(new Nesterovs(0.1))
                .list()
                .layer(0, new DenseLayer.Builder().nIn(1).nOut(4).activation(Activation.RELU).build())
                .layer(1, new OutputLayer.Builder().nIn(4).nOut(1).activation(Activation.SIGMOID).lossFunction(LossFunctions.LossFunction.MSE).build())
                .build());

        // Train the network on a set of random data
        Random random = new Random(1234);
        for (int i = 0; i < 1000; i++) {
            double input = random.nextDouble();
            double target = sigmoid(input);
            INDArray inputs = Nd4j.create(new double[][]{{input}});
            INDArray outputs = Nd4j.create(new double[][]{{target}});
            net.fit(inputs, outputs);
        }

        // Test the network on a new input
        double newInput = 0.5;
        INDArray newInputs = Nd4j.create(new double[][]{{newInput}});
        INDArray output = net.output(newInputs);
        System.out.println("Output for input " + newInput + ": " + output.getDouble(0));
    }
}
```