```java
private static Matcher<String> imagePulled(final String image) {
    return ischematches(String.format("Status: Downloaded newer image for %s", image));
}
```