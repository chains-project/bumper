```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return org.hamcrest.CoreMatchers.containsString(java.lang.String.format("Status: Downloaded newer image for %s", image));
}
```