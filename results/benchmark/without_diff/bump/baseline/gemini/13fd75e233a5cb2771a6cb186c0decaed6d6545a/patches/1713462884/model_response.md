```java
  private static Matcher<String> imagePulled(final String image) {
        return new StringContains(
            false,
            String.format("Pulled image: %s", image)
        );
    }
```