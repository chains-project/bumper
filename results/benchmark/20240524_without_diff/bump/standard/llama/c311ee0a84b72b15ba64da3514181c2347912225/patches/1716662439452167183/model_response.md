```java
private org.hamcrest.Matcher<java.lang.String> layersAlreadyExist() {
    org.hamcrest.core.StringContains contains = org.hamcrest.core.StringContains.containsString(java.lang.String.format("%s: Layer already exists", this.image.layer()));
    return contains;
}
```