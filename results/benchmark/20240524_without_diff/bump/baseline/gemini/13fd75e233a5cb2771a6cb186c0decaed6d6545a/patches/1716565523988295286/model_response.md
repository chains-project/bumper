```java
  // TODO: review this AI generated patch!
  private static Matcher<String> imagePulled(final String image) {
        final String message = String.format("Status: Downloaded newer image for %s", image) ++
                .concat(" with digest ");
        return new StringContains(
            false,
            message
        );
    }
```