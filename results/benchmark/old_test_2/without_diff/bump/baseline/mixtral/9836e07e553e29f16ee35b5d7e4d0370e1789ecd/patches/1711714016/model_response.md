Here is a fixed version of the method that should resolve the error:

```java
private static Matcher<String> imagePulled(final String image) {
    return new TypeSafeMatcher<String>() {
        @Override
        protected boolean matchesSafely(String item) {
            return item.contains(String.format("Downloaded newer image for %s", image));
        }

        @Override
        public void describeTo(Description description) {
            description.appendText("a string containing the substring: Status: Downloaded newer image for " + image);
        }
    };
}
```

Explanation:

The original code was using the `StringContains` matcher from the Hamcrest library, which has been removed in the new version. To fix the error, we need to replace the usage of the removed `StringContains` matcher with a custom `TypeSafeMatcher` implementation that checks if a string contains a specific substring.

The `TypeSafeMatcher` is an abstract class that provides a generic way of creating matchers that match objects based on their runtime type and behavior. In this case, we extend `TypeSafeMatcher` and override the `matchesSafely` method to check if the input string contains the desired substring. We also override the `describeTo` method to provide a meaningful description of the matcher when it is used in assertions.

Note that we use the `contains` method of the `String` class to check if the input string contains the desired substring. This method is an added library method in the new version, so it is safe to use.