```java
  private static Matcher<String> imagePulled(final String image) {
        final String expectedLogMessage =
            String.format("Status: Downloaded newer image for %s", image);
        return new StringContains(expectedLogMessage);
    }
```