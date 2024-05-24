Here's a possible patch for the failing code:

```java
private Matcher<String> layersPushed() {
    String layer = this.image.layer();
    return new StringContains(String.format("%s: Pushed", layer));
}
```

In this patch, we create a new variable `layer` to store the result of `this.image.layer()`, and then pass it as a single argument to the `StringContains` constructor. This should fix the error caused by the updated library version, which no longer accepts a `boolean` argument in the constructor.