```java
private static Matcher<String> imagePulled(final String image) {
    return new TypeSafeMatcher<String>() {
        @Override
        public void describeTo(Description description) {
            description.appendText("Status: Downloaded newer image for " + image);
        }

        @Override
        protected boolean matchesSafely(String item) {
            return item.contains(String.format("Status: Downloaded newer image for %s", image));
        }
    };
}
```