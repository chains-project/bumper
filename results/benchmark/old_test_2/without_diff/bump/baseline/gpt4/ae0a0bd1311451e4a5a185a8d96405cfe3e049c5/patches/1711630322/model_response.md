```java
private Matcher<String> layersPushed() {
    return new org.hamcrest.core.StringContains(String.format("%s: Pushed", this.image.layer()));
}
```