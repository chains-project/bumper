```java
private org.hamcrest.Matcher<java.lang.String> layersAlreadyExist() {
    String format = "%s: Layer already exists";
    Object[] args = new Object[]{this.image.layer()};
    return new org.hamcrest.core.StringContains(false, String.format(format, args));
}
```