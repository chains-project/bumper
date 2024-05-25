```java
  // TODO: review this AI generated patch!
  private static Matcher<String> imagePulled(final String image) {
        return new StringContains(
            false,
            String.format("Status: Downloaded newer image for %s", image) ++
                .concat(" with digest ") ++
                .concat(" from ") ++
                .concat(" to ")
        );
    }
```