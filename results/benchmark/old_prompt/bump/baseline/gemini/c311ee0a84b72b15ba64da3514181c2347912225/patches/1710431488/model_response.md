```java
  private static Matcher<String> imagePulled(final String image) {
        String expected = String.format("Status: Downloaded newer image for %s", image);
        return new StringContains(
            false,
            expected
        );
    }
```