```java
private Matcher<String> layersPushed() {
    String expectedSubstring = String.format("%s: Pushed", this.image.layer());
    return new StringContains(expectedSubstring);
}
```