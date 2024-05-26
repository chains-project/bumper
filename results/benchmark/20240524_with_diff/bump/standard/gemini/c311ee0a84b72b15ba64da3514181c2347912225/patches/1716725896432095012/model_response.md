```java
private org.hamcrest.Matcher<java.lang.String> layersPushed() {
    String layer = this.image.layer();
    // ++
    if (layer == null) {
        throw new org.junit.ComparisonFailure("Image does not contain layers", layer, null);
    }
    // ++
    return new org.hamcrest.core.StringContains(false, String.format("%s: Pushed", layer));
}
```