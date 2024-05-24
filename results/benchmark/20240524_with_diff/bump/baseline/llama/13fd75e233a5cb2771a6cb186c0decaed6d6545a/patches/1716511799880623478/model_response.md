```java
private Matcher<String> layersPushed() {
    String contains = String.format("%s: Pushed", this.image.layer());
    return Matchers.containsString(contains);
}
```