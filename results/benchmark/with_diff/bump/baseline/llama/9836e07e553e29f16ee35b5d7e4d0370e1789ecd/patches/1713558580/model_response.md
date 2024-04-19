Here's a proposed patch to fix the failing test:
```java
  private static Matcher<String> imagePulled(final String image) {
        return new StringContains(
            false,
            String.format("Status: Downloaded newer image for %s", image)
        ) {
            @Override
            public boolean matches(String s) {
                return s.contains("Status: Downloaded newer image for " + image);
            }

            @Override
            public void describeMismatchSafely(String s, Description description) {
                description.appendText("was not pulled");
            }

            @Override
            public void describeTo(Description description) {
                description.appendText("pulling image " + image);
            }
        };
    }
```
The `StringContains` constructor with a single `String` argument is removed in the new version of the library, so we need to use the alternative constructor that takes a `boolean` and a `String` argument. We also need to implement the `Matcher` interface methods to make the patch compatible with the new version.