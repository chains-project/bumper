```java
private Matcher<String> layersAlreadyExist() {
    return new TypeSafeMatcher<String>() {
        @Override
        protected boolean matchesSafely(final String item) {
            return item.contains(String.format("%s: Layer already exists", image.layer()));
        }

        @Override
        public void describeTo(final Description description) {
            description.appendText("Layer already exists");
        }
    };
}
```