Based on the error message, it seems that the `StringContains` constructor now requires a single `String` argument, instead of a `boolean` and a `String`. Here's a possible fix for the client code:
```java
private Matcher<String> layersAlreadyExist() {
    String message = String.format("Layer already exists: %s", this.image.layer());
    return new StringContains(message);
}
```
In this fix, we create a new `String` variable `message` that contains the formatted error message. Then, we pass this `message` variable to the `StringContains` constructor. This should fix the error, as it now matches the updated constructor signature.