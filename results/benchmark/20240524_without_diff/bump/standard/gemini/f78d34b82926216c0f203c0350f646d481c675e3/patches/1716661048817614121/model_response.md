```java
import develop.p2p.lib.LearnMath;
import org.deeplearning4j.nn.layers.convolution.ConvolutionLayer;
import org.deeplearning4j.nn.layers.convolution.SubsamplingLayer;
import org.deeplearning4j.nn.layers.core.DenseLayer;
import org.deeplearning4j.nn.multilayer.MultiLayerNetwork;
import org.deeplearning4j.nn.weights.WeightInit;
import org.nd4j.linalg.activations.Activation;
import org.nd4j.linalg.api.ndarray.INDArray;
import org.nd4j.linalg.factory.Nd4j;
import org.nd4j.linalg.learning.config.Nesterovs;
import org.nd4j.linalg.lossfunctions.LossFunctions;

import java.util.Random;

public class Neuron {

    private static final int SEED = 123;
    private static final int N_EPOCHS = 1000;
    private static final double LEARNING_RATE = 0.01;
    private static final Random rng = new Random(SEED);
    private static final int NUM_SAMPLES = 1000;

    public static void main(String[] args) {
        int numRows = 28;
        int numColumns = 28;
        int nChannels = 1; // Number of input channels
        int outputNum = 10; // Number of output classes
        int batchSize = 64; // Test batch size

        // Generate some sample data
        INDArray input = Nd4j.rand(batchSize, nChannels, numRows, numColumns, rng);
        INDArray labels = Nd4j.zeros(batchSize, outputNum);
        Random r = new Random(12345);
        for (int i = 0; i < batchSize; i++) {
            int idx = r.nextInt(10);
            labels.putScalar(new int[]{i, idx}, 1.0);
        }

        // Create the network
        MultiLayerNetwork net = new MultiLayerNetwork(new int[]{nChannels, numRows, numColumns}, outputNum);
        net.init();
        net.setLayerWeights(0, ConvolutionLayer.Builder.layerBuilder(0, 5, 5)
                .nIn(nChannels)
                .stride(1, 1)
                .nOut(20)
                .weightInit(WeightInit.XAVIER)
                .activation(Activation.IDENTITY)
                .build().initializer().call());
        net.setLayerWeights(1, SubsamplingLayer.Builder.layerBuilder(SubsamplingLayer.PoolingType.MAX, new int[]{2, 2})
                .stride(2, 2)
                .build().initializer().call());
        net.setLayerWeights(2, DenseLayer.Builder.layerBuilder()
                .nIn(50 * 12 * 12)
                .nOut(500)
                .weightInit(WeightInit.XAVIER)
                .activation(Activation.RELU)
                .build().initializer().call());
        net.setLayerWeights(3, DenseLayer.Builder.layerBuilder()
                .nIn(500)
                .nOut(outputNum)
                .weightInit(WeightInit.XAVIER)
                .activation(Activation.SOFTMAX)
                .build().initializer().call());
        net.setConf(new Nesterovs(LEARNING_RATE, 0.9));
        net.setLossFunction(LossFunctions.LossFunction.NEGATIVELOGLIKELIHOOD);

        // Train the network on the sample data
        for (int i = 0; i < N_EPOCHS; i++) {
            net.fit(input, labels);
        }

        // Test the network on the sample data
        INDArray output = net.output(input, false);
        System.out.println(output);
    }
}
```