```java
  private static Matcher<String> imagePulled(final String image) {
        // variable to store the expected message
        final String expectedMessage = String.format("Status: Downloaded newer image for %s", image);
        // return a matcher that checks if the string contains the expected message
        return new StringContains(false, expectedMessage);
    }
```