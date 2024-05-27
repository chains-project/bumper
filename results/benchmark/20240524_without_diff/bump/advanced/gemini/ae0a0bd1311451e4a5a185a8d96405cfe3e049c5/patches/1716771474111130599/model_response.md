```java
private org.hamcrest.Matcher<java.lang.String> layersAlreadyExist() {
    return new org.hamcrest.core.StringContains(this.image.layer(), false);
}
```