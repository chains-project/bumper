```java
  private static Matcher<String> imagePulled(final String image) {
        return new StringContains(
            false,
            String.format("Status: Downloaded newer image for %s", image)
        ) {
            @Override
            protected boolean matchesSafely(String item) {
                return item.contains(getSubstring());
            }
        };
    }
```