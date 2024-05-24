```java
private static Matcher<String> imagePulled(final String image) {
    final String expectedMessage = String.format("Status: Downloaded newer image for %s", image);
    return new StringContains(expectedMessage);
}
```