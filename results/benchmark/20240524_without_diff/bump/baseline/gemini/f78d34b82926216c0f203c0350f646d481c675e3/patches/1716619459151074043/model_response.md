```java
import static org.apache.commons.math3.util.FastMath.max;
import static org.apache.commons.math3.util.FastMath.min;

  public class Neuron {
    private double[] weights;
    private double bias;

    public Neuron(int inputSize) {
      weights = new double[inputSize];
      bias = 0;
    }

    public double sigmoid(double x) {
      return 1 / (1 + Math.exp(-x));
    }

    public double activate(double[] inputs) {
      double sum = 0;
      for (int i = 0; i < inputs.length; i++) {
        sum += inputs[i] * weights[i];
      }
      sum += bias;
      return sigmoid(sum);
    }

    public void train(double[] inputs, double target, double learningRate) {
      double output = activate(inputs);
      double error = target - output;
      for (int i = 0; i < inputs.length; i++) {
        weights[i] += learningRate * error * inputs[i];
      }
      bias += learningRate * error;
    }
  }
```