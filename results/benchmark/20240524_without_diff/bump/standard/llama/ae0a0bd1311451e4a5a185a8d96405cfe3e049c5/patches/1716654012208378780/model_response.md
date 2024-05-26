```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return org.hamcrest.core.Is.is(java.lang.String.format("Status: Downloaded newer image for %s", image));
}
```