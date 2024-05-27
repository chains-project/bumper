```java
import develop.p2p.lib.LearnMath;

public class Neuron {
	private double[] weights;
	private double bias;
	private double learningRate;

	public Neuron(int numInputs) {
		this.weights = new double[numInputs];
		this.bias = 0;
		this.learningRate = 0.1;
	}

	public double activate(double[] inputs) {
		double sum = 0;
		for (int i = 0; i < inputs.length; i++) {
			sum += inputs[i] * weights[i];
		}
		sum += bias;
		return sigmoid(sum);
	}

	public void train(double[] inputs, double target) {
		double output = activate(inputs);
		double error = target - output;
		for (int i = 0; i < inputs.length; i++) {
			weights[i] += learningRate * error * inputs[i];
		}
		bias += learningRate * error;
	}
}
```