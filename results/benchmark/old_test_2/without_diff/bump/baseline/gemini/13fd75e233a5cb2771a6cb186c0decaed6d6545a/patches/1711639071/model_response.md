```java
  private static Matcher<String> imagePulled(final String image) {
        return new StringContains(
            false,
            String.format("Status: Downloaded newer image for %s", image)
        )
        {
            @Override
            public boolean matches(Object item) {
                return super.matches(item.toString());
            }
        };
    }
```