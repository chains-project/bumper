```java
private Matcher<String> manifestPushed() {
    String expectedString = String.format("latest: digest: %s", this.image.digest());
    return new TypeSafeMatcher<String>() {
        public void describeTo(Description description) {
            description.appendText(expectedString);
        }

        protected boolean matchesSafely(String item) {
            return item.contains(expectedString);
        }
    };
}
```