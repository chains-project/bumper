Here is a possible patch for the failing code:

```java
private static Matcher<String> imagePulled(final String image) {
    return new CoreMatchers.containsString(
            String.format("Status: Downloaded newer image for %s", image)
    );
}
```

In this patch, we replaced the `StringContains` constructor from the `org.hamcrest.core` package with the `containsString` method from the `org.hamcrest.CoreMatchers` class. This is because the `StringContains` constructor is no longer available in the version of Hamcrest that you are using. The `containsString` method serves the same purpose, so the code should work as expected.