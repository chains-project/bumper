```java
private Matcher<String> layersPushed() {
    String layerPushed = String.format("%s: Pushed", this.image.layer());
    return CoreMatchers.containsString(layerPushed);
}
```