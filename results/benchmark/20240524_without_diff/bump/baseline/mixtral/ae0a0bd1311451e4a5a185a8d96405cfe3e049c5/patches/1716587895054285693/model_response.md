Here is a possible patch for the given code:

```java
private static Matcher<String> imagePulled(final String image) {
    return new CoreMatchers.containsString(
            String.format("Status: Downloaded newer image for %s", image)
    );
}
```

In this patch, we replace the `StringContains` constructor with the `containsString` method from the `CoreMatchers` class, which is a part of the Hamcrest library. This method performs the same functionality as the `StringContains` constructor, but it is compatible with the updated version of the Hamcrest library.

Note that the `CoreMatchers` class is marked with the `++` symbol, which indicates that it is an added library method that can be used to fix the error.

I hope this helps! Let me know if you have any questions or concerns.