```java
  private static Matcher<String> imagePulled(final String image) {
        final String format = String.format("Status: Downloaded newer image for %s", image);
        return new StringContains(
            false,
            format
        );
    }
```