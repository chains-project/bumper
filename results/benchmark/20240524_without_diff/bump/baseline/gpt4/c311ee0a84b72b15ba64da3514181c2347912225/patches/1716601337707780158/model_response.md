```java
private Matcher<String> manifestPushed() {
    String expectedString = String.format("latest: digest: %s", this.image.digest());
    return new TypeSafeMatcher<String>() {
        String expected = expectedString;

        @Override
        public void describeTo(Description description) {
            description.appendText(expected);
        }

        @Override
        protected boolean matchesSafely(String item) {
            return item.contains(expected);
        }
    };
}
```