```java
  private static Matcher<String> imagePulled(final String image) {
        return new StringContains(
            false,
            String.format("Status: Pulled newer image for %s", image)
        );
    }
```