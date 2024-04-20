Here is the patch for the given code:

```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return new org.hamcrest.Matcher<java.lang.String>() {
        @Override
        public boolean matches(final java.lang.String actual) {
            return actual.contains(String.format("Status: Downloaded newer image for %s", image));
        }

        @Override
        public void describeTo(final org.hamcrest.Description description) {
            description.appendText("a string containing: Status: Downloaded newer image for ").appendValue(image);
        }
    };
}
```

This code creates an anonymous subclass of `org.hamcrest.Matcher` that overrides its `matches` and `describeTo` methods. This allows you to define custom matcher behavior while still using the `Matcher` interface. In this case, the `matches` method checks if the actual string contains the expected substring, and the `describeTo` method provides a description of the matcher's expected value.