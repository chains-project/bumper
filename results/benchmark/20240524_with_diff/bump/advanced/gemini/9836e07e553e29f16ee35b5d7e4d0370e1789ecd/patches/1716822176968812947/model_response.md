```java
private org.hamcrest.Matcher<java.lang.String> layersAlreadyExist() {
    return new org.hamcrest.core.StringContains(String.valueOf(this.image.layer()), false);
}
```