```java
private Matcher<String> layersPushed() {
    return org.hamcrest.core.StringContains.containsString(String.format("%s: Pushed", this.image.layer()));
}
```