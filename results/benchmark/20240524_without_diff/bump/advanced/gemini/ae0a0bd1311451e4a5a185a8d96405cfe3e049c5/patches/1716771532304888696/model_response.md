```java
private org.hamcrest.Matcher<java.lang.String> layersAlreadyExist() {
    String expectedMessage = String.format("%s: Layer already exists", this.image.layer());
    return new org.hamcrest.core.StringContains(expectedMessage);
}
```