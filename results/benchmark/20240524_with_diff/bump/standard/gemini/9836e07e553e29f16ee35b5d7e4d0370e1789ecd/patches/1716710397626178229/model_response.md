```java
private org.hamcrest.Matcher<java.lang.String> layersAlreadyExist() {
    return new org.hamcrest.core.StringContains(
            String.format("%s: Layer already exists", this.image.layer()),
            false);
}
```