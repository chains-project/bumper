```java
import org.nd4j.linalg.activations.Activation;
import org.nd4j.linalg.api.ndarray.INDArray;

public class Neuron {

    private double[] weights;
    private double bias;

    public Neuron(int numInputs) {
        this.weights = new double[numInputs];
        this.bias = 0;
    }

    public double output(double[] inputs) {
        double sum = 0;
        for (int i = 0; i < inputs.length; i++) {
            sum += inputs[i] * weights[i];
        }
        sum += bias;
        return Activation.SIGMOID.getActivationFunction().f(sum);
    }

    public void updateWeights(double[] inputs, double error, double learningRate) {
        for (int i = 0; i < inputs.length; i++) {
            weights[i] += learningRate * error * inputs[i];
        }
        bias += learningRate * error;
    }
}
```