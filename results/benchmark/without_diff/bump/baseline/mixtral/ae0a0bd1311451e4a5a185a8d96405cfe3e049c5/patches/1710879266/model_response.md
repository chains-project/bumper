I cannot see the full code, but I can see that the error message is related to the `StringContains` constructor. I'm assuming that `StringContains` is from the `hamcrest` library, and the constructor `StringContains(boolean negated, String substring)` is not present in the version you are using.

Instead, you can use `is(containsString(String substring)))` method introduced in `hamcrest` version 1.3, which seems to be equivalent to what you are trying to do.

Here's the patched code:

```java
private static Matcher<String> imagePulled(final String image) {
    return new TypeSafeMatcher<String>() {
        @Override
        protected boolean matchesSafely(String item) {
            return item.contains(String.format("Status: Downloaded newer image for %s", image));
        }

        @Override
        public void describeTo(Description description) {
            description.appendText("a string containing ").appendValue(image));
        }
    }.describedAs("imagePulled(" + image + ")");
}
```

```diff
- return new StringContains(
-     false,
-     String.format("Status: Downloaded newer image for %s", image)
- );
+ return new TypeSafeMatcher<String>() {
+     @Override
+     protected boolean matchesSafely(String item) {
+         return item.contains(String.format("Status: Downloaded newer image for %s", image));
+     }
+
+     @Override
+     public void describeTo(Description description) {
+         description.appendText("a string containing ").appendValue(image));
+     }
+ }.describedAs("imagePulled(" + image + ")");
```

This patch replaces the `StringContains` constructor with a custom `TypeSafeMatcher` that checks if the string contains the specified substring. The `describeTo()` method is also overridden to provide a more informative error message when the matcher fails.

Please note that you should replace the `hamcrest` library version to 1.3 or higher for the patch to work.