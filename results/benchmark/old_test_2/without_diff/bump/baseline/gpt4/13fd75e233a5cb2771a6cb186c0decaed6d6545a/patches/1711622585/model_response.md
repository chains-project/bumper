```java
private static Matcher<String> imagePulled(final String image) {
    return new org.hamcrest.core.StringContains(
        String.format("Status: Downloaded newer image for %s", image)
    );
}
```