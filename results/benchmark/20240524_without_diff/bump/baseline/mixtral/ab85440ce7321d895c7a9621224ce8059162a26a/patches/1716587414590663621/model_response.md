Here is a possible patch for the failing client code:

```java
private static Matcher<String> imagePulled(final String image) {
    return new CoreMatchers.containsString(
        String.format("Status: Downloaded newer image for %s", image)
    );
}
```

In this patch, we replaced the `StringContains` class from `org.hamcrest.core` with the `containsString` method from `org.hamcrest.CoreMatchers`. This should fix the error message you provided.