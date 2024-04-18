```
    public void input(ArrayList<Input> inputData)
    {
        inputData.parallelStream().forEachOrdered(input -> input(input.getWeightingValue()));
        setValue(tokyo.peya.lib.LearnMath.sigmoid(sum));
    }
```

Explanation:

The error message indicates that the method `sigmoid` from the `develop.p2p.lib.LearnMath` class is not found. This method has been removed in the new library version, and instead, the `tokyo.peya.lib.LearnMath` class provides a `sigmoid` method. Therefore, we need to update the code to use the new `sigmoid` method.

The proposed patch replaces the line `setValue(sigmoid(sum));` with `setValue(tokyo.peya.lib.LearnMath.sigmoid(sum));`. This change imports the new `sigmoid` method from the `tokyo.peya.lib.LearnMath` class and uses it instead of the removed method.

The rest of the code remains unchanged, as it does not depend on the removed methods.