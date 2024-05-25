```java
private Matcher<String> layersPushed() {
    String layer = this.image.layer();
    String pattern = String.format("%s: Pushed", layer);
    return Matchers.containsString(pattern);
}
```