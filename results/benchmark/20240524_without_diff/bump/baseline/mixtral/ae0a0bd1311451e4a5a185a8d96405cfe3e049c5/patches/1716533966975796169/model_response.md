Here's a possible patch for the failing code:

```java
private Matcher<String> layersAlreadyExist() {
    String layer = this.image.layer();
    return new StringContains(String.format("%s: Layer already exists", layer));
}
```

In this patch, I created a new variable `layer` to store the result of `this.image.layer()`, and then passed it to the `StringContains` constructor. This way, the constructor only receives one argument, as required by the updated library version.