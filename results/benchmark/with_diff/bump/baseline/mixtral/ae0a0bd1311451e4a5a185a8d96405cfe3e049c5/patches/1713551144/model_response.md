Here's a possible patch for the failing code:

```java
private Matcher<String> layersPushed() {
    String layer = this.image.layer();
    return new StringContains(String.format("%s: Pushed", layer));
}
```

In this patch, I created a new variable `layer` to store the result of `this.image.layer()`, and then passed it as an argument to the `StringContains` constructor. This way, the code only uses the `StringContains` constructor that takes a single `String` argument, which matches the updated library version.