Here is a patch for the given code:
```java
private static Matcher<String> imagePulled(final String image) {
    String imagePattern = String.format("Status: Downloaded newer image for %s", image);
    return new TypeSafeMatcher<String>() {
        @Override
        public boolean matchesSafely(String item) {
            return item.contains(imagePattern);
        }

        @Override
        public void describeTo(Description description) {
            description.appendText("a string containing ").appendValue(image);
        }
    }.describedAs("imagePulled(" + image + ")");
}
```
The issue with the original code is that the `matchesSafely` method was missing the `public` access modifier. I added a variable `imagePattern` to make the code more readable and to avoid repeating the string concatenation.

Additionally, I would like to point out that the error message `[ERROR] /docker-adapter/src/test/java/com/artipie/docker/http/CachingProxyITCase.java:[179,78] ';' expected` suggests that the error is in a different file and line, so it might be unrelated to the code snippet provided. However, the code snippet provided does have a different issue, so the patch above should fix it.