```java
private org.hamcrest.Matcher<java.lang.String> layersAlreadyExist() {
    boolean exists = this.image.layer().isPresent();
    String message = String.format("%s: Layer already exists", this.image.layer().get());
    return new org.hamcrest.core.StringContains(exists, message);
}
```