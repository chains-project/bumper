```java
private Matcher<String> manifestPushed() {
    return new TypeSafeMatcher<String>() {
        private String expectedString;

        public void describeTo(Description description) {
            expectedString = String.format("latest: digest: %s", image.digest());
            description.appendText(expectedString);
        }

        protected boolean matchesSafely(String item) {
            expectedString = String.format("latest: digest: %s", image.digest());
            return item.contains(expectedString);
        }
    };
}
```