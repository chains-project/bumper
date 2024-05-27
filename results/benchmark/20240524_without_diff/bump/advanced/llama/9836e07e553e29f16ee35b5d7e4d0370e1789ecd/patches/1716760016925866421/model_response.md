```java
private org.hamcrest.Matcher<java.lang.String> layersAlreadyExist() {
    return org.hamcrest.CoreMatchers.containsString(java.lang.String.format("%s: Layer already exists", this.image.layer()));
}
```