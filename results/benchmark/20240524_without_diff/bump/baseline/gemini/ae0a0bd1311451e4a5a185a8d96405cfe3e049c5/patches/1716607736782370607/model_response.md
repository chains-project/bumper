```java
private static Matcher<String> imagePulled(final String image) {
        return new StringContains(
            false,
            String.format("Downloaded newer image for %s", image)
        );
    }
```