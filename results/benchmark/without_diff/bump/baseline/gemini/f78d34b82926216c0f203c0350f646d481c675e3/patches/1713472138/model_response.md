```java
  import static develop.p2p.lib.LearnMath.sigmoid;

  import java.util.Random;

  public class Neuron {

    private double[] weights;
    private double bias;
    private Random random;

    public Neuron(int inputs) {
      this.weights = new double[inputs];
      this.bias = 0;
      this.random = new Random();
      for (int i = 0; i < inputs; i++) {
        weights[i] = random.nextDouble();
      }
    }

    public double calculateOutput(double[] inputs) {
      double sum = 0;
      for (int i = 0; i < inputs.length; i++) {
        sum += inputs[i] * weights[i];
      }
      sum += bias;
      return sigmoid(sum);
    }

    public void updateWeights(double[] inputs, double error) {
      for (int i = 0; i < inputs.length; i++) {
        weights[i] += error * inputs[i];
      }
      bias += error;
    }
  }
```