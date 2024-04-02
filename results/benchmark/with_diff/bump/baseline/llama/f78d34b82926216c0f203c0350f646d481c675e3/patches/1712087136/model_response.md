```
import tokyo.peya.lib.LearnMath;
import tokyo.peya.lib.LeetConverter;
import tokyo.peya.lib.TimeParser;
import tokyo.peya.lib.WaveCreator;

public class Neuron {
    // ...

    public void input(ArrayList<Input> inputData) {
        inputData.parallelStream().forEachOrdered(input -> {
            double weightedSum = 0;
            for (int i = 0; i < input.getWeight().length; i++) {
                weightedSum += input.getWeight()[i] * input.getInput()[i];
            }
            double sigmoid = LearnMath.sigmoid(weightedSum);
            setValue(sigmoid);
        });
    }
}
```
In this patch, we've replaced the removed `sigmoid` method with the new `LearnMath.sigmoid` method. We've also added an import statement for `tokyo.peya.lib.LearnMath`.


Note that we've kept the rest of the code unchanged, as it's not affected by the changes in the library.