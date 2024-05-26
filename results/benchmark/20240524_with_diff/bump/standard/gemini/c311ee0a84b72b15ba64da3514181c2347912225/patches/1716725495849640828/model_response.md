```java
private org.hamcrest.Matcher<java.lang.String> layersAlreadyExist() {
    return new org.hamcrest.core.StringContains(
            java.lang.String.format("%s: Layer already exists", this.image.layer())
    );
}
```