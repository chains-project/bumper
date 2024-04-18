Here's a possible patch for the code:
```java
private static Matcher<String> imagePulled(final String image) {
    return new CoreMatchers.containsString(
        String.format("Status: Downloaded newer image for %s", image)
    );
}
```
In this patch, we replace the `StringContains` constructor from `org.hamcrest.core` with the `containsString` method from `org.hamcrest.CoreMatchers`. This is because the `StringContains` constructor has been removed in the new version of the library, and replaced with the `containsString` method.

Note that this patch assumes that the `CoreMatchers` class is available in the new version of the library. If it is not, you may need to find an alternative way of constructing the matcher.