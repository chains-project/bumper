Here is a possible patch for the failing code:

```java
private Matcher<String> layersAlreadyExist() {
    String layer = this.image.layer();
    return new StringContains(String.format("Layer already exists: %s", layer));
}
```

This patch creates a new variable `layer` to store the result of `this.image.layer()`, and then uses this variable to construct the `StringContains` matcher. This avoids the need to pass a boolean argument to the `StringContains` constructor, which was causing the error.

Note that this patch assumes that the `StringContains` constructor with a single `String` argument is still available in the new version of the library. If this constructor has been removed, you may need to use a different matcher or a different approach to solve the error.