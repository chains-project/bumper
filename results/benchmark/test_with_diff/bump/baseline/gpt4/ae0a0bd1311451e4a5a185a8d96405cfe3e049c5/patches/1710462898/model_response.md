```java
private Matcher<String> layersPushed() {
    String expectedString = String.format("%s: Pushed", this.image.layer());
    return new StringContains(expectedString);
}
```