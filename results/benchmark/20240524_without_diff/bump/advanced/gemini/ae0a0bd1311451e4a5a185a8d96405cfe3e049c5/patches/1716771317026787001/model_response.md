```java
private org.hamcrest.Matcher<java.lang.String> layersPushed() {
    final String layer = this.image.layer();
    return new org.hamcrest.core.StringContains(false, String.format("%s: Pushed", layer));
}
```