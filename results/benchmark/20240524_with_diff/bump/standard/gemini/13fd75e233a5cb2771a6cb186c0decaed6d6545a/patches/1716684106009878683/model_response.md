```java
private org.hamcrest.Matcher<java.lang.String> layersPushed() {
    return new org.hamcrest.core.StringContains(this.image.layer(), java.lang.String.format("%s: Pushed", this.image.layer()));
}
```