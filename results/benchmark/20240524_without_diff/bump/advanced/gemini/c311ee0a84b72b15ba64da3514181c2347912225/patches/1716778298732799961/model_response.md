```java
private org.hamcrest.Matcher<java.lang.String> layersAlreadyExist() {
    return new org.hamcrest.core.StringContains(this.image.layer(), java.lang.String.format("%s: Layer already exists", false));
}
```