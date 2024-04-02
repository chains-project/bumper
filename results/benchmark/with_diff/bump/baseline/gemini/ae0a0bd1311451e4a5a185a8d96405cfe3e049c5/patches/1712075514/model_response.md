```java
  private static Matcher<String> imagePulled(final String image) {
        final String msg = String.format("Status: Downloaded newer image for %s", image);
        return new StringContains(false, msg);
    }
```