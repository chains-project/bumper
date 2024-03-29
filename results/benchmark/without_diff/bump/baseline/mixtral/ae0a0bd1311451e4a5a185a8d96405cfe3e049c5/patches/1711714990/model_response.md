Here is a fixed version of the `imagePulled` method that should resolve the error:
```java
private static Matcher<String> imagePulled(final String image) {
    return new TypeSafeMatcher<String>() {
        @Override
        protected boolean matchesSafely(String item) {
            return item.contains(String.format("Status: Downloaded newer image for %s", image));
        }

        @Override
        public void describeTo(Description description) {
            description.appendText("a string containing the substring: Status: Downloaded newer image for " + image);
        }
    };
}
```
Explanation:

* Instead of using the `StringContains` matcher from Hamcrest, we create a custom `TypeSafeMatcher` that checks if the given string contains the desired substring.
* We override the `matchesSafely` method to perform the actual check.
* We also override the `describeTo` method to provide a meaningful description of the matcher for error messages.

Note: I'm assuming that the error is caused by a change in the Hamcrest library version that removes the `StringContains` matcher. If that's not the case, the fix might be different.