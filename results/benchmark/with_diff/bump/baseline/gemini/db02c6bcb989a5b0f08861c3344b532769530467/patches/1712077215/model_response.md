```java
  private static Matcher<String> imagePulled(final String image) {
        final boolean negative = false;
        final String message = String.format("Status: Downloaded newer image for %s", image);
        return new StringContains(negative, message);
    }
```