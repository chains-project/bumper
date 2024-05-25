```java
private Matcher<String> manifestPushed() {
    String expectedString = String.format("latest: digest: %s", this.image.digest());
    return new TypeSafeMatcher<String>() {
        String expected = expectedString;

        public void describeTo(Description description) {
            description.appendText(expected);
        }

        protected boolean matchesSafely(String item) {
            return item.contains(expected);
        }
    };
}
```