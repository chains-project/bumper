```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    final boolean ignoreCase = false;
    return new org.hamcrest.core.StringContains(ignoreCase, java.lang.String.format("Status: Downloaded newer image for %s", image));
}
```