```java
  private static Matcher<String> imagePulled(final String image) {
        return new StringEndsWith(
            false,
            String.format("Status: Downloaded newer image for %s", image)
        );
    }
```