```java
  private static Matcher<String> imagePulled(final String image) {
        final String contains = String.format("Status: Downloaded newer image for %s", image);
        return new StringContains(false, contains);
    }
```