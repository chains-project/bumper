```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    final String expected = java.lang.String.format("Status: Downloaded newer image for %s", image);
    return new org.hamcrest.core.StringContains(false, expected);
}
```