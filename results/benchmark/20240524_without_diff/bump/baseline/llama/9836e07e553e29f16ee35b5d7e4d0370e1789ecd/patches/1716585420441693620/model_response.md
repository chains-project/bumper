```java
private static Matcher<String> imagePulled(final String image) {
    String expected = String.format("Status: Downloaded newer image for %s", image);
    return ischematches(expected);
}

private static Matcher<String> ischematches(final String expected) {
    return Matchers.containsString(expected);
}
```