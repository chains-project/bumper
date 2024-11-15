```java
import org.deeplearning4j.nn.api.Layer;
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

public class Neuron {

    public static void main(String[] args) {
        int numInputs = 3;
        int numOutputs = 1;
        int seed = 123;

        // Create the network
        MultiLayerNetwork network = new MultiLayerNetwork(new NeuralNetConfiguration.Builder()
                .seed(seed)
                .weightInit(WeightInit.XAVIER)
                .updater(new Nesterovs(0.1))
                .list()
                .layer(0, new DenseLayer.Builder().nIn(numInputs).nOut(2).activation(Activation.SIGMOID).build())
                .layer(1, new OutputLayer.Builder(LossFunctions.LossFunction.MSE).activation(Activation.IDENTITY).nIn(2).nOut(numOutputs).build())
                .build());
        network.init();

        // Generate some training data
        INDArray input = Nd4j.rand(10, numInputs);
        INDArray labels = Nd4j.zeros(10, numOutputs);

        // Train the network
        for (int i = 0; i < 1000; i++) {
            network.fit(input, labels);
        }

        // Test the network
        INDArray output = network.output(input);
        System.out.println(output);
    }
}
```