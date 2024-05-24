```java
private Matcher<String> layersPushed() {
    String layer = this.image.layer();
    return Matchers.containsString(layer + ": Pushed");
}
```