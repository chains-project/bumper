```java
private org.hamcrest.Matcher<java.lang.String> layersPushed() {
    String layerName = this.image.layer();
    return new org.hamcrest.core.StringContains(layerName == null, String.format("%s: Pushed", layerName));
}
```