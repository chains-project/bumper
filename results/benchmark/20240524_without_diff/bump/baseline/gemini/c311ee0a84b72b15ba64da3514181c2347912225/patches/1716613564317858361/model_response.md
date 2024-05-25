```java
  // TODO: review this AI generated patch!
  private static Matcher<String> imagePulled(final String image) {
    final String successMessage = String.format("Status: Downloaded newer image for %s", image);
    final String downloadMessage = "Downloaded";
    return new StringContains(false, successMessage)
        .and(new StringContains(false, downloadMessage));
  }
```