```java
private Matcher<String> layersPushed() {
    String formattedString = String.format("%s: Pushed", this.image.layer());
    return new StringContains(formattedString);
}
```