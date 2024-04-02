```java
  private static Matcher<String> imagePulled(final String image) {
        final String format = "Status: Downloaded newer image for %s";
        return new StringContains(
            false,
            String.format(format, image)
        );
    }
```