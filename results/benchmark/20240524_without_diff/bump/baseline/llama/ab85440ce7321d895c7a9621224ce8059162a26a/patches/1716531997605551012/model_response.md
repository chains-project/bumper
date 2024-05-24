```java
private static Matcher<String> imagePulled(final String image) {
    return containsString(String.format("Status: Downloaded newer image for %s", image));
}
```