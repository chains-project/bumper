```java
import develop.p2p.lib.LearnMath;

public class Neuron {

    private final double[] weights;
    private final double bias;

    public Neuron(double[] weights, double bias) {
        this.weights = weights;
        this.bias = bias;
    }

    public double activate(double[] inputs) {
        double sum = 0.0;
        for (int i = 0; i < inputs.length; i++) {
            sum += inputs[i] * weights[i];
        }
        return sigmoid(sum + bias);
    }

    public void updateWeights(double[] inputs, double error, double learningRate) {
        for (int i = 0; i < inputs.length; i++) {
            weights[i] += learningRate * error * inputs[i];
        }
        bias += learningRate * error;
    }

}
```