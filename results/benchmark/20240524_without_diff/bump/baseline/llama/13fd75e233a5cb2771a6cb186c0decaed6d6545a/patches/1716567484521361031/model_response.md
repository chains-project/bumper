```java
private Matcher<String> layersPushed() {
    String layer = this.image.layer();
    String contains = String.format("%s: Pushed", layer);
    return Matchers.containsString(contains);
}
```