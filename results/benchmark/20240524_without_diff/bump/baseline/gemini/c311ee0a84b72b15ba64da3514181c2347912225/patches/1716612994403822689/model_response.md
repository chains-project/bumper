```java
  private static Matcher<String> imagePulled(final String image) {
        final Matcher<String> status = new StringContains(
            false,
            String.format("Status: Downloaded newer image for %s", image)
        );
        return new StringContains(
            false,
            status.toString()
        );
    }
```