```java
private org.hamcrest.Matcher<java.lang.String> layersPushed() {
    return new org.hamcrest.core.StringContains(false, String.format("%s: Pushed", this.image.layer()));
}
```