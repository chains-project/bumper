```
private static Matcher<String> imagePulled(final String image) {
    String expectedString = String.format("Status: Downloaded newer image for %s", image);
    return Matchers.containsString(expectedString);
}
```