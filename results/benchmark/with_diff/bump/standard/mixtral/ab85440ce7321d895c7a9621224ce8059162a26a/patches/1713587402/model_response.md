Here is the proposed patch for the failing client code:
```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return new org.hamcrest.Matcher<java.lang.String>() {
        @Override
        public boolean matches(final java.lang.String actual) {
            return actual.contains(String.format("Status: Downloaded newer image for %s", image));
        }
    };
}
```
In the new library version, the `StringContains` class no longer has a `containsString` method, so I have replaced it with a custom `Matcher` implementation that checks if the actual string contains the specified substring. This should fix the error and allow the code to compile and run successfully.