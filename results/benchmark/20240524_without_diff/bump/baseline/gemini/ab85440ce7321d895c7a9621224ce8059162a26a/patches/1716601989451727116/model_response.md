```java
 private static Matcher<String> imagePulled(final String image) {
        return new StringContains(
            String.format("Status: Downloaded newer image for %s", image)
        );
    }
```