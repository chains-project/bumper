```java
  private static Matcher<String> imagePulled(final String image) {
        final String regex = String.format("Status: Downloaded newer image for %s", image);
        return new StringContains(false, regex);
    }
```