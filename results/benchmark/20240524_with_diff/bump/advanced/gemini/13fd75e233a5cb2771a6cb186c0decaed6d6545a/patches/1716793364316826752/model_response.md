```java
private org.hamcrest.Matcher<java.lang.String> layersAlreadyExist() {
    boolean exist = this.image.layer().isPresent();
    String message = String.format("%s: Layer already exists", this.image.layer());
    return new org.hamcrest.core.StringContains(exist, message);
}
```