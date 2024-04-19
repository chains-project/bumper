Here's the fixed version of the `layersAlreadyExist` method:

```java
private Matcher<String> layersAlreadyExist() {
    String message = String.format("%s: Layer already exists", this.image.layer());
    return new StringContains(message);
}
```

The issue was caused by passing two arguments to the `StringContains` constructor, while it expects only one. I've stored the formatted string in a separate variable and passed it as a single argument to the constructor.