```
public void input(ArrayList<Input> inputData) {
    inputData.parallelStream().forEachOrdered(input -> {
        double sum = 0;
        for (int i = 0; i < input.getWeightingValue().length; i++) {
            sum += input.getWeightingValue()[i] * input.getInput()[i];
        }
        setValue(tokyo.peya.lib.LearnMath.sigmoid(sum));
    });
}
```
This patch fixes the error by replacing `sigmoid` with `tokyo.peya.lib.LearnMath.sigmoid`, which is the updated version of the method in the new library version.

The `tokyo.peya.lib.LearnMath.sigmoid` method is a static method that takes a double argument and returns its sigmoid value. It is imported from the updated library version, which includes the changes mentioned in the question.

The rest of the code remains the same, as it does not depend on the removed methods.