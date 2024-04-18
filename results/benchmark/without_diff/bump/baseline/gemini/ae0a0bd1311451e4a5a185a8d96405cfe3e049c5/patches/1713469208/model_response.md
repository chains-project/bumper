```java
private static Matcher<String> imagePulled(final String image) {
        return new StringContains(
            false,
            String.format("Status: Image is up to date for %s", image)
        );
    }
```