```java
private static Matcher<String> imagePulled(final String image) {
    return new StringContains(
        false,
        "Status: Downloaded newer image for " + image
    );
}
```