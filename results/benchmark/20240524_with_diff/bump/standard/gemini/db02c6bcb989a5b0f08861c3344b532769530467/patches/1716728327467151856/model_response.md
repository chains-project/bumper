```java
private org.hamcrest.Matcher<java.lang.String> layersPushed() {
    String layer = this.image.layer();
    return new org.hamcrest.core.StringContains(false, java.lang.String.format("%s: Pushed", layer));
}
```