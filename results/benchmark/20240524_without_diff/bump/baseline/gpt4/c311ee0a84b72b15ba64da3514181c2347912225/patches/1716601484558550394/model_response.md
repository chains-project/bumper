```java
private Matcher<String> manifestPushed() {
    return new TypeSafeMatcher<String>() {
        String expectedString = String.format("latest: digest: %s", image.digest());

        public void describeTo(Description description) {
            description.appendText(expectedString);
        }

        protected boolean matchesSafely(String item) {
            return item.contains(expectedString);
        }
    };
}
```