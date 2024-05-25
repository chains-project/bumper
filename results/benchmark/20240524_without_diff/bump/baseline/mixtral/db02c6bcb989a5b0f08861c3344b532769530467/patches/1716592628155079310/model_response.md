Here is a possible patch for the given code:

```java
private static Matcher<String> imagePulled(final String image) {
    return new CoreMatchers.containsString(
        String.format("Status: Downloaded newer image for %s", image)
    );
}
```

This patch replaces the `StringContains` constructor with the `containsString` method from the `CoreMatchers` class, which is a part of the Hamcrest library. This method has the same behavior as the `StringContains` constructor and can be used as a drop-in replacement.

Note that this patch assumes that the Hamcrest library has been updated to a version that includes the `CoreMatchers` class. If this is not the case, you may need to update the Hamcrest dependency in your project.