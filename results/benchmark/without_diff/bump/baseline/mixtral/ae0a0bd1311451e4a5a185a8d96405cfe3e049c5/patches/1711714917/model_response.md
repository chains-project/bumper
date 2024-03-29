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

* Instead of using the `StringContains` matcher from Hamcrest, we can create a custom `TypeSafeMatcher` that checks if a string contains a specific substring.
* In the `matchesSafely` method, we use the `contains` method of the `String` class to check if the given string contains the desired substring.
* In the `describeTo` method, we provide a description of the matcher that includes the expected substring.
* This solution avoids using the `StringContains` constructor, which was causing the original error.