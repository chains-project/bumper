Here is a possible patch for the failing code:

```java
private static Matcher<String> imagePulled(final String image) {
    return new CoreMatchers.containsString(
        String.format("Status: Downloaded newer image for %s", image)
    );
}
```

In this patch, we replaced the `StringContains` class from the `org.hamcrest.core` package with the `containsString` method from the `CoreMatchers` class in the same package. This is because the `StringContains` constructor is no longer available in the version of Hamcrest that you are using. The `CoreMatchers.containsString` method serves the same purpose and can be used as a drop-in replacement.