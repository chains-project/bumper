```java
private Matcher<String> layersPushed() {
    String layerName = String.format("%s: Pushed", this.image.layer());
    return Matchers.containsString(layerName);
}
```