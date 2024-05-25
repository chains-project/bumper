```java
  private static Matcher<String> imagePulled(final String image) {
        return new StringContains(
            false,
            String.format("status: Downloaded newer image for %s", image)
        );
    }
```