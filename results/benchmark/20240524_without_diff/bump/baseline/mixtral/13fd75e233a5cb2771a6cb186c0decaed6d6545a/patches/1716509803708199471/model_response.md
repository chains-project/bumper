Here's a possible patch for the code:

```java
private Matcher<String> layersAlreadyExist() {
    String layerName = String.format("%s: Layer already exists", this.image.layer());
    return new StringContains(layerName);
}
```

In this patch, we create a separate variable `layerName` to store the formatted string. This allows us to pass only a single argument to the `StringContains` constructor, which is now required in the updated library version.