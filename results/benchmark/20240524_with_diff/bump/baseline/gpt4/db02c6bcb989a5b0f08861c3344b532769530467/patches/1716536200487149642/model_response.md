```java
private Matcher<String> layersPushed() {
    String expectedSubString = String.format("%s: Pushed", this.image.layer());
    return new StringContains(expectedSubString);
}
```