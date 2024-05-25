Here's a potential patch for the failing client code:

```java
private static Matcher<String> imagePulled(final String image) {
    return new CoreMatchers.<String>containsString(
        String.format("Status: Downloaded newer image for %s", image)
    );
}
```

This patch replaces the `StringContains` constructor with the `containsString` method from the `CoreMatchers` class, which is an added library method identified with `++`. The `CoreMatchers` class is a part of the Hamcrest library, which is a dependency of the Artipie project, and it provides a convenient way to create matchers for various types of objects. The `containsString` method checks if the given string contains the specified substring, which is what the original code was trying to do with the `StringContains` constructor.