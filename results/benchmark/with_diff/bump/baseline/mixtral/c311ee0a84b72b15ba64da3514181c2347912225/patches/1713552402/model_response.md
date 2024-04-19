Here's a possible patch for the given code:

```java
private Matcher<String> layersPushed() {
    String layer = this.image.layer();
    return new StringContains(String.format("%s: Pushed", layer));
}
```

In this patch, we create a temporary variable `layer` to store the result of `this.image.layer()`, and pass it directly to the `StringContains` constructor. This avoids the issue of passing a boolean value to the constructor.