```java
private static Matcher<String> imagePulled(final String image) {
    String message = String.format("Status: Downloaded newer image for %s", image);
    return new StringContains(false, message.substring(message.indexOf(":") + 2));
}
```