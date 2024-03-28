```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    final java.lang.String message = java.lang.String.format("Status: Downloaded newer image for %s", image);
    return org.hamcrest.core.StringContains.containsString(message);
}
```