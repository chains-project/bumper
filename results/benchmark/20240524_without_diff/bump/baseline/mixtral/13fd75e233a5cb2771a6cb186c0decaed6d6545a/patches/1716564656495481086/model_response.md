Here is a possible patch for the given code:

```java
private static Matcher<String> imagePulled(final String image) {
    return new AbstractMatcher<String>("a string containing") {
        @Override
        public boolean matches(final Object item) {
            String string = (String) item;
            return string.contains(String.format("Status: Downloaded newer image for %s", image));
        }
    };
}
```

This patch uses an anonymous subclass of `AbstractMatcher` to create a custom matcher that checks if a string contains the specified substring. It is an alternative to the deprecated `StringContains` class.

Note: I assumed that the `StringContains` class is deprecated or removed in the new version of the library. If this is not the case, please provide more information about the library version and the error message.