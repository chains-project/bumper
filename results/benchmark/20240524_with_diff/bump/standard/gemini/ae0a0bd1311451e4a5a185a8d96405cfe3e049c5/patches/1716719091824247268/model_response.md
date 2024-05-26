```java
private org.hamcrest.Matcher<java.lang.String> layersAlreadyExist() {
    String layer = this.image.layer();
    return new org.hamcrest.core.StringContains(false, String.format("%s: Layer already exists", layer));
}
```