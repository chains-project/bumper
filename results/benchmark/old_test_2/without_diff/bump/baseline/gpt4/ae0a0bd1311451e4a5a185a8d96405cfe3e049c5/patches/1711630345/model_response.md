```java
private Matcher<String> layersAlreadyExist() {
    return new TypeSafeMatcher<String>() {
        @Override
        public void describeTo(Description description) {
            description.appendText(String.format("%s: Layer already exists", image.layer()));
        }

        @Override
        protected boolean matchesSafely(String item) {
            return item.contains(String.format("%s: Layer already exists", image.layer()));
        }
    };
}
```