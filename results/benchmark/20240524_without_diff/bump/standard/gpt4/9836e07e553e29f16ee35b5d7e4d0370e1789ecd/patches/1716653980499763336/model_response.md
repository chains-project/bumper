```java
private org.hamcrest.Matcher<java.lang.String> layersAlreadyExist() {
    return org.hamcrest.core.StringContains.containsString(java.lang.String.format("%s: Layer already exists", this.image.layer()));
}
```