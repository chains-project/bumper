```java
private org.hamcrest.Matcher<java.lang.String> layersPushed() {
    return new org.hamcrest.core.StringContains(false, java.lang.String.format("%s: Pushed", this.image.layer()));
}
```