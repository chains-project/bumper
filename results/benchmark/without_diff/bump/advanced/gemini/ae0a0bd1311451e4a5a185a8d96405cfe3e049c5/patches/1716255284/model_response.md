```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return new org.hamcrest.core.StringContains(false, java.lang.String.format("Status: Image is up to date for %s", image));
}
```