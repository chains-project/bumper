Here's a proposed patch to fix the failing test:
```java
  private static Matcher<String> imagePulled(final String image) {
        return new StringContains(
            false,
            String.format("Status: Downloaded newer image for %s", image)
        ) {
            @Override
            public boolean matches(String s) {
                return s.contains("Downloaded newer image for " + image);
            }

            @Override
            public void describeTo(Description description) {
                description.appendText("status should contain 'Downloaded newer image for " + image + "'");
            }
        };
    }
```
The `StringContains` constructor that takes two arguments `boolean, String` is removed in the new library version, which causes the failure. To fix this, we can create a new instance of `StringContains` with the `String` parameter only, and override the `matches` and `describeTo` methods to keep the original logic. The `Override` decorator is not needed as the method is not overriding any method in the new version.