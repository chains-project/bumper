Here is a potential patch for the failing code:

```java
private static Matcher<String> imagePulled(final String image) {
    return new CoreMatchers.containsString(
        String.format("Status: Downloaded newer image for %s", image)
    );
}
```

This patch replaces the `StringContains` constructor with a call to the `containsString` method from the `CoreMatchers` class. This method is a replacement for the deprecated `StringContains` constructor and should work in a similar way.

Note that the `CoreMatchers` class is part of the Hamcrest library, which is a dependency of the code you provided. It is likely that this class was added in a newer version of the library, which is why the original code is failing.

I hope this helps! Let me know if you have any questions.