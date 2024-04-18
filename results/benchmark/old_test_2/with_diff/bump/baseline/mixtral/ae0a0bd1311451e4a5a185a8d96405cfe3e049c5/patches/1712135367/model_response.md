Based on the error message and the library changes, it seems that the `StringContains` constructor's signature has changed, and now it only accepts a single `String` argument, instead of a `boolean` and a `String`.

Here's a possible patch for the failing code:
```java
private Matcher<String> layersPushed() {
    String layer = this.image.layer();
    return new StringContains(String.format("%s: Pushed", layer));
}
```
In this patch, we first extract the layer value to a separate variable, and then we construct the `StringContains` matcher using only the formatted string, without the `false` argument. This should fix the compilation error.