```java
private org.hamcrest.Matcher<java.lang.String> layersAlreadyExist() {
    return new org.hamcrest.core.StringContains(false, java.lang.String.format("Layer %s already exists", this.image.layer()));
}
```