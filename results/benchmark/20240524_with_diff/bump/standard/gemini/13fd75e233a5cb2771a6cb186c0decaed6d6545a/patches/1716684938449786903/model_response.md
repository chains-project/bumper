```java
private org.hamcrest.Matcher<java.lang.String> layersPushed() {
    String layer = this.image.layer();
    String message = String.format("%s: Pushed", layer);
    return new org.hamcrest.core.StringContains(false, message);
}
```