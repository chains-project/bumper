```java
private Matcher<String> layersPushed() {
    String expected = String.format("%s: Pushed", this.image.layer());
    return Matchers.containsString(expected);
}
```