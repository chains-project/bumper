```java
  private static Matcher<String> imagePulled(final String image) {
    // Create a new matcher that checks if the string contains the expected substring.
    final Matcher<String> matcher = new StringContains(
        false,
        String.format("Status: Downloaded newer image for %s", image)
    );
    // Return the created matcher.
    return matcher;
  }
```