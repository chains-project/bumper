Here is a possible patch for the code:

```java
private static Matcher<String> imagePulled(final String image) {
    return new CoreMatchers.containsString(
        String.format("Status: Downloaded newer image for %s", image)
    );
}
```

This patch replaces the `StringContains` constructor with the `containsString` method from the `CoreMatchers` class, which is part of the Hamcrest library. This method has the same functionality as the `StringContains` constructor, but it takes a `String` argument instead of a `boolean` and a `String`. This should fix the error message you provided.