```java
private Matcher<String> layersPushed() {
    String layer = this.image.layer();
    String expected = String.format("%s: Pushed", layer);
    return Matchers.containsString(expected);
}
```