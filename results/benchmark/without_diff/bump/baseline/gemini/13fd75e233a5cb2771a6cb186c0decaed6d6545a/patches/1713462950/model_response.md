```java
private static Matcher<String> imagePulled(final String image) {
    // -- StringContains(boolean, String) is removed in Hamcrest 2.2.
    // ++ StringContainsIgnoringCase(String) is added in Hamcrest 2.2.
    return StringContainsIgnoringCase.containsString(
        String.format("Status: Downloaded newer image for %s", image)
    );
}
```