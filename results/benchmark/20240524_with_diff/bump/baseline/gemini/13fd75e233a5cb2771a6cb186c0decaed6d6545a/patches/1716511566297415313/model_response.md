```java
  private Matcher<String> layersPushed() {
    String expectedMessage = String.format("%s: Pushed", this.image.layer());
    return new StringContains(false, expectedMessage);
}
```