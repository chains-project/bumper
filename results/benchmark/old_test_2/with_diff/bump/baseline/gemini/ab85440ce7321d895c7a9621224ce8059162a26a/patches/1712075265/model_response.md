```java
  private static Matcher<String> imagePulled(final String image) {
        String status = String.format("Status: Downloaded newer image for %s", image);
        return new StringContains(false, status);
    }
```