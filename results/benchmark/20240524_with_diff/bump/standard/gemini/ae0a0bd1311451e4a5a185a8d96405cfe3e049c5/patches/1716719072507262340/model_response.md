```java
private org.hamcrest.Matcher<java.lang.String> layersAlreadyExist() {
    boolean doesLayerExist = this.image.layer().isPresent();
    String message = String.format("%s: Layer already exists", this.image.layer());
    if (doesLayerExist) {
        return new org.hamcrest.core.StringContains(false, message);
    } else {
        return new org.hamcrest.core.StringContains(true, message);
    }
}
```