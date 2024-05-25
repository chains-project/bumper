```java
  // TODO: review this AI generated patch!
  private static Matcher<String> imagePulled(final String image) {
        final Matcher<String> downloadedNewerImage = new StringContains(
            false,
            String.format("Status: Downloaded newer image for %s", image)
        );
        final Matcher<String> downloaded = new StringContains(false, "Downloaded");
        return downloadedNewerImage.and(downloaded);
    }
```