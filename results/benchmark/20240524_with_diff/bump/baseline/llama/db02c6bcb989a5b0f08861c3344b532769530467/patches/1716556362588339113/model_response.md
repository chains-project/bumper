```java
private Matcher<String> layersPushed() {
    String containsString = String.format("%s: Pushed", this.image.layer());
    return Matchers.containsString(containsString);
}
```