```java
private org.hamcrest.Matcher<java.lang.String> layersAlreadyExist() {
    String layerName = this.image.layer();
    return new org.hamcrest.core.StringContains(false, java.lang.String.format("%s: Layer already exists", layerName));
}
```