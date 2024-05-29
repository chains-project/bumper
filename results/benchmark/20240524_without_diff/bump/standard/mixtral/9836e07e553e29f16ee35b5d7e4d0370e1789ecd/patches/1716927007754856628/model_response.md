Here is a possible patch for the failing client code:
```java
private org.hamcrest.Matcher<java.lang.String> layersAlreadyExist() {
    return new org.hamcrest.core.IsEqual(
        java.lang.String.format("%s: Layer already exists", this.image.layer())
    );
}
```
This patch uses the `IsEqual` matcher from Hamcrest, which takes a single argument of type `T` and checks if the actual value is equal to the expected value. In this case, the expected value is the formatted string indicating that the layer already exists.

Note that the `StringContains` matcher is not suitable for this use case, because it expects a boolean argument followed by a string argument. Instead, we can use the `IsEqual` matcher to check if the actual value is equal to the expected value.