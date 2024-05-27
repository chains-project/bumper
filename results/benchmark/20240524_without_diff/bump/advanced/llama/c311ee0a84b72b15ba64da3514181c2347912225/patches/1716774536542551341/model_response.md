```java
private org.hamcrest.Matcher<java.lang.String> layersAlreadyExist() {
    java.lang.String message = java.lang.String.format("%s: Layer already exists", this.image.layer());
    return org.hamcrest.CoreMatchers.containsString(message);
}
```