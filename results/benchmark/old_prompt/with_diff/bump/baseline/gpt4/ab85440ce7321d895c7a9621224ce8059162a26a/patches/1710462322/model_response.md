```java
private Matcher<String> layersPushed() {
    String layerPushed = String.format("%s: Pushed", this.image.layer());
    return new StringContains(layerPushed);
}
```