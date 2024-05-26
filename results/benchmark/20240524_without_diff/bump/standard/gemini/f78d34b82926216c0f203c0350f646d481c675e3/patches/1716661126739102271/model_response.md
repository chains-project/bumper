```java
import static org.apache.commons.math3.special.Erf.erf;

public class Neuron {

    private double[] weights;
    private double bias;

    public Neuron(int numInputs) {
        weights = new double[numInputs];
        for (int i = 0; i < numInputs; i++) {
            weights[i] = Math.random();
        }
        bias = Math.random();
    }

    public double calculateOutput(double[] inputs) {
        double sum = 0;
        for (int i = 0; i < inputs.length; i++) {
            sum += weights[i] * inputs[i];
        }
        sum += bias;
        return sigmoid(sum);
    }

    private double sigmoid(double x) {
        return 1 / (1 + Math.exp(-x));
    }
}
```