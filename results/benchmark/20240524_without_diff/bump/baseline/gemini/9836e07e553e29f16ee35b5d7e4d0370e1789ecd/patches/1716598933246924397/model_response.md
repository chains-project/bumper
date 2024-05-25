```java
  private static Matcher<String> imagePulled(final String image) {
        final String expectedLog = String.format("Status: Downloaded newer image for %s", image);
        return new StringContains(
            false,
            expectedLog
        );
    }
```