```java
private static Matcher<String> imagePulled(final String image) {
    String expectedString = String.format("Status: Downloaded newer image for %s", image);
    return new org.hamcrest.core.StringContains(expectedString);
}
```