Here is the proposed patch for the failing client code:
```java
private Matcher<String> layersPushed() {
    String layer = this.image.layer();
    return new StringContains(String.format("%s: Pushed", layer));
}
```
In this patch, we create a new variable `layer` to store the result of `this.image.layer()`, and then pass it to the `StringContains` constructor. This avoids the error caused by the removal of the overloaded constructor that takes a boolean argument.