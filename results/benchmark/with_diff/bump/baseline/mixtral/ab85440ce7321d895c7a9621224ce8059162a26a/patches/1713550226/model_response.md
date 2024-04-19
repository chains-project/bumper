Here's the fixed version of the `layersPushed` method:

```java
private Matcher<String> layersPushed() {
    String layerString = this.image.layer();
    return new StringContains(String.format("%s: Pushed", layerString));
}
```

The issue in the original code was passing `false` as the first argument to the `StringContains` constructor, which was not expected by the new version of the library. I removed the `false` argument and stored the `layer()` value in a separate variable for better readability.