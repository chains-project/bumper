Here's the fixed version of the `layersPushed` method:

```java
private Matcher<String> layersPushed() {
    String layerString = this.image.layer();
    return new StringContains(String.format("%s: Pushed", layerString));
}
```

This code creates a temporary variable `layerString` to store the result of `this.image.layer()`, and then passes it as a single argument to the `StringContains` constructor. This resolves the error caused by the updated Hamcrest library, which no longer accepts a `boolean` argument in the `StringContains` constructor.