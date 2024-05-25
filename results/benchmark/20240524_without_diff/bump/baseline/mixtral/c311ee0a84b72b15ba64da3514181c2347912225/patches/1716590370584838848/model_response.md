Here is a fixed version of the method using a different Hamcrest matcher:

```java
private static Matcher<String> imagePulled(final String image) {
    return new StringMatcher("Status: Downloaded newer image for " + image) {
        @Override
        protected boolean match(String actual) {
            return actual.contains(this.string);
        }
    };
}
```

This version uses the `StringMatcher` class instead of `StringContains`, and overrides the `match` method to check if the actual string contains the expected substring.

Note: I am assuming that the `StringMatcher` class is available in the project, as it is not part of the standard Java library but is included in some testing frameworks. If it is not available, you may need to find a different way to implement the matcher or add a dependency on a library that includes it.