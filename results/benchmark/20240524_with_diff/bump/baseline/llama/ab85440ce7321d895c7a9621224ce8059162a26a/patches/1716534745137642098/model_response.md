```java
private static Matcher<String> imagePulled(final String image) {
    return CoreMatchers.containsString(
        String.format("Status: Downloaded newer image for %s", image)
    );
}
```