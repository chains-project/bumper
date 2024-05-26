```java
private org.hamcrest.Matcher<java.lang.String> layersAlreadyExist() {
    String message = String.format("%s: Layer already exists", this.image.layer());
    return new org.hamcrest.core.StringContains(false, message);
}
```