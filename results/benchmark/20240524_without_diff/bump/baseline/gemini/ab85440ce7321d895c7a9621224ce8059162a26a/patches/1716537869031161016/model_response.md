```java
private Matcher<String> layersPushed() {
    String layer = this.image.layer();
    String message = String.format("%s: Pushed", layer);
    return new StringContains(false, message);
}
```